import os
import secrets
from django.shortcuts import render, redirect
from .models import *
from .client_models import *
import datetime
from .forms import *
from .client_forms import *
from .filters import *
from .decorators import unauthenticated_user, allowed_users
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from django.core.paginator import Paginator
import json
import csv
#================ Export As PDF ======================
from io import BytesIO
from django.http import HttpResponse, JsonResponse
from django.template.loader import get_template
from django.views import View
from xhtml2pdf import pisa
#=====================================================


@login_required(login_url='login')
def login_redirect_page(request):
    user = request.user
    if user.is_staff == True:
        return redirect("dashboard")

    elif user.is_staff == False:
        return redirect("c_client_profile")

    else:
        return redirect('login')


#=====================================================
#==================== Register =======================
#=====================================================

def register(request):
	if request.method == 'POST':
		form = RegisterForm(request.POST)
		if form.is_valid():
			form.save()
			client = User.objects.get(username=request.POST["username"])
			group = Group.objects.get(name='Client')
			client.groups.add(group)
			return redirect('second_step_register')
		return redirect('login')
	else:
		form = RegisterForm()

	context = {'title':'ES | Sign Up','form':form}

	return render(request, 'home/en/registration.html', context)
#=====================================================
#=====================================================
#=====================================================


#=====================================================
#===================== Profile =======================
#=====================================================
#----------------- Client's Profile ------------------
@login_required(login_url='login')
@allowed_users(allowed_roles=['Client'])
def c_client_profile(request):
	c_main_menu = 'client_profile'

	user_logged_in = request.user
	recent_messages = Mail.objects.filter(receiver=user_logged_in).filter(is_trash=0).order_by('-date_receive')[:5]
	recent_notifications = Notification.objects.filter(receiver=user_logged_in).order_by('-date_receive')[:5]


	selected_client = request.user
	client_cv = Client_CV.objects.filter(client=request.user).first()
	client_experience = Client_CV_Experiences.objects.filter(client=request.user.id)
	client_educations = Client_CV_Educations.objects.filter(client=request.user.id)
	client_courses = Client_CV_Courses.objects.filter(client=request.user.id)
	client_skills = Client_CV_Skills.objects.filter(client=request.user.id)

	context = {'title': selected_client.first_name, 'selected_client':selected_client, 
			   'client_experience':client_experience, 'client_educations':client_educations, 
			   'Client_Educations':Client_Educations, 'client_courses':client_courses, 
			   'client_skills':client_skills,  'client_cv':client_cv, 'c_main_menu':c_main_menu, 
			   'user_logged_in':user_logged_in, 'recent_messages':recent_messages,
			   'recent_notifications':recent_notifications}

	return render(request, 'candidate/en/profile/profile.html', context)
#-----------------------------------------------------

#------------------- Update Client -------------------
@login_required(login_url='login')
@allowed_users(allowed_roles=['Client'])
def second_step_register(request):	
	user_logged_in = request.user
	formset = ClientCVForm(instance=user_logged_in)
	if request.method == 'POST':
		# first_name = request.POST['first_name']
		# second_name = request.POST['second_name']
		# third_name = request.POST['third_name']
		# last_name = request.POST['last_name']
		# email = request.POST['email']
		# personal_id = request.POST['personal_id']
		# phone_primary = request.POST['phone_primary']
		# phone_secondary = request.POST['phone_secondary']
		# gender = request.POST['gender']
		# birth_date = request.POST['birth_date']
		# photo = request.FILES['photo']
		# degree = request.POST['degree']
		# city = Cities.objects.get(city_id=request.POST['city'])
		# specialization = Specializations.objects.get(specialization_id=request.POST['specialization'])
		# nationality = Nationalities.objects.get(nationality_id=request.POST['nationality'])
		
			
		# formset = Client_CV(first_name=first_name, second_name=second_name, third_name=third_name,	
		# 	last_name=last_name, email=email, personal_id=personal_id, degree=degree,
		# 	phone_primary=phone_primary, phone_secondary=phone_secondary, city=city, 
		# 	specialization=specialization, gender=gender, nationality=nationality,
		# 	birth_date=birth_date, photo=photo, client=request.user)
		# if formset:
		# 	user_update = User(first_name=first_name,last_name=last_name,
		# 						id=user_logged_in.id, password=user_logged_in.password,
		# 						last_login=user_logged_in.last_login, is_superuser=user_logged_in.is_superuser,
		# 						username=user_logged_in.username, email=user_logged_in.email,
		# 						is_staff=user_logged_in.is_staff, is_active=user_logged_in.is_active,
		# 						date_joined=user_logged_in.date_joined)
		# 	if user_logged_in:
		# 		formset.save()
		# 		user_update.save()
				return redirect('c_client_profile')

	context = {'title': 'Complete Information',
			   'formset':formset, 'user_logged_in':user_logged_in}

	return render(request, 'candidate/en/profile/cv_update.html', context)
#-----------------------------------------------------

#------------------- Update Client -------------------
@login_required(login_url='login')
@allowed_users(allowed_roles=['Client'])
def client_cv_update(request):
	c_main_menu = 'client_profile'
	
	user_logged_in = request.user
	recent_messages = Mail.objects.filter(receiver=user_logged_in).filter(is_trash=0).order_by('-date_receive')[:5]
	recent_notifications = Notification.objects.filter(receiver=user_logged_in).order_by('-date_receive')[:5]

	selected_cv = Client_CV.objects.filter(client=request.user).first()
	formset = ClientCVForm(instance=selected_cv)
	if request.method == 'POST':
		# first_name = request.POST['first_name']
		# second_name = request.POST['second_name']
		# third_name = request.POST['third_name']
		# last_name = request.POST['last_name']
		# personal_id = request.POST['personal_id']
		# phone_primary = request.POST['phone_primary']
		# phone_secondary = request.POST['phone_secondary']
		# gender = request.POST['gender']
		# birth_date = request.POST['birth_date']
		# degree = request.POST['degree']
		# bo = request.POST['bo']
		# city = Cities.objects.get(city_id=request.POST['city'])
		# specialization = Specializations.objects.get(specialization_id=request.POST['specialization'])
		# nationality = Nationalities.objects.get(nationality_id=request.POST['nationality'])
		
		# selected_cv.first_name = first_name
		# selected_cv.second_name = second_name
		# selected_cv.third_name = third_name
		# selected_cv.last_name = last_name
		# selected_cv.bio = bio
		# selected_cv.personal_id = personal_id
		# selected_cv.degree = degree
		# selected_cv.phone_primary = phone_primary
		# selected_cv.phone_secondary = phone_secondary
		# selected_cv.specialization = specialization
		# selected_cv.gender = gender
		# selected_cv.nationality = nationality
		# selected_cv.birth_date = birth_date
		# if selected_cv:
		# 	user_update = user_logged_in
		# 	user_update.first_name = first_name 
		# 	user_update.last_name = last_name 

		# 	if selected_cv:
		# 		selected_cv.save()
		# 		user_update.save()
				return redirect('c_client_profile')


	context = {'title': selected_cv, 'selected_client':selected_cv,
				'formset':formset, 'c_main_menu':c_main_menu, 
				'user_logged_in':user_logged_in, 'recent_messages':recent_messages,
			   'recent_notifications':recent_notifications}

	return render(request, 'candidate/en/profile/cv_update.html', context)
#-----------------------------------------------------
#=====================================================
#=====================================================
#=====================================================


#=====================================================
#====================== Jobs =========================
#=====================================================
#-------------------- Show Jobs ----------------------
@login_required(login_url='login')
@allowed_users(allowed_roles=['Client'])
def c_jobs(request):
	c_main_menu = 'all_jobs'
	
	user_logged_in = request.user
	recent_messages = Mail.objects.filter(receiver=user_logged_in).filter(is_trash=0).order_by('-date_receive')[:5]
	recent_notifications = Notification.objects.filter(receiver=user_logged_in).order_by('-date_receive')[:5]

	all_jobs = Jobs.objects.filter(is_available='1').order_by('-start_date')
	all_jobs_count = all_jobs.count()
	all_jobs_filter = ClientJobsFilter(request.GET, queryset=all_jobs)
	all_jobs = all_jobs_filter.qs
	results_number = all_jobs.count()
	job_applied = Job_Applied.objects.filter(client=request.user)
	applied = []
	for job in job_applied:
		applied.append(job.job.job_id)

	context = {'title':'clients', 'all_jobs':all_jobs, 'all_jobs_count':all_jobs_count,
			   'all_jobs_filter':all_jobs_filter, 'applied':applied, 
			   'results_number':results_number, 'c_main_menu':c_main_menu, 
			   'user_logged_in':user_logged_in, 'recent_messages':recent_messages,
			   'recent_notifications':recent_notifications}

	return render(request, 'candidate/en/jobs/jobs.html', context)
#-----------------------------------------------------

#-------------------- Job Details --------------------
@login_required(login_url='login')
@allowed_users(allowed_roles=['Client'])
def c_job_details(request, job_id):
	c_main_menu = 'all_jobs'
	
	user_logged_in = request.user
	recent_messages = Mail.objects.filter(receiver=user_logged_in).filter(is_trash=0).order_by('-date_receive')[:5]
	recent_notifications = Notification.objects.filter(receiver=user_logged_in).order_by('-date_receive')[:5]

	selected_job = Jobs.objects.get(job_id=job_id)
	clients_applied = Job_Applied.objects.filter(job_id=job_id).count()
	date_now = datetime.datetime.now().date()
	job_applied = Job_Applied.objects.filter(client=request.user)
	applied = []
	for job in job_applied:
		applied.append(job.job.job_id)

	context = {'title':'{} - {}'.format(selected_job.company.english_name, selected_job.title), 'date_now':date_now, 'applied':applied,
			   'selected_job':selected_job, 'clients_applied':clients_applied, 'c_main_menu':c_main_menu, 
			   'user_logged_in':user_logged_in, 'recent_messages':recent_messages,
			   'recent_notifications':recent_notifications}

	return render(request, 'candidate/en/jobs/job_details.html', context)
#-------------------------------------------------------

#--------------------- Job Apply -----------------------
@login_required(login_url='login')
@allowed_users(allowed_roles=['Client'])
def c_job_apply(request, job_id):
	c_main_menu = 'all_jobs'
	
	user_logged_in = request.user
	recent_messages = Mail.objects.filter(receiver=user_logged_in).filter(is_trash=0).order_by('-date_receive')[:5]
	recent_notifications = Notification.objects.filter(receiver=user_logged_in).order_by('-date_receive')[:5]

	selected_job = Jobs.objects.get(job_id=job_id)
	clients_applied = request.user
	if Client_CV.objects.filter(client=user_logged_in).all():
		client_data = ClientApplyForm(instance=clients_applied.client_cv)
		formset = JobApplyForm()
		if request.method == 'POST':
			cover_letter = request.POST['cover_letter']
			resume = request.FILES.get('resume')
			selected_client = Client_CV.objects.get(client=user_logged_in)
			formset = Job_Applied(first_name=selected_client.first_name, second_name=selected_client.second_name,
				third_name=selected_client.third_name, last_name=selected_client.last_name,
				email=selected_client.email, personal_id=selected_client.personal_id, degree=selected_client.degree,
				phone_primary=selected_client.phone_primary, phone_secondary=selected_client.phone_secondary, 
				gender=selected_client.gender, nationality=selected_client.nationality, specialization=selected_client.specialization,
				birth_date=selected_client.birth_date, job=selected_job, client=request.user, city=selected_client.city,
				cover_letter=cover_letter, resume=resume)
			if formset:
				formset.save()
				return redirect('c_job_details', selected_job.job_id)

		context = {'title':'Apply to {}'.format(selected_job.company.english_name), 'selected_job':selected_job, 
				'clients_applied':clients_applied, 'formset':formset, 'c_main_menu':c_main_menu, 
				'user_logged_in':user_logged_in, 'recent_messages':recent_messages,
				'recent_notifications':recent_notifications, 'client_data':client_data}
	 
		return render(request, 'candidate/en/jobs/job_apply.html', context)
	else:
		return redirect('second_step_register')
#-------------------------------------------------------


#--------------------- Job Apply -----------------------
@login_required(login_url='login')
@allowed_users(allowed_roles=['Client'])
def c_job_update_apply(request, job_apply_id):
	c_main_menu = 'all_jobs'
	
	user_logged_in = request.user
	recent_messages = Mail.objects.filter(receiver=user_logged_in).filter(is_trash=0).order_by('-date_receive')[:5]
	recent_notifications = Notification.objects.filter(receiver=user_logged_in).order_by('-date_receive')[:5]

	selected_job_apply = Job_Applied.objects.get(apply_id=job_apply_id)
	clients_applied = request.user
	formset = ClientCVForm(instance=clients_applied.client_cv)
	# if request.method == 'POST':
	# 	first_name = request.POST['first_name']
	# 	second_name = request.POST['second_name']
	# 	third_name = request.POST['third_name']
	# 	last_name = request.POST['last_name']
	# 	email = request.POST['email']
	# 	personal_id = request.POST['personal_id']
	# 	phone_primary = request.POST['phone_primary']
	# 	phone_secondary = request.POST['phone_secondary']
	# 	gender = request.POST['gender']
	# 	birth_date = request.POST['birth_date']
	# 	degree = request.POST['degree']
	# 	city = Cities.objects.get(city_id=request.POST['city'])
	# 	specialization = Specializations.objects.get(specialization_id=request.POST['specialization'])
	# 	nationality = Nationalities.objects.get(nationality_id=request.POST['nationality'])
	# 	formset = Job_Applied(first_name=first_name, second_name=second_name, third_name=third_name,
	# 		last_name=last_name, email=email, personal_id=personal_id, degree=degree,
	# 		phone_primary=phone_primary, phone_secondary=phone_secondary, city=city, 
	# 		specialization=specialization, gender=gender, nationality=nationality,
	# 		birth_date=birth_date, job=selected_job_apply.job, client=request.user, 
	# 		apply_id=job_apply_id, date=selected_job_apply.date)
	# 	if formset:
	# 		# formset.save()
	# 		return redirect('c_applied_job_details', selected_job_apply.job.job_id)

	context = {'title':'Apply to {}'.format(selected_job_apply.job.company.english_name),
			'clients_applied':clients_applied, 'formset':formset, 'c_main_menu':c_main_menu, 
			'user_logged_in':user_logged_in, 'recent_messages':recent_messages,
			   'recent_notifications':recent_notifications}

	return render(request, 'candidate/en/jobs/job_update_apply.html', context)
#-------------------------------------------------------


#----------------- Job Cancel Apply --------------------
@login_required(login_url='login')
@allowed_users(allowed_roles=['Client'])
def c_job_cancel_apply(request, job_id):
	c_main_menu = 'all_jobs'
	
	user_logged_in = request.user
	recent_messages = Mail.objects.filter(receiver=user_logged_in).filter(is_trash=0).order_by('-date_receive')[:5]
	recent_notifications = Notification.objects.filter(receiver=user_logged_in).order_by('-date_receive')[:5]

	selected_job = Jobs.objects.get(job_id=job_id)
	clients_applied = request.user
	if request.method == 'POST':
		cancel_apply = Job_Applied.objects.get(job=selected_job, client=clients_applied)	
		cancel_apply.delete()
		return redirect('c_job_details', selected_job.job_id)

	context = {'title':'Cancel Apply - {}'.format(selected_job.title), 
				'item':selected_job, 'c_main_menu':c_main_menu, 'user_logged_in':user_logged_in, 
				'recent_messages':recent_messages,
			   'recent_notifications':recent_notifications}

	return render(request, 'candidate/en/jobs/job_cancel_apply.html', context)
#-------------------------------------------------------

#--------------  Client's Applied Jobs -----------------
@login_required(login_url='login')
@allowed_users(allowed_roles=['Client'])
def client_applied_jobs(request):
	c_main_menu = 'all_jobs'
	
	user_logged_in = request.user
	recent_messages = Mail.objects.filter(receiver=user_logged_in).filter(is_trash=0).order_by('-date_receive')[:5]
	recent_notifications = Notification.objects.filter(receiver=user_logged_in).order_by('-date_receive')[:5]

	all_applied_jobs = Job_Applied.objects.filter(client=request.user).all().order_by('-date')
	applied = []
	for job in all_applied_jobs:
		applied.append(job.job.job_id)

	context = {'title':'Applied Clients', 'all_applied_jobs':all_applied_jobs, 
				'applied':applied, 'c_main_menu':c_main_menu, 'user_logged_in':user_logged_in, 
				'recent_messages':recent_messages,
			   'recent_notifications':recent_notifications}

	return render(request, 'candidate/en/jobs/client_applied_jobs.html', context)
#-------------------------------------------------------

#---------------- Applied Job Details ------------------
@login_required(login_url='login')
@allowed_users(allowed_roles=['Client'])
def c_applied_job_details(request, job_id):
	c_main_menu = 'all_jobs'
	
	user_logged_in = request.user
	recent_messages = Mail.objects.filter(receiver=user_logged_in).filter(is_trash=0).order_by('-date_receive')[:5]
	recent_notifications = Notification.objects.filter(receiver=user_logged_in).order_by('-date_receive')[:5]

	selected_job = Jobs.objects.get(job_id=job_id)
	selected_client = request.user
	applied_job = Job_Applied.objects.get(job=selected_job, client=selected_client)

	context = {'title':'{} - {}'.format(selected_job.company.english_name, selected_job.title), 
				'applied_job':applied_job, 'c_main_menu':c_main_menu, 'user_logged_in':user_logged_in, 
				'recent_messages':recent_messages,
			   'recent_notifications':recent_notifications}

	return render(request, 'candidate/en/jobs/applied_job_details.html', context)
#-------------------------------------------------------
#=====================================================
#=====================================================
#=====================================================


#=====================================================
#================ Client Experience ==================
#=====================================================
#-------------- Show Client Experience ---------------
@login_required(login_url='login')
@allowed_users(allowed_roles=['Client'])
def client_cv_experience(request, experience_id):
	c_main_menu = 'client_profile'
	
	user_logged_in = request.user
	recent_messages = Mail.objects.filter(receiver=user_logged_in).filter(is_trash=0).order_by('-date_receive')[:5]
	recent_notifications = Notification.objects.filter(receiver=user_logged_in).order_by('-date_receive')[:5]

	selected_experience = Client_CV_Experiences.objects.get(experience_id=experience_id)

	context = {'title':'{} at {}'.format(selected_experience.job_title, selected_experience.company_name), 
				'selected_experience':selected_experience, 'c_main_menu':c_main_menu, 
				'user_logged_in':user_logged_in, 'recent_messages':recent_messages,
			   'recent_notifications':recent_notifications}

	return render(request, 'candidate/en/profile/experience.html', context)
#-----------------------------------------------------

#------------ Create Client Experience ---------------
@login_required(login_url='login')
@allowed_users(allowed_roles=['Client'])
def client_cv_experience_create(request):
	c_main_menu = 'client_profile'
	
	user_logged_in = request.user
	recent_messages = Mail.objects.filter(receiver=user_logged_in).filter(is_trash=0).order_by('-date_receive')[:5]
	recent_notifications = Notification.objects.filter(receiver=user_logged_in).order_by('-date_receive')[:5]

	client = Client_CV.objects.get(client=request.user)
	formset = ClientCVExperiencesForm(instance=client)
	if request.method == 'POST':
		# company_name = request.POST['company_name']
		# job_title = request.POST['job_title']
		# description = request.POST['description']
		# start_date = request.POST['start_date']
		# end_date = request.POST['end_date']
		# formset = Client_CV_Experiences(company_name=company_name, 
		# 	job_title=job_title, description=description, start_date=start_date, 
		# 	end_date=end_date, client=request.user)
		# if formset:
		# 	formset.save()
			return redirect('c_client_profile')

	context = {'title':'Create Experience', 'formset':formset, 'c_main_menu':c_main_menu, 
				'user_logged_in':user_logged_in, 'recent_messages':recent_messages,
			   'recent_notifications':recent_notifications}

	return render(request, 'candidate/en/profile/experience_create.html', context)
#-----------------------------------------------------

#------------ Update Client Experience ---------------
@login_required(login_url='login')
@allowed_users(allowed_roles=['Client'])
def client_cv_experience_update(request, experience_id): # Try to make it one form (Done)
	c_main_menu = 'client_profile'

	user_logged_in = request.user
	recent_messages = Mail.objects.filter(receiver=user_logged_in).filter(is_trash=0).order_by('-date_receive')[:5]
	recent_notifications = Notification.objects.filter(receiver=user_logged_in).order_by('-date_receive')[:5]

	client_experience = Client_CV_Experiences.objects.get(experience_id=experience_id)
	if client_experience in Client_CV_Experiences.objects.filter(client=user_logged_in).all():
		client = Client_CV.objects.get(client=request.user)
		formset = ClientCVExperiencesForm(instance=client_experience)
		if request.method == 'POST':
			# company_name = request.POST['company_name']
			# job_title = request.POST['job_title']
			# description = request.POST['description']
			# start_date = request.POST['start_date']
			# end_date = request.POST['end_date']
			# formset = Client_CV_Experiences(experience_id=experience_id, company_name=company_name, 
			# 	job_title=job_title, description=description, start_date=start_date, 
			# 	end_date=end_date, client=request.user)
			# if formset:
			# 	formset.save()
				return redirect('c_client_profile')

		context = {'title':'Update Experience', 'formset':formset, 'c_main_menu':c_main_menu, 
					'user_logged_in':user_logged_in, 'recent_messages':recent_messages,
				   'recent_notifications':recent_notifications}

		return render(request, 'candidate/en/profile/experience_update.html', context)
	else:
		return redirect('c_client_profile')
#-----------------------------------------------------

#------------ Delete Client Experience ---------------
@login_required(login_url='login')
@allowed_users(allowed_roles=['Client'])
def client_cv_experience_delete(request, experience_id):
	c_main_menu = 'client_profile'
	
	user_logged_in = request.user
	recent_messages = Mail.objects.filter(receiver=user_logged_in).filter(is_trash=0).order_by('-date_receive')[:5]
	recent_notifications = Notification.objects.filter(receiver=user_logged_in).order_by('-date_receive')[:5]

	selected_client_experience = Client_CV_Experiences.objects.get(experience_id=experience_id)
	if selected_client_experience in Client_CV_Experiences.objects.filter(client=user_logged_in).all():
		if request.method == 'POST':
			# selected_client_experience.delete()
			return redirect('c_client_profile')

		context = {'title':'Delete {}'.format(selected_client_experience.job_title), 
					'item':selected_client_experience, 'c_main_menu':c_main_menu, 
					'user_logged_in':user_logged_in, 'recent_messages':recent_messages,
				   'recent_notifications':recent_notifications}

		return render(request, 'candidate/en/profile/experience_delete.html', context)
	else:
		return redirect('c_client_profile')
#-----------------------------------------------------
#=====================================================
#=====================================================
#=====================================================


#=====================================================
#================ Client Education ===================
#=====================================================
#-------------- Show Client's Education --------------
@login_required(login_url='login')
@allowed_users(allowed_roles=['Client'])
def client_cv_education(request, education_id):
	c_main_menu = 'client_profile'
	
	user_logged_in = request.user
	recent_messages = Mail.objects.filter(receiver=user_logged_in).filter(is_trash=0).order_by('-date_receive')[:5]
	recent_notifications = Notification.objects.filter(receiver=user_logged_in).order_by('-date_receive')[:5]

	selected_education = Client_CV_Educations.objects.get(education_id=education_id)

	context = {'title':'{} at {}'.format(selected_education.title, selected_education.educational_istitution),
				'selected_education':selected_education, 'c_main_menu':c_main_menu, 
				'user_logged_in':user_logged_in, 'recent_messages':recent_messages,
			   'recent_notifications':recent_notifications}

	return render(request, 'candidate/en/profile/education.html', context)
#-----------------------------------------------------

#------------ Create Client's Education --------------
@login_required(login_url='login')
@allowed_users(allowed_roles=['Client'])
def client_cv_education_create(request):
	c_main_menu = 'client_profile'
	
	user_logged_in = request.user
	recent_messages = Mail.objects.filter(receiver=user_logged_in).filter(is_trash=0).order_by('-date_receive')[:5]
	recent_notifications = Notification.objects.filter(receiver=user_logged_in).order_by('-date_receive')[:5]

	formset = ClientCVEducationsForm()
	if request.method == 'POST':
		# educational_istitution = request.POST['educational_istitution']
		# title = request.POST['title']
		# description = request.POST['description']
		# start_date = request.POST['start_date']
		# end_date = request.POST['end_date']
		# pdf_file = request.POST['pdf_file']
		# formset = Client_CV_Educations(educational_istitution=educational_istitution, title=title, start_date=start_date, 
		# 	end_date=end_date, pdf_file=pdf_file, description=description, client=request.user)
		# if formset:
		# 	formset.save()
			return redirect('c_client_profile')

	context = {'title':'Create Education', 'formset':formset, 'c_main_menu':c_main_menu, 
				'user_logged_in':user_logged_in, 'recent_messages':recent_messages,
			   'recent_notifications':recent_notifications}

	return render(request, 'candidate/en/profile/education_create.html', context)
#-----------------------------------------------------

#------------ Update Client's Education --------------
@login_required(login_url='login')
@allowed_users(allowed_roles=['Client'])
def client_cv_education_update(request, education_id):
	c_main_menu = 'client_profile'
	
	user_logged_in = request.user
	recent_messages = Mail.objects.filter(receiver=user_logged_in).filter(is_trash=0).order_by('-date_receive')[:5]
	recent_notifications = Notification.objects.filter(receiver=user_logged_in).order_by('-date_receive')[:5]

	client_educations = Client_CV_Educations.objects.get(education_id=education_id)
	if client_educations in Client_CV_Educations.objects.filter(client=user_logged_in).all():
		formset = ClientCVEducationsForm(instance=client_educations)
		if request.method == 'POST':
			# educational_istitution = request.POST['educational_istitution']
			# title = request.POST['title']
			# start_date = request.POST['start_date']
			# end_date = request.POST['end_date']
			# pdf_file = request.POST['pdf_file']
			# formset = Client_CV_Educations(education_id=education_id, educational_istitution=educational_istitution, title=title, start_date=start_date, 
			# 	end_date=end_date, pdf_file=pdf_file, client=request.user)
			# if formset:
			# 	formset.save()
				return redirect('c_client_profile')

		context = {'title':'Update Education', 'formset':formset, 
					'education_id':education_id, 'c_main_menu':c_main_menu, 
					'user_logged_in':user_logged_in, 'recent_messages':recent_messages,
				   'recent_notifications':recent_notifications}

		return render(request, 'candidate/en/profile/education_update.html', context)
	else:
		return redirect('c_client_profile')
#-----------------------------------------------------

#------------ Delete Client's Education --------------
@login_required(login_url='login')
@allowed_users(allowed_roles=['Client'])
def client_cv_education_delete(request, education_id):
	c_main_menu = 'client_profile'
	
	user_logged_in = request.user
	recent_messages = Mail.objects.filter(receiver=user_logged_in).filter(is_trash=0).order_by('-date_receive')[:5]
	recent_notifications = Notification.objects.filter(receiver=user_logged_in).order_by('-date_receive')[:5]

	selected_client_educations = Client_CV_Educations.objects.get(education_id=education_id)
	if selected_client_educations in Client_CV_Educations.objects.filter(client=user_logged_in).all():
		if request.method == 'POST':
			# selected_client_educations.delete()
			return redirect('c_client_profile')

		context = {'title':'Delete {}'.format(selected_client_educations.title), 
					'item':selected_client_educations, 'c_main_menu':c_main_menu, 
					'user_logged_in':user_logged_in, 'recent_messages':recent_messages,
				   'recent_notifications':recent_notifications}

		return render(request, 'candidate/en/profile/education_delete.html', context)
	else:
		return redirect('c_client_profile')
#-----------------------------------------------------
#=====================================================
#=====================================================
#=====================================================


#=====================================================
#================= Client Courses ====================
#=====================================================
#-------------- Show Client's Course -----------------
@login_required(login_url='login')
@allowed_users(allowed_roles=['Client'])
def client_cv_course(request, course_id):
	c_main_menu = 'client_profile'
	
	user_logged_in = request.user
	recent_messages = Mail.objects.filter(receiver=user_logged_in).filter(is_trash=0).order_by('-date_receive')[:5]
	recent_notifications = Notification.objects.filter(receiver=user_logged_in).order_by('-date_receive')[:5]

	selected_course = Client_CV_Courses.objects.get(course_id=course_id)

	context = {'title':'{} at {}'.format(selected_course.title, selected_course.educational_istitution),
				'selected_course':selected_course, 'c_main_menu':c_main_menu, 
				'user_logged_in':user_logged_in, 'recent_messages':recent_messages,
			   'recent_notifications':recent_notifications}

	return render(request, 'candidate/en/profile/course.html', context)
#-----------------------------------------------------

#------------- Create Client's Course ----------------
@login_required(login_url='login')
@allowed_users(allowed_roles=['Client'])
def client_cv_course_create(request):
	c_main_menu = 'client_profile'
	
	user_logged_in = request.user
	recent_messages = Mail.objects.filter(receiver=user_logged_in).filter(is_trash=0).order_by('-date_receive')[:5]
	recent_notifications = Notification.objects.filter(receiver=user_logged_in).order_by('-date_receive')[:5]

	formset = ClientCVCoursesForm()
	client = Client_CV.objects.get(client=request.user)
	if request.method == 'POST':
		# educational_istitution = request.POST['educational_istitution']
		# title = request.POST['title']
		# date = request.POST['date']
		# description = request.POST['description']
		# pdf_file = request.POST['pdf_file']
		# total_hours = request.POST['total_hours']
		# formset = Client_CV_Courses(educational_istitution=educational_istitution, title=title, 
		# 	date=date, description=description, pdf_file=pdf_file, total_hours=total_hours, client=request.user)
		# if formset:
		# 	formset.save()
			return redirect('c_client_profile')

	context = {'title':'Create course', 'formset':formset, 'c_main_menu':c_main_menu, 
				'user_logged_in':user_logged_in, 'recent_messages':recent_messages,
			   'recent_notifications':recent_notifications}

	return render(request, 'candidate/en/profile/course_create.html', context)
#-----------------------------------------------------

#------------ Update Client's Course ----------------
@login_required(login_url='login')
@allowed_users(allowed_roles=['Client'])
def client_cv_course_update(request, course_id):
	c_main_menu = 'client_profile'
	
	user_logged_in = request.user
	recent_messages = Mail.objects.filter(receiver=user_logged_in).filter(is_trash=0).order_by('-date_receive')[:5]
	recent_notifications = Notification.objects.filter(receiver=user_logged_in).order_by('-date_receive')[:5]

	client_courses = Client_CV_Courses.objects.get(course_id=course_id)
	if client_courses in Client_CV_Courses.objects.filter(client=user_logged_in).all():
		formset = ClientCVCoursesForm(instance=client_courses)
		if request.method == 'POST':
			# educational_istitution = request.POST['educational_istitution']
			# title = request.POST['title']
			# date = request.POST['date']
			# description = request.POST['description']
			# pdf_file = request.POST['pdf_file']
			# total_hours = request.POST['total_hours']
			# formset = Client_CV_Courses(course_id=course_id, educational_istitution=educational_istitution, 
			# 	title=title, date=date, description=description, pdf_file=pdf_file, 
			# 	total_hours=total_hours, client=request.user)
			# if formset:
			# 	formset.save()
				return redirect('c_client_profile')

		context = {'title':'Update Course', 'formset':formset, 'course_id':course_id, 
					'c_main_menu':c_main_menu, 'user_logged_in':user_logged_in, 
					'recent_messages':recent_messages,
				   'recent_notifications':recent_notifications}

		return render(request, 'candidate/en/profile/course_update.html', context)
	else:
		return redirect('c_client_profile')
#-----------------------------------------------------

#------------ Delete Client's Course ----------------
@login_required(login_url='login')
@allowed_users(allowed_roles=['Client'])
def client_cv_course_delete(request, course_id):
	c_main_menu = 'client_profile'
	
	user_logged_in = request.user
	recent_messages = Mail.objects.filter(receiver=user_logged_in).filter(is_trash=0).order_by('-date_receive')[:5]
	recent_notifications = Notification.objects.filter(receiver=user_logged_in).order_by('-date_receive')[:5]

	selected_client_courses = Client_CV_Courses.objects.get(course_id=course_id)
	if selected_client_courses in Client_CV_Courses.objects.filter(client=user_logged_in).all():
		if request.method == 'POST':
			# selected_client_courses.delete()
			return redirect('c_client_profile')

		context = {'title':'Delete {}'.format(selected_client_courses.title), 'item':selected_client_courses, 
					'c_main_menu':c_main_menu, 'user_logged_in':user_logged_in, 
					'recent_messages':recent_messages,
				   'recent_notifications':recent_notifications}

		return render(request, 'candidate/en/profile/course_delete.html', context)
	else:
		return redirect('c_client_profile')
#-----------------------------------------------------
#=====================================================
#=====================================================
#=====================================================


#=====================================================
#================== Client Skills ====================
#=====================================================
#--------------- Show Client's Skill -----------------
@login_required(login_url='login')
@allowed_users(allowed_roles=['Client'])
def client_cv_skill(request, skill_id):
	c_main_menu = 'client_profile'
	
	user_logged_in = request.user
	recent_messages = Mail.objects.filter(receiver=user_logged_in).filter(is_trash=0).order_by('-date_receive')[:5]
	recent_notifications = Notification.objects.filter(receiver=user_logged_in).order_by('-date_receive')[:5]

	selected_skill = Client_CV_Skills.objects.get(skill_id=skill_id)

	context = {'title':'{} at {}'.format(selected_skill.title, selected_skill.educational_istitution),
				'selected_skill':selected_skill, 'c_main_menu':c_main_menu, 
				'user_logged_in':user_logged_in, 'recent_messages':recent_messages,
			   'recent_notifications':recent_notifications}

	return render(request, 'candidate/en/profile/skill.html', context)
#-----------------------------------------------------

#------------- Create Client's Skill -----------------
@login_required(login_url='login')
@allowed_users(allowed_roles=['Client'])
def client_cv_skill_create(request):
	c_main_menu = 'client_profile'
	
	user_logged_in = request.user
	recent_messages = Mail.objects.filter(receiver=user_logged_in).filter(is_trash=0).order_by('-date_receive')[:5]
	recent_notifications = Notification.objects.filter(receiver=user_logged_in).order_by('-date_receive')[:5]

	formset = ClientCVSkillsForm()
	if request.method == 'POST':
		# title = request.POST['title']
		# progress = request.POST['progress']
		# formset = Client_CV_Skills(client=user_logged_in, title=title, progress=progress)
		# if formset:
		# 	formset.save()
			return redirect('c_client_profile')

	context = {'title':'Create course', 'formset':formset, 'c_main_menu':c_main_menu, 
				'user_logged_in':user_logged_in, 'recent_messages':recent_messages,
			   'recent_notifications':recent_notifications}

	return render(request, 'candidate/en/profile/skill_create.html', context)
#-----------------------------------------------------

#------------- Update Client's Skill -----------------
@login_required(login_url='login')
@allowed_users(allowed_roles=['Client'])
def client_cv_skill_update(request, skill_id):
	c_main_menu = 'client_profile'
	
	user_logged_in = request.user
	recent_messages = Mail.objects.filter(receiver=user_logged_in).filter(is_trash=0).order_by('-date_receive')[:5]
	recent_notifications = Notification.objects.filter(receiver=user_logged_in).order_by('-date_receive')[:5]

	client_skills = Client_CV_Skills.objects.get(skill_id=skill_id)
	if client_skills in Client_CV_Skills.objects.filter(client=user_logged_in).all():
		formset = ClientCVSkillsForm(instance=client_skills)
		if request.method == 'POST':
			# title = request.POST['title']
			# progress = request.POST['progress']
			# formset = Client_CV_Skills(skill_id=client_skills.skill_id, client=user_logged_in, title=title, progress=progress)
			# if formset:
			# 	formset.save()
				return redirect('c_client_profile')

		context = {'title':'Update Course', 'formset':formset, 'skill_id':skill_id, 
					'c_main_menu':c_main_menu, 'user_logged_in':user_logged_in, 
					'recent_messages':recent_messages,
				   'recent_notifications':recent_notifications}

		return render(request, 'candidate/en/profile/skill_update.html', context)
	else:
		return redirect('c_client_profile')
#-----------------------------------------------------

#------------- Delete Client's Skill -----------------
@login_required(login_url='login')
@allowed_users(allowed_roles=['Client'])
def client_cv_skill_delete(request, skill_id):
	c_main_menu = 'client_profile'
	
	user_logged_in = request.user
	recent_messages = Mail.objects.filter(receiver=user_logged_in).filter(is_trash=0).order_by('-date_receive')[:5]
	recent_notifications = Notification.objects.filter(receiver=user_logged_in).order_by('-date_receive')[:5]

	selected_client_skills = Client_CV_Skills.objects.get(skill_id=skill_id)
	if selected_client_skills in Client_CV_Skills.objects.filter(client=user_logged_in).all():
		if request.method == 'POST':
			# selected_client_skills.delete()
			return redirect('c_client_profile')

		context = {'title':'Delete {}'.format(selected_client_skills.title), 'item':selected_client_skills, 
					'c_main_menu':c_main_menu, 'user_logged_in':user_logged_in, 
					'recent_messages':recent_messages,
				   'recent_notifications':recent_notifications}

		return render(request, 'candidate/en/profile/skill_delete.html', context)
	else:
		return redirect('c_client_profile')
#-----------------------------------------------------
#=====================================================
#=====================================================
#=====================================================


#=====================================================
#===================== Mails =========================
#=====================================================
#--------------------- Inbox -------------------------
@login_required(login_url='login')
@allowed_users(allowed_roles=['Client'])
def inbox(request):
	c_main_menu = 'mail'
	mail_nav = 'inbox'
	
	user_logged_in = request.user
	recent_messages = Mail.objects.filter(receiver=user_logged_in).filter(is_trash=0).order_by('-date_receive')[:5]
	recent_notifications = Notification.objects.filter(receiver=user_logged_in).order_by('-date_receive')[:5]

	all_mails = Mail.objects.filter(receiver=request.user).filter(is_trash=0).order_by('-date_receive').all()
	mails_count = all_mails.count()
	mails_unread_count = Mail.objects.filter(receiver=request.user).filter(is_read=0).filter(is_trash=0).all().count()

	pagination = Paginator(all_mails, 12)
	page = request.GET.get('page')
	all_mails = pagination.get_page(page)

	context = {'title':'Index', 'all_mails':all_mails, 'mail_nav':'inbox',
			'mails_count':mails_count, 'mails_unread_count':mails_unread_count, 
			'c_main_menu':c_main_menu, 'user_logged_in':user_logged_in, 
			'recent_messages':recent_messages,
			   'recent_notifications':recent_notifications}
	
	return render(request, 'candidate/en/mails/inbox.html', context)
#-----------------------------------------------------

#------------------ Unread Mails -------------------
@login_required(login_url='login')
@allowed_users(allowed_roles=['Client'])
def unread_mails(request):
	c_main_menu = 'mail'
	mail_nav = 'unread'
	
	user_logged_in = request.user
	recent_messages = Mail.objects.filter(receiver=user_logged_in).filter(is_trash=0).order_by('-date_receive')[:5]
	recent_notifications = Notification.objects.filter(receiver=user_logged_in).order_by('-date_receive')[:5]

	all_mails = Mail.objects.filter(receiver=request.user).filter(is_read=0).filter(is_trash=0).order_by('-date_receive').all()
	mails_count = all_mails.count()
	mails_unread_count = Mail.objects.filter(receiver=request.user).filter(is_read=0).filter(is_trash=0).all().count()
	
	pagination = Paginator(all_mails, 12)
	page = request.GET.get('page')
	all_mails = pagination.get_page(page)

	context = {'title':'Unread Messages', 'all_mails':all_mails, 'mail_nav':'unread',
			'mails_count':mails_count, 'mails_unread_count':mails_unread_count, 
			'c_main_menu':c_main_menu, 'user_logged_in':user_logged_in, 
			'recent_messages':recent_messages,
			   'recent_notifications':recent_notifications}
	
	return render(request, 'candidate/en/mails/inbox.html', context)
#-----------------------------------------------------

#------------------ Read Mails ---------------------
@login_required(login_url='login')
@allowed_users(allowed_roles=['Client'])
def read_mails(request):
	c_main_menu = 'mail'
	mail_nav = 'read'
	
	user_logged_in = request.user
	recent_messages = Mail.objects.filter(receiver=user_logged_in).filter(is_trash=0).order_by('-date_receive')[:5]
	recent_notifications = Notification.objects.filter(receiver=user_logged_in).order_by('-date_receive')[:5]

	all_mails = Mail.objects.filter(receiver=request.user).filter(is_read=1).filter(is_trash=0).order_by('-date_receive').all()
	mails_count = all_mails.count()
	mails_unread_count = Mail.objects.filter(receiver=request.user).filter(is_read=0).filter(is_trash=0).all().count()
	
	pagination = Paginator(all_mails, 12)
	page = request.GET.get('page')
	all_mails = pagination.get_page(page)

	context = {'title':'Read Messages', 'all_mails':all_mails, 'mail_nav':'read',
			'mails_count':mails_count, 'mails_unread_count':mails_unread_count, 
			'c_main_menu':c_main_menu, 'user_logged_in':user_logged_in, 
			'recent_messages':recent_messages,
			   'recent_notifications':recent_notifications}
	
	return render(request, 'candidate/en/mails/inbox.html', context)
#-----------------------------------------------------

#------------------ Trash Mails --------------------
@login_required(login_url='login')
@allowed_users(allowed_roles=['Client'])
def trash_mails(request):
	c_main_menu = 'mail'
	mail_nav = 'trash'
	
	user_logged_in = request.user
	recent_messages = Mail.objects.filter(receiver=user_logged_in).filter(is_trash=0).order_by('-date_receive')[:5]
	recent_notifications = Notification.objects.filter(receiver=user_logged_in).order_by('-date_receive')[:5]

	all_mails = Mail.objects.filter(receiver=request.user).filter(is_trash=1).order_by('-date_receive').all()
	mails_count = all_mails.count()
	mails_unread_count = Mail.objects.filter(receiver=request.user).filter(is_read=0).filter(is_trash=0).all().count()
	
	pagination = Paginator(all_mails, 12)
	page = request.GET.get('page')
	all_mails = pagination.get_page(page)

	context = {'title':'Trash Messages', 'all_mails':all_mails, 'mail_nav':'trash',
			'mails_count':mails_count, 'mails_unread_count':mails_unread_count, 
			'c_main_menu':c_main_menu, 'user_logged_in':user_logged_in, 
			'recent_messages':recent_messages,
			   'recent_notifications':recent_notifications}
	
	return render(request, 'candidate/en/mails/inbox.html', context)
#-----------------------------------------------------

#-------------------- Read Mail ----------------------
@login_required(login_url='login')
@allowed_users(allowed_roles=['Client'])
def mail_read(request, mail_id, mail_nav):
	c_main_menu = 'mail'
	user_logged_in = request.user
	recent_messages = Mail.objects.filter(receiver=user_logged_in).filter(is_trash=0).order_by('-date_receive')[:5]
	recent_notifications = Notification.objects.filter(receiver=user_logged_in).order_by('-date_receive')[:5]

	mails_unread_count = Mail.objects.filter(receiver=request.user).filter(is_read=0).filter(is_trash=0).all().count()
	selected_mail = Mail.objects.get(mail_id=mail_id)
	all_replays = Mail_Replay.objects.filter(mail=selected_mail).all()
	formset = Mail(mail_id=mail_id, receiver=selected_mail.receiver, 
		sender=selected_mail.sender, message=selected_mail.message, 
		date_receive=selected_mail.date_receive, title=selected_mail.title, 
		is_read=1, is_trash=selected_mail.is_trash)
	if formset:
		formset.save()
	if request.method == 'POST':
		message = request.POST['message']
		receiver_mail_replay = Mail_Replay(sender="{} {}".format(user_logged_in.first_name, user_logged_in.last_name),
			mail=Mail.objects.get(mail_id=mail_id), message=message, is_admin=0)
		if receiver_mail_replay:
			receiver_mail_replay.save()
		sender_mail_replay = Sent_Mail_Replay(replay_id=receiver_mail_replay.replay_id,
			sender=request.user.username, mail=Sent_Mail.objects.get(mail_id=mail_id),
			message=message, is_admin=0)
		if sender_mail_replay:
			sender_mail_replay.save()
			return redirect('mail_read', mail_id, mail_nav)
	
	context = {'title':'{}'.format(selected_mail.title), 'selected_mail':selected_mail, 
				'mails_unread_count':mails_unread_count, 'mail_nav':mail_nav, 
				'c_main_menu':c_main_menu, 'user_logged_in':user_logged_in, 
				'recent_messages':recent_messages, 'all_replays':all_replays,
			   'recent_notifications':recent_notifications}
	
	return render(request, 'candidate/en/mails/mail_read.html', context)
#-----------------------------------------------------

#--------------- Move Mail to Trash ------------------
@login_required(login_url='login')
@allowed_users(allowed_roles=['Client'])
def mail_trash(request, mail_id):
	c_main_menu = 'mail'
	
	selected_mail = Mail.objects.get(mail_id=mail_id)
	formset = Mail(mail_id=mail_id, receiver=selected_mail.receiver, 
	sender=selected_mail.sender, message=selected_mail.message, 
	date_receive=selected_mail.date_receive, title=selected_mail.title, 
	is_read=selected_mail.is_read, is_trash=1)
	if formset:
		formset.save()
		
		return redirect('trash_mails')
#-----------------------------------------------------

#--------------- Sent Mail to Inbox ------------------
@login_required(login_url='login')
@allowed_users(allowed_roles=['Client'])
def mail_to_inbox(request, mail_id):
	c_main_menu = 'mail'
	
	selected_mail = Mail.objects.get(mail_id=mail_id)
	formset = Mail(mail_id=mail_id, receiver=selected_mail.receiver, 
	sender=selected_mail.sender, message=selected_mail.message, 
	date_receive=selected_mail.date_receive, title=selected_mail.title, 
	is_read=selected_mail.is_read, is_trash=0)
	if formset:
		formset.save()
		
		return redirect('inbox')
#-----------------------------------------------------

#------------------- Delete Mail ---------------------
@login_required(login_url='login')
@allowed_users(allowed_roles=['Client'])
def mail_delete(request, mail_id):
	c_main_menu = 'mail'
	
	user_logged_in = request.user
	recent_messages = Mail.objects.filter(receiver=user_logged_in).filter(is_trash=0).order_by('-date_receive')[:5]
	recent_notifications = Notification.objects.filter(receiver=user_logged_in).order_by('-date_receive')[:5]

	selected_mail = Mail.objects.get(mail_id=mail_id)
	if request.method == 'POST':
		# selected_mail.delete()
		return redirect('inbox')
	
	context = {'title':'Delete the Massege', 'item':selected_mail, 
				'c_main_menu':c_main_menu, 'user_logged_in':user_logged_in, 
				'recent_messages':recent_messages,
			   'recent_notifications':recent_notifications}
	
	return render(request, 'candidate/en/mails/mail_delete.html', context)
#-----------------------------------------------------

#--------------- Make Mail Unread ------------------
@login_required(login_url='login')
@allowed_users(allowed_roles=['Client'])
def mail_to_unread(request, mail_id):
	c_main_menu = 'mail'
	
	selected_mail = Mail.objects.get(mail_id=mail_id)
	formset = Mail(mail_id=mail_id, receiver=selected_mail.receiver, 
	sender=selected_mail.sender, message=selected_mail.message, 
	date_receive=selected_mail.date_receive, title=selected_mail.title, 
	is_read=0, is_trash=selected_mail.is_trash)
	if formset:
		formset.save()
		
		return redirect('inbox')
#-----------------------------------------------------

#-------------------- Replays ------------------------
@login_required(login_url='login')
@allowed_users(allowed_roles=['Client'])
def replays(request):
	c_main_menu = 'mail'
	mail_nav = 'replays'
	
	user_logged_in = request.user
	recent_messages = Mail.objects.filter(receiver=user_logged_in).filter(is_trash=0).order_by('-date_receive')[:5]
	recent_notifications = Notification.objects.filter(receiver=user_logged_in).order_by('-date_receive')[:5]

	all_mails = Mail.objects.filter(receiver=request.user).all()
	all_replays = Mail_Replay.objects.filter(mail__in=all_mails).order_by('-date').all()
	mails_unread_count = Mail.objects.filter(receiver=request.user).filter(is_read=0).filter(is_trash=0).all().count()

	pagination = Paginator(all_replays, 12)
	page = request.GET.get('page')
	all_replays = pagination.get_page(page)

	context = {'title':'Replays', 'all_replays':all_replays, 'mail_nav':mail_nav,
				'mails_unread_count':mails_unread_count, 
				'c_main_menu':c_main_menu, 'user_logged_in':user_logged_in, 
				'recent_messages':recent_messages,
				'recent_notifications':recent_notifications}
	
	return render(request, 'candidate/en/mails/replays.html', context)
#-----------------------------------------------------

#------------------- Mail Replay ---------------------
# @login_required(login_url='login')
# @allowed_users(allowed_roles=['Client'])
# def mail_replay(request, mail_id, mail_nav):
# 	c_main_menu = 'mail'
	
# 	selected_message = Mail.objects.get(id=mail_id)
	
# 	if request.method == 'POST':
# 		message = request.POST['message']
# 		receiver_mail_replay = Mail_Replay(sender=request.user, mail=Mail.objects.get(id=mail_id), message=message)
# 		if receiver_mail_replay:
# 			receiver_mail_replay.save()
# 		sender_mail = Sent_Mail_Replay(replay_id=receiver_mail_replay.replay_id, sender=request.user, mail=Sent_Mail.objects.get(id=mail_id), message=message)
# 		if sender_mail:
# 			sender_mail_replay.save()
# 			return redirect('mail_read', mail_id, mail_nav)


#-----------------------------------------------------
#=====================================================
#=====================================================
#=====================================================


#=====================================================
#================= Client Mail PDF ===================
#=====================================================
#-------------- PDF Client Mail view -----------------
@login_required(login_url='login')
@allowed_users(allowed_roles=['Client'])
def pdf_client_mail_view(request, mail_id):
	template = get_template('pdf/es_pdf_client_mail.html')
	selected_mail = Mail.objects.get(mail_id=mail_id)
	data = {'title':selected_mail.title,
			'receiver':selected_mail.receiver,
			'sender':selected_mail.sender,
			'message':selected_mail.message,
			'date_receive':selected_mail.date_receive}
	html = template.render(data)
	result = BytesIO()
	pdf = pisa.pisaDocument(BytesIO(html.encode('cp1252')), result)
	if not pdf.err:
		pdf = HttpResponse(result.getvalue(), content_type='application/pdf')
	
	return HttpResponse(pdf, content_type='application/pdf')
#-----------------------------------------------------

#------------- PDF Client Mail Download --------------
@login_required(login_url='login')
@allowed_users(allowed_roles=['Client'])
def pdf_client_mail_download(request, mail_id):
	template = get_template('pdf/es_pdf_client_mail.html')
	selected_mail = Mail.objects.get(mail_id=mail_id)
	data = {'title':selected_mail.title,
			'receiver':selected_mail.receiver,
			'sender':selected_mail.sender,
			'message':selected_mail.message,
			'date_receive':selected_mail.date_receive}
	html = template.render(data)
	result = BytesIO()
	pdf = pisa.pisaDocument(BytesIO(html.encode('cp1252')), result)
	if not pdf.err:
		pdf = HttpResponse(result.getvalue(), content_type='application/pdf')
	response = HttpResponse(pdf, content_type='application/pdf')
	file_name = "%s" %(selected_mail.title)
	content = "attachment; filename='%s.pdf'" %(file_name)
	response['Content-Disposition'] = content
	
	return response
#-----------------------------------------------------
#=====================================================
#=====================================================
#=====================================================


#=====================================================
#============== Client Notifications =================
#=====================================================
#------------------ Notifications --------------------
@login_required(login_url='login')
@allowed_users(allowed_roles=['Client'])
def notifications(request):	
	user_logged_in = request.user
	recent_messages = Mail.objects.filter(receiver=user_logged_in).filter(is_trash=0).order_by('-date_receive')[:5]
	recent_notifications = Notification.objects.filter(receiver=user_logged_in).order_by('-date_receive')[:5]

	all_notifications = Notification.objects.filter(receiver=request.user).order_by('-date_receive').all()
	# notifications_count = all_notifications.count()
	notifications_unread_count = Notification.objects.filter(receiver=request.user).filter(is_read=0).all().count()

	context = {'title':'Notifications', 'all_notifications':all_notifications, 'notification_nav':'inbox',
			   'notifications_unread_count':notifications_unread_count, 'user_logged_in':user_logged_in, 
			   'recent_messages':recent_messages, 'recent_notifications':recent_notifications}
	
	return render(request, 'candidate/en/notifications/notifications_all.html', context)
#-----------------------------------------------------


#------------------ Notifications --------------------
@login_required(login_url='login')
@allowed_users(allowed_roles=['Client'])
def unread_notifications(request):	
	notification_menu = 'unread'
	user_logged_in = request.user
	recent_messages = Mail.objects.filter(receiver=user_logged_in).filter(is_trash=0).order_by('-date_receive')[:5]
	recent_notifications = Notification.objects.filter(receiver=user_logged_in).order_by('-date_receive')[:5]

	all_notifications = Notification.objects.filter(receiver=request.user).filter(is_read=0).order_by('-date_receive').all()
	# notifications_count = all_notifications.count()
	notifications_unread_count = all_notifications.count()

	context = {'title':'Unread Notifications', 'all_notifications':all_notifications, 'notification_nav':'inbox',
			   'notifications_unread_count':notifications_unread_count, 'user_logged_in':user_logged_in, 
			   'recent_messages':recent_messages, 'recent_notifications':recent_notifications,
			   'notification_menu':notification_menu}
	
	return render(request, 'candidate/en/notifications/notifications_unread.html', context)
#-----------------------------------------------------


#-------------- Show Client's notification -----------
@login_required(login_url='login')
@allowed_users(allowed_roles=['Client'])
def notification_read(request, notification_id):
	c_main_menu = 'client_profile'
	
	user_logged_in = request.user
	recent_messages = Mail.objects.filter(receiver=user_logged_in).filter(is_trash=0).order_by('-date_receive')[:5]
	recent_notifications = Notification.objects.filter(receiver=user_logged_in).order_by('-date_receive')[:5]

	selected_notification = Notification.objects.get(notification_id=notification_id)
	formset = Notification(notification_id=notification_id, receiver=selected_notification.receiver, 
		job=selected_notification.job, message=selected_notification.message, 
		date_receive=selected_notification.date_receive, title=selected_notification.title, 
		is_read=1)
	if formset:
		formset.save()

	context = {'title':'{}'.format(selected_notification.title),
				'selected_notification':selected_notification, 'c_main_menu':c_main_menu, 
				'user_logged_in':user_logged_in, 'recent_messages':recent_messages,
			   'recent_notifications':recent_notifications}

	return render(request, 'candidate/en/notifications/notification_read.html', context)
#-----------------------------------------------------


#-------------- Show Client's notification -----------
@login_required(login_url='login')
@allowed_users(allowed_roles=['Client'])
def mark_notifications_read(request):
	c_main_menu = 'client_profile'
	
	user_logged_in = request.user
	recent_messages = Mail.objects.filter(receiver=user_logged_in).filter(is_trash=0).order_by('-date_receive')[:5]
	recent_notifications = Notification.objects.filter(receiver=user_logged_in).order_by('-date_receive')[:5]

	all_notifications = Notification.objects.filter(is_read=0).all()
	for notification in all_notifications:
		formset = Notification(notification_id=notification.notification_id, receiver=notification.receiver, 
								job=notification.job, message=notification.message, 
								date_receive=notification.date_receive, title=notification.title, 
								is_read=1)
		if formset:
			formset.save()


	return redirect('notifications')
#-----------------------------------------------------


#------------- Delete Client's Skill -----------------
@login_required(login_url='login')
@allowed_users(allowed_roles=['Client'])
def notification_delete(request, notification_id):
	c_main_menu = 'client_profile'
	
	user_logged_in = request.user
	recent_messages = Mail.objects.filter(receiver=user_logged_in).filter(is_trash=0).order_by('-date_receive')[:5]
	recent_notifications = Notification.objects.filter(receiver=user_logged_in).order_by('-date_receive')[:5]
	
	selected_notification = Notification.objects.get(notification_id=notification_id)
	if request.method == 'POST':
		# selected_notification.delete()
		return redirect('c_client_profile')

	context = {'title':'Delete {}'.format(selected_notification.title), 'item':selected_notification, 
				'c_main_menu':c_main_menu, 'user_logged_in':user_logged_in, 
				'recent_messages':recent_messages, 'recent_notifications':recent_notifications}

	return render(request, 'candidate/en/notifications/notification_delete.html', context)
#-----------------------------------------------------
#=====================================================
#=====================================================
#=====================================================


#------------ Clients' CVs PDF Download --------------
@login_required(login_url='login')
@allowed_users(allowed_roles=['Client'])
def cv_download(request):
	template = get_template('employer/en/pdf/cv_pdf.html')
	selected_client = request.user
	client_cv = Client_CV.objects.get(client=selected_client)
	client_experience = Client_CV_Experiences.objects.filter(client=selected_client).all()
	client_courses = Client_CV_Courses.objects.filter(client=selected_client).all()
	client_skills = Client_CV_Skills.objects.filter(client=selected_client).all()
	client_educations = Client_CV_Educations.objects.filter(client=selected_client).all()
	# data = {
	# 		'selected_client':selected_client,
	# 		'client_cv':client_cv,
	# 		'client_experience':client_experience,
	# 		'client_courses':client_courses,
	# 		'client_skills':client_skills,
	# 		'client_educations':client_educations,
	# 		}

	result = {}

	result["Information"] = {"first_name":client_cv.first_name, "second_name":client_cv.second_name, "third_name":client_cv.third_name, "last_name":client_cv.last_name,
	"summary":client_cv.bio, "specialization":client_cv.specialization.english_name}

	result["Contact"] = {"email":client_cv.email, "phone1":client_cv.phone_primary,
	"phone2":client_cv.phone_secondary, "location":client_cv.city.english_name}

	result["Education"] = [ {"title":education.title, "istitution":education.educational_istitution,
		"description":education.description, "start_date":str(education.start_date), "end_date":str(education.end_date)} for education in client_educations ]

	result["Experience"] = [ {"title":experience.job_title, "company":experience.company_name,
		"description":experience.description, "start_date":str(experience.start_date), "end_date":str(experience.end_date)} for experience in client_experience ]

	result["Courses"] = [ {"title":course.title, "istitution":course.educational_istitution,
		"description":course.description, "date":str(course.date), "total_hours":str(course.total_hours)} for course in client_courses ]

	result["Skills"] = [ skill.title for skill in client_skills ]

	result = json.dumps(result)
	print(result)

	with open("sample.json", "w") as outfile:
		outfile.write(result)

	return result
	# html = template.render(data)
	# result = BytesIO()
	# pdf = pisa.pisaDocument(BytesIO(html.encode('cp1252')), result)
	
	# if not pdf.err:
	# 	pdf = HttpResponse(result.getvalue(), content_type='application/pdf')
	# response = HttpResponse(pdf, content_type='application/pdf')
	# file_name = "%s" %(selected_client.first_name)
	# content = "attachment; filename='%s.pdf'" %(file_name)
	# response['Content-Disposition'] = content
	
	# return response
#-----------------------------------------------------
#=====================================================
#=====================================================
#=====================================================