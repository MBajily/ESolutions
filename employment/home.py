import os
import secrets
from django.shortcuts import render, redirect
from .models import *
from .client_models import *
import datetime
from .forms import *
from .client_forms import *
from .filters import *
from ES.settings import MEDIA_ROOT
from django.contrib.auth.decorators import login_required


from django.shortcuts import render, redirect
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.models import User
from django.template.loader import render_to_string
from django.db.models.query_utils import Q
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
from django.contrib import messages
# Import pafination
from django.core.paginator import Paginator


#------------------- Home Page -----------------------
def error_404(request, exception):
	user_logged_in = request.user
	if user_logged_in.id != None:
		new_messages = Mail.objects.filter(receiver=user_logged_in).filter(is_read=0).all().count()
		new_notifications = Notification.objects.filter(receiver=user_logged_in).filter(is_read=0).all().count()
	else:
		new_messages = 0
		new_notifications = 0

	context = {'title':'Excelent Solutions', 'user_logged_in':user_logged_in,
				'new_messages':new_messages, 'new_notifications':new_notifications}
	
	return render(request, 'home/en/page-not-found.html', context)
#-----------------------------------------------------

@login_required(login_url='login')
def login_redirect_page(request):

	if request.user.groups.filter(id=2):
		return redirect('c_client_profile')
		
	else:
		return redirect('dashboard')


#=====================================================
#=================== Home Page =======================
#=====================================================
#------------------- Home Page -----------------------
def home(request):
	home_menu = 'home'
	user_logged_in = request.user
	
	jobs_count = Jobs.objects.all().count()
	recent_jobs = Jobs.objects.filter(is_available='1').order_by('-start_date')[:3]
	best_candidates = User.objects.filter(groups__in='2').all()[:4]
	specializations = Specializations.objects.all()[:12]
	if user_logged_in.id != None:
		new_messages = Mail.objects.filter(receiver=user_logged_in).filter(is_read=0).all().count()
		new_notifications = Notification.objects.filter(receiver=user_logged_in).filter(is_read=0).all().count()
	else:
		new_messages = 0
		new_notifications = 0

	all_partners = Partners.objects.all()
	

	context = {'title':'Excelent Solutions', 'user_logged_in':user_logged_in,
				'new_messages':new_messages, 'new_notifications':new_notifications, 'jobs_count':jobs_count,
				'all_partners':all_partners, 'home_menu':home_menu, 'recent_jobs':recent_jobs,
				'specializations':specializations, 'best_candidates':best_candidates}
	
	return render(request, 'home/en/home.html', context)
#-----------------------------------------------------
#=====================================================
#=====================================================
#=====================================================




#-------------------- Show Jobs ----------------------
def home_jobs(request):
	home_menu = 'jobs'

	user_logged_in = request.user

	all_jobs = Jobs.objects.filter(is_available='1').order_by('-start_date')
	
	all_jobs_filter = HomeJobsFilter(request.GET, queryset=all_jobs)
	all_jobs = all_jobs_filter.qs
	results_number = all_jobs.count()

	pagination = Paginator(all_jobs, 12)
	page = request.GET.get('page')
	all_jobs = pagination.get_page(page)

	context = {'title':'ES | Jobs', 'all_jobs':all_jobs,
			   'all_jobs_filter':all_jobs_filter,
			   'results_number':results_number, 'home_menu':home_menu,
			   'user_logged_in':user_logged_in}

	return render(request, 'home/en/job.html', context)
#-----------------------------------------------------


#=====================================================
#===================== Profile =======================
#=====================================================
#----------------- Client's Profile ------------------
def candidate_profile(request, client_id):
	home_menu = 'public_profile'
	user_logged_in = request.user
	if user_logged_in.id != None:
		new_messages = Mail.objects.filter(receiver=user_logged_in).filter(is_read=0).all().count()
		new_notifications = Notification.objects.filter(receiver=user_logged_in).filter(is_read=0).all().count()
	else:
		new_messages = 0
		new_notifications = 0
	selected_user = User.objects.get(id=client_id)
	client_cv = Client_CV.objects.filter(client=selected_user).first()
	client_experience = Client_CV_Experiences.objects.filter(client=selected_user.id)
	client_educations = Client_CV_Educations.objects.filter(client=selected_user.id)
	client_courses = Client_CV_Courses.objects.filter(client=selected_user.id)
	client_skills = Client_CV_Skills.objects.filter(client=selected_user.id)

	context = {'title': selected_user.first_name, 
			   'client_experience':client_experience, 'client_educations':client_educations, 
			   'Client_Educations':Client_Educations, 'client_courses':client_courses, 
			   'client_skills':client_skills,  'client_cv':client_cv, 'home_menu':home_menu, 
			   'selected_user':selected_user, 'user_logged_in':user_logged_in,
			   'new_messages':new_messages, 'new_notifications':new_notifications}

	return render(request, 'home/en/candidate-details.html', context)
#-----------------------------------------------------


#-------------------- Job Details --------------------
def public_job_details(request, job_id):
	home_menu = 'jobs'
	
	user_logged_in = request.user
	if user_logged_in.id != None:
		new_messages = Mail.objects.filter(receiver=user_logged_in).filter(is_read=0).all().count()
		new_notifications = Notification.objects.filter(receiver=user_logged_in).filter(is_read=0).all().count()
	else:
		new_messages = 0
		new_notifications = 0

	selected_job = Jobs.objects.get(job_id=job_id)
	# job_same_specialization = Jobs.objects.filter(specialization=selected_job.specialization).order_by('-start_date')[:5]
	job_same_company = Jobs.objects.filter(company=selected_job.company).order_by('-start_date')[:5]
	clients_applied = Job_Applied.objects.filter(job_id=job_id).count()

	context = {'title':'{} - {}'.format(selected_job.company.english_name, selected_job.title),
			   'selected_job':selected_job, 'clients_applied':clients_applied, 'home_menu':home_menu, 
			   'user_logged_in':user_logged_in, 'MEDIA_ROOT':MEDIA_ROOT,
			   'new_messages':new_messages, 'new_notifications':new_notifications,
			   'job_same_company':job_same_company}

	return render(request, 'home/en/job-details.html', context)
# -------------------------------------------------------


#-------------------- Show partners ----------------------
def home_employers(request):
	home_menu = 'employers'

	user_logged_in = request.user

	all_employers = Partners.objects.all()
	
	# all_jobs_filter = JobsFilter(request.GET, queryset=all_jobs)
	# all_jobs = all_jobs_filter.qs
	# results_number = all_jobs.count()

	# pagination = Paginator(all_jobs, 12)
	# page = request.GET.get('page')
	# all_jobs = pagination.get_page(page)

	context = {'title':'ES | employers', 'all_employers':all_employers,
				'home_menu':home_menu, 'user_logged_in':user_logged_in}

	return render(request, 'home/en/employer.html', context)
#-----------------------------------------------------


#-------------------- employer Details --------------------
def employer_details(request, partner_id):
	home_menu = 'employers'
	
	user_logged_in = request.user

	selected_employer = Partners.objects.get(partner_id=partner_id)
	# job_same_specialization = Jobs.objects.filter(specialization=selected_job.specialization).order_by('-start_date')[:5]
	jobs_from_company = Jobs.objects.filter(company=selected_employer).order_by('-start_date')
	jobs_count = jobs_from_company.count()
	job_applied_count = Job_Applied.objects.filter(job__in=jobs_from_company).count()
	# clients_applied = Job_Applied.objects.filter(partner_id=partner_id).count()

	context = {'title':selected_employer.english_name,
			   'selected_employer':selected_employer, 'job_applied_count':job_applied_count, 'home_menu':home_menu, 
			   'user_logged_in':user_logged_in,	'jobs_count':jobs_count, 'jobs_from_company':jobs_from_company}

	return render(request, 'home/en/employers-details.html', context)
# -------------------------------------------------------


def password_reset_request(request):
	if request.method == "POST":
		password_reset_form = PasswordResetForm(request.POST)
		if password_reset_form.is_valid():
			data = password_reset_form.cleaned_data['email']
			associated_users = User.objects.filter(Q(email=data))
			if associated_users.exists():
				for user in associated_users:
					subject = "Password Reset Requested"
					email_template_name = "registration/password_reset_email.txt"
					c = {
					"email":user.email,
					'domain':'127.0.0.1:8000',
					'site_name': 'Website',
					"uid": urlsafe_base64_encode(force_bytes(user.pk)),
					'token': default_token_generator.make_token(user),
					'protocol': 'http',
					}
					email = render_to_string(email_template_name, c)
					try:
						send_mail(subject, email, 'admin@example.com' , [user.email], fail_silently=False)
					except BadHeaderError:

						return HttpResponse('Invalid header found.')
						
					messages.success(request, 'A message with reset password instructions has been sent to your inbox.')
					return redirect ("password_reset_done")
	password_reset_form = PasswordResetForm()
	return render(request=request, template_name="registration/password_reset.html", context={"password_reset_form":password_reset_form})


#-------------------- Show partners ----------------------
def home_candidates(request):
	home_menu = 'candidates'

	user_logged_in = request.user

	all_candidates = Client_CV.objects.all()
	
	# all_jobs_filter = JobsFilter(request.GET, queryset=all_jobs)
	# all_jobs = all_jobs_filter.qs
	# results_number = all_jobs.count()

	# pagination = Paginator(all_jobs, 12)
	# page = request.GET.get('page')
	# all_jobs = pagination.get_page(page)

	context = {'title':'ES | Candidates', 'all_candidates':all_candidates,
				'home_menu':home_menu, 'user_logged_in':user_logged_in}

	return render(request, 'home/en/candidate.html', context)
#-----------------------------------------------------



#=====================================================
#================= Contact Page ======================
#=====================================================
#----------------- Contact Page ----------------------
def contact(request):
	home_menu = 'contact'
	user_logged_in = request.user

	context = {'title':'Contact Us'}
	
	return render(request, 'home/en/contact.html', context)
#-----------------------------------------------------
#=====================================================
#=====================================================
#=====================================================