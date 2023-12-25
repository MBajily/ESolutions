from django.shortcuts import render, redirect
from .models import *
from .forms import *
from .filters import *
from django.http import HttpResponse
from .decorators import admin_only
from django.contrib.auth.decorators import login_required
import csv

#------------------ Active Clients --------------------
@login_required(login_url='login')
@admin_only
def active_clients(request):
	main_menu = 'clients'
	sub_menu = 'active_clients'
	
	all_cvs = Client_CV.objects.all()
	all_clients_count = all_cvs.count()
	all_clients_filter = ActiveClientsFilter(request.GET, queryset=all_cvs)
	all_cvs = all_clients_filter.qs
	cvs = []
	for cv in all_cvs:
		cvs.append(cv.client.id)
	all_clients = User.objects.filter(is_staff='0').filter(is_active='1').filter(id__in=cvs).all()

	context = {'title':'Active Clients', 'all_clients':all_clients, 
			   'all_clients_count':all_clients_count, 'all_clients_filter':all_clients_filter,
			   'main_menu':main_menu, 'sub_menu':sub_menu}

	return render(request, 'employer/en/active_clients/active_clients.html', context)
#------------------------------------------------------

#-------------- Active Client's Profile ----------------
@login_required(login_url='login')
@admin_only
def active_client_profile(request, client_id):
	main_menu = 'clients'
	sub_menu = 'active_clients'

	selected_client = User.objects.get(id=client_id)
	client_cv = Client_CV.objects.filter(client=selected_client)
	client_experience = Client_CV_Experiences.objects.filter(client=selected_client)
	client_educations = Client_CV_Educations.objects.filter(client=selected_client)
	client_courses = Client_CV_Courses.objects.filter(client=selected_client)
	client_skills = Client_CV_Skills.objects.filter(client=selected_client)

	context = {'title': selected_client.first_name, 'selected_client':selected_client, 
			   'client_experience':client_experience, 'client_educations':client_educations, 
			   'Client_Educations':Client_Educations, 'client_courses':client_courses, 
			   'client_skills':client_skills,  'client_cv':client_cv,
			   'main_menu':main_menu, 'sub_menu':sub_menu}

	return render(request, 'employer/en/active_clients/active_client_profile.html', context)
#-------------------------------------------------------

#--------------- Export Clients CSV ------------------
@login_required(login_url='login')
@admin_only
def export_active_clients_csv(request):
	response = HttpResponse(content_type='text/csv')
	response['Content-Disposition'] = 'attachment; filename="Active_Clients.csv"'
	writer = csv.writer(response)
	writer.writerow(['Personal ID', 'First Name', 'Last Name', 'Degree', 'Email', 'Phone Primary', 'Phone Secondary', 'Birth Date'])
	all_clients = Client_CV.objects.all()
	all_clients_filter = ClientsFilter(request.GET, queryset=all_clients)
	all_clients = all_clients_filter.qs
	clients = all_clients.values_list('personal_id', 'first_name', 'last_name', 'degree', 'email', 'phone_primary', 'phone_secondary', 'birth_date')
	
	for client in clients:
		writer.writerow(client)
	
	return response
#-----------------------------------------------------

#-------------- Show Client Experience ---------------
@login_required(login_url='login')
@admin_only
def active_client_experience(request, experience_id):
	main_menu = 'clients'
	sub_menu = 'active_clients'

	selected_experience = Client_CV_Experiences.objects.get(experience_id=experience_id)

	context = {'title':'{} at {}'.format(selected_experience.job_title, selected_experience.company_name), 
			   'selected_experience':selected_experience, 'main_menu':main_menu, 'sub_menu':sub_menu}

	return render(request, 'employer/en/active_clients/active_client_experience.html', context)
#-----------------------------------------------------

#-------------- Show Client's Education --------------
@login_required(login_url='login')
@admin_only
def active_client_education(request, education_id):
	main_menu = 'clients'
	sub_menu = 'active_clients'
	
	selected_education = Client_CV_Educations.objects.get(education_id=education_id)

	context = {'title':'{} at {}'.format(selected_education.title, selected_education.educational_istitution),
			   'selected_education':selected_education, 'main_menu':main_menu, 'sub_menu':sub_menu}

	return render(request, 'employer/en/active_clients/active_client_education.html', context)
#-----------------------------------------------------

#--------------- Show Client's Course ----------------
@login_required(login_url='login')
@admin_only
def active_client_course(request, course_id):
	main_menu = 'clients'
	sub_menu = 'active_clients'
	
	selected_course = Client_CV_Courses.objects.get(course_id=course_id)

	context = {'title':'{} at {}'.format(selected_course.title, selected_course.educational_istitution),
			   'selected_course':selected_course, 'main_menu':main_menu, 'sub_menu':sub_menu}

	return render(request, 'employer/en/active_clients/active_client_course.html', context)
#-----------------------------------------------------