from django.shortcuts import render, redirect
from .models import *
from .forms import *
from .filters import *
from django.http import HttpResponse
from .decorators import admin_only
from django.contrib.auth.decorators import login_required
import csv



#=====================================================
#==================== Clients ========================
#=====================================================
#---------------- Inactive Clients -------------------
@login_required(login_url='login')
@admin_only
def clients(request):
	main_menu = 'clients'
	sub_menu = 'inactive_clients'
	
	all_clients = Clients.objects.all().order_by('client_id')
	all_clients_count = all_clients.count()
	all_clients_filter = ClientsFilter(request.GET, queryset=all_clients)
	all_clients = all_clients_filter.qs

	context = {'title':'Inactive Clients', 'all_clients':all_clients, 
			   'all_clients_count':all_clients_count, 'all_clients_filter':all_clients_filter,
			   'main_menu':main_menu, 'sub_menu':sub_menu}

	return render(request, 'employer/en/inactive_clients/inactive_clients.html', context)
#------------------------------------------------------

#---------------- Export Clients CSV ------------------
@login_required(login_url='login')
@admin_only
def export_clients_csv(request):
	response = HttpResponse(content_type='text/csv')
	response['Content-Disposition'] = 'attachment; filename="Clients.csv"'
	writer = csv.writer(response)
	writer.writerow(['Personal ID', 'First Name', 'Last Name', 'Email', 'Phone Primary', 'Phone Secondary', 'Birth', 'Degree', 'Specialization', 'Nationality'])
	all_clients = Clients.objects.all().order_by('client_id')
	all_clients_filter = ClientsFilter(request.GET, queryset=all_clients)
	all_clients = all_clients_filter.qs
	clients = all_clients.values_list('personal_id', 'first_name', 'last_name', 'email', 'phone_primary', 'phone_secondary', 'birth_date', 'degree', 'specialization__english_name', 'nationality__english_name')
	
	for client in clients:
		writer.writerow(client)
	
	return response
#-----------------------------------------------------

#------------------ Create Client ----------------------
@login_required(login_url='login')
@admin_only
def client_create(request):
	main_menu = 'clients'
	sub_menu = 'add_client'

	formset = ClientsForm()
	
	if request.method == 'POST':
		first_name = request.POST['first_name']
		second_name = request.POST['second_name']
		third_name = request.POST['third_name']
		last_name = request.POST['last_name']
		email = request.POST['email']
		personal_id = request.POST['personal_id']
		degree = request.POST['degree']
		phone_primary = request.POST['phone_primary']
		phone_secondary = request.POST['phone_secondary']
		gender = request.POST['gender']
		birth_date = request.POST['birth_date']
		city = Cities.objects.get(city_id=request.POST['city'])
		specialization = Specializations.objects.get(specialization_id=request.POST['specialization'])
		nationality = Nationalities.objects.get(nationality_id=request.POST['nationality'])
		formset = Clients(first_name=first_name, second_name=second_name, third_name=third_name, 
			last_name=last_name, email=email, phone_primary=phone_primary, personal_id=personal_id, 
			phone_secondary=phone_secondary, photo=photo, gender=gender, birth_date=birth_date, 
			city=city, specialization=specialization, nationality=nationality, degree=degree)
		if formset:
			formset.save()
			return redirect('client_profile', formset.client_id)
			redirect('dashboard')

	context = {'title':'Add Client', 'formset':formset,
			   'main_menu':main_menu, 'sub_menu':sub_menu}

	return render(request, 'employer/en/inactive_clients/client_create.html', context)
#-------------------------------------------------------

#----------------- Client's Profile --------------------
@login_required(login_url='login')
@admin_only
def client_profile(request, client_id):
	main_menu = 'clients'
	sub_menu = 'inactive_clients'

	selected_client = Clients.objects.get(client_id=client_id)
	client_experience = Client_Experiences.objects.filter(client=client_id)
	client_educations = Client_Educations.objects.filter(client=client_id)
	client_courses = Client_Courses.objects.filter(client=client_id)
	client_skills = Client_Skills.objects.filter(client=client_id)

	context = {'title': selected_client.first_name, 'selected_client':selected_client,
			   'Client_Experiences':Client_Experiences, 'client_experience':client_experience,
			   'client_educations':client_educations, 'Client_Educations':Client_Educations,
			   'client_courses':client_courses, 'client_skills':client_skills,
			   'main_menu':main_menu, 'sub_menu':sub_menu}

	return render(request, 'employer/en/profile/client_profile.html', context)
#-------------------------------------------------------

#------------------- Update Client ---------------------
@login_required(login_url='login')
@admin_only
def client_update(request, client_id):
	main_menu = 'clients'
	sub_menu = 'inactive_clients'

	selected_client = Clients.objects.get(client_id=client_id)
	formset = ClientsForm(instance=selected_client)
	
	if request.method == 'POST':
		first_name = request.POST['first_name']
		second_name = request.POST['second_name']
		third_name = request.POST['third_name']
		last_name = request.POST['last_name']
		email = request.POST['email']
		personal_id = request.POST['personal_id']
		degree = request.POST['degree']
		phone_primary = request.POST['phone_primary']
		phone_secondary = request.POST['phone_secondary']
		photo = request.FILES['photo']
		gender = request.POST['gender']
		birth_date = request.POST['birth_date']
		city = Cities.objects.get(city_id=request.POST['city'])
		specialization = Specializations.objects.get(specialization_id=request.POST['specialization'])
		nationality = Nationalities.objects.get(nationality_id=request.POST['nationality'])

		if selected_client.photo:
			selected_client.photo.delete()
		formset = Clients(client_id=client_id, first_name=first_name, second_name=second_name, 
			third_name=third_name, last_name=last_name, email=email, phone_primary=phone_primary, 
			photo=photo, gender=gender, birth_date=birth_date, city=city, personal_id=personal_id,
			phone_secondary=phone_secondary, specialization=specialization, nationality=nationality,
			degree=degree)
		if formset:
			formset.save()
			return redirect('client_profile', client_id)

	context = {'title': selected_client.first_name, 'selected_client':selected_client,
			   'formset':formset, 'main_menu':main_menu, 'sub_menu':sub_menu}

	return render(request, 'employer/en/inactive_clients/client_update.html', context)
#-----------------------------------------------------

#------------------- Delete Client -------------------
@login_required(login_url='login')
@admin_only
def client_delete(request, client_id):
	main_menu = 'clients'
	sub_menu = 'inactive_clients'

	selected_client = Clients.objects.get(client_id=client_id)
	
	if request.method == 'POST':
		selected_client.delete()
		return redirect('/clients/')

	context = {'title':'Delete Client', 'item':selected_client,
			   'main_menu':main_menu, 'sub_menu':sub_menu}

	return render(request, 'employer/en/inactive_clients/client_delete.html', context)
#-----------------------------------------------------
#=====================================================
#=====================================================
#=====================================================


#=====================================================
#================ Client Experience ==================
#=====================================================
#-------------- Show Client Experience ---------------
@login_required(login_url='login')
@admin_only
def client_experience(request, experience_id):
	main_menu = 'clients'
	sub_menu = 'inactive_clients'

	selected_experience = Client_Experiences.objects.get(experience_id=experience_id)

	context = {'title':'{} at {}'.format(selected_experience.job_title, selected_experience.company_name), 
				'selected_experience':selected_experience,
				'main_menu':main_menu, 'sub_menu':sub_menu}

	return render(request, 'employer/en/profile/client_experience.html', context)
#-----------------------------------------------------

#------------ Create Client Experience ---------------
@login_required(login_url='login')
@admin_only
def client_experience_create(request, client_id):
	main_menu = 'clients'
	sub_menu = 'inactive_clients'
	
	client = Clients.objects.get(client_id=client_id)
	formset = ClientExperiencesForm()
	
	if request.method == 'POST':
		company_name = request.POST['company_name']
		job_title = request.POST['job_title']
		description = request.POST['description']
		start_date = request.POST['start_date']
		end_date = request.POST['end_date']
		formset = Client_Experiences(company_name=company_name, 
			job_title=job_title, description=description, start_date=start_date, 
			end_date=end_date, client=client)
		if formset:
			formset.save()
			return redirect('client_profile', client_id)

	context = {'title':'Create Experience', 'formset':formset, 'client_id':client_id,
				'main_menu':main_menu, 'sub_menu':sub_menu}

	return render(request, 'employer/en/profile/client_experience_create.html', context)
#----------------------------------------------------

#------------ Update Client Experience --------------
@login_required(login_url='login')
@admin_only
def client_experience_update(request, experience_id, client_id): # Try to make it one form (Done)
	main_menu = 'clients'
	sub_menu = 'inactive_clients'

	client_experience = Client_Experiences.objects.get(experience_id=experience_id)
	client = Clients.objects.get(client_id=client_id)
	formset = ClientExperiencesForm(instance=client_experience)
	
	if request.method == 'POST':
		company_name = request.POST['company_name']
		job_title = request.POST['job_title']
		description = request.POST['description']
		start_date = request.POST['start_date']
		end_date = request.POST['end_date']
		formset = Client_Experiences(experience_id=experience_id, company_name=company_name, 
			job_title=job_title, description=description, start_date=start_date, 
			end_date=end_date, client_id=client_id)
		if formset:
			formset.save()
			return redirect('client_profile', client_id)

	context = {'title':'Update Experience', 'formset':formset, 'client_id':client_id,
				'main_menu':main_menu, 'sub_menu':sub_menu}

	return render(request, 'employer/en/profile/client_experience_update.html', context)
#----------------------------------------------------

#------------ Delete Client Experience --------------
@login_required(login_url='login')
@admin_only
def client_experience_delete(request, client_id, experience_id):
	main_menu = 'clients'
	sub_menu = 'inactive_clients'
	
	selected_client_experience = Client_Experiences.objects.get(experience_id=experience_id)
	
	if request.method == 'POST':
		selected_client_experience.delete()
		return redirect('/client/{}/profile/'.format(client_id))

	context = {'title':'Delete {}'.format(selected_client_experience.job_title), 
			   'item':selected_client_experience, 'client_id':client_id,
			   'main_menu':main_menu, 'sub_menu':sub_menu}

	return render(request, 'employer/en/profile/client_experience_delete.html', context)
#-----------------------------------------------------
#=====================================================
#=====================================================
#=====================================================


#=====================================================
#================ Client Education ===================
#=====================================================
#-------------- Show Client's Education --------------
@login_required(login_url='login')
@admin_only
def client_education(request, education_id):
	main_menu = 'clients'
	sub_menu = 'inactive_clients'
	
	selected_education = Client_Educations.objects.get(education_id=education_id)

	context = {'title':'{} at {}'.format(selected_education.title, selected_education.educational_istitution),
				'selected_education':selected_education,
				'main_menu':main_menu, 'sub_menu':sub_menu}

	return render(request, 'employer/en/profile/client_education.html', context)
#-----------------------------------------------------

#------------ Create Client's Education --------------
@login_required(login_url='login')
@admin_only
def client_education_create(request, client_id):
	main_menu = 'clients'
	sub_menu = 'inactive_clients'
	
	formset = ClientEducationsForm()
	
	if request.method == 'POST':
		educational_istitution = request.POST['educational_istitution']
		title = request.POST['title']
		start_date = request.POST['start_date']
		end_date = request.POST['end_date']
		pdf_file = request.POST['pdf_file']
		formset = Client_Educations(educational_istitution=educational_istitution, title=title, start_date=start_date, 
			end_date=end_date, pdf_file=pdf_file, client_id=client_id)
		if formset:
			formset.save()
			return redirect('client_profile', client_id)

	context = {'title':'Create Education', 'formset':formset, 'client_id':client_id,
				'main_menu':main_menu, 'sub_menu':sub_menu}

	return render(request, 'employer/en/profile/client_education_create.html', context)
#-----------------------------------------------------

#------------ Update Client's Education --------------
@login_required(login_url='login')
@admin_only
def client_education_update(request, education_id, client_id):
	main_menu = 'clients'
	sub_menu = 'inactive_clients'
	
	client_educations = Client_Educations.objects.get(education_id=education_id)
	client = Clients.objects.get(client_id=client_id)
	formset = ClientEducationsForm(instance=client_educations)
	
	if request.method == 'POST':
		educational_istitution = request.POST['educational_istitution']
		title = request.POST['title']
		start_date = request.POST['start_date']
		end_date = request.POST['end_date']
		pdf_file = request.POST['pdf_file']
		formset = Client_Educations(education_id=education_id, educational_istitution=educational_istitution, title=title, start_date=start_date, 
			end_date=end_date, pdf_file=pdf_file, client_id=client_id)
		if formset:
			formset.save()
			return redirect('client_profile', client_id)

	context = {'title':'Update Education', 'formset':formset, 'education_id':education_id,
			   'client_id':client_id,
			   'main_menu':main_menu, 'sub_menu':sub_menu}

	return render(request, 'employer/en/profile/client_education_update.html', context)
#-----------------------------------------------------

#------------ Delete Client's Education --------------
@login_required(login_url='login')
@admin_only
def client_education_delete(request, client_id, education_id):
	main_menu = 'clients'
	sub_menu = 'inactive_clients'
	
	selected_client_educations = Client_Educations.objects.get(education_id=education_id)
	
	if request.method == 'POST':
		selected_client_educations.delete()
		return redirect('/client/{}/profile/'.format(client_id))

	context = {'title':'Delete {}'.format(selected_client_educations.title), 'item':selected_client_educations,
			   'client_id':client_id, 'main_menu':main_menu, 'sub_menu':sub_menu}

	return render(request, 'employer/en/profile/client_education_delete.html', context)
#-----------------------------------------------------
#=====================================================
#=====================================================
#=====================================================


#=====================================================
#================= Client Courses ====================
#=====================================================
#--------------- Show Client's Course ----------------
@login_required(login_url='login')
@admin_only
def client_course(request, course_id):
	main_menu = 'clients'
	sub_menu = 'inactive_clients'
	
	selected_course = Client_Courses.objects.get(course_id=course_id)

	context = {'title':'{} at {}'.format(selected_course.title, selected_course.educational_istitution),
			   'selected_course':selected_course, 'main_menu':main_menu, 'sub_menu':sub_menu}

	return render(request, 'employer/en/profile/client_course.html', context)
#-----------------------------------------------------

#------------- Create Client's Course ----------------
@login_required(login_url='login')
@admin_only
def client_course_create(request, client_id):
	main_menu = 'clients'
	sub_menu = 'inactive_clients'
	
	formset = ClientCoursesForm()
	client = Clients.objects.get(client_id=client_id)
	
	if request.method == 'POST':
		educational_istitution = request.POST['educational_istitution']
		title = request.POST['title']
		date = request.POST['date']
		description = request.POST['description']
		pdf_file = request.POST['pdf_file']
		total_hours = request.POST['total_hours']
		formset = Client_Courses(educational_istitution=educational_istitution, title=title, 
			date=date, description=description, pdf_file=pdf_file, total_hours=total_hours, client_id=client_id)
		if formset:
			formset.save()
			return redirect('client_profile', client_id)

	context = {'title':'Create course', 'formset':formset, 'client_id':client_id,
			   'main_menu':main_menu, 'sub_menu':sub_menu}

	return render(request, 'employer/en/profile/client_course_create.html', context)
#----------------------------------------------------

#------------ Update Client's Course ----------------
@login_required(login_url='login')
@admin_only
def client_course_update(request, course_id, client_id):
	main_menu = 'clients'
	sub_menu = 'inactive_clients'
	
	client_courses = Client_Courses.objects.get(course_id=course_id)
	client = Clients.objects.get(client_id=client_id)
	formset = ClientCoursesForm(instance=client_courses)
	
	if request.method == 'POST':
		educational_istitution = request.POST['educational_istitution']
		title = request.POST['title']
		date = request.POST['date']
		description = request.POST['description']
		pdf_file = request.POST['pdf_file']
		total_hours = request.POST['total_hours']
		formset = Client_Courses(course_id=course_id, educational_istitution=educational_istitution, 
			title=title, date=date, description=description, pdf_file=pdf_file, 
			total_hours=total_hours, client_id=client_id)
		if formset:
			formset.save()
			return redirect('client_profile', client_id)

	context = {'title':'Update Course', 'formset':formset, 'course_id':course_id, 'client_id':client_id,
	           'main_menu':main_menu, 'sub_menu':sub_menu}

	return render(request, 'employer/en/profile/client_course_update.html', context)
#-----------------------------------------------------

#------------ Delete Client's Course ----------------
@login_required(login_url='login')
@admin_only
def client_course_delete(request, client_id, course_id):
	main_menu = 'clients'
	sub_menu = 'inactive_clients'
	
	selected_client_courses = Client_Courses.objects.get(course_id=course_id)
	
	if request.method == 'POST':
		selected_client_courses.delete()
		return redirect('/client/{}/profile/'.format(client_id))

	context = {'title':'Delete {}'.format(selected_client_courses.title), 'item':selected_client_courses,
			   'client_id':client_id, 'main_menu':main_menu, 'sub_menu':sub_menu}

	return render(request, 'employer/en/profile/client_course_delete.html', context)
#-----------------------------------------------------
#=====================================================
#=====================================================
#=====================================================


#=====================================================
#================== Client Skills ====================
#=====================================================
#-------------- Show Client's Skill ----------------
@login_required(login_url='login')
@admin_only
def client_skill(request, skill_id):
	main_menu = 'clients'
	sub_menu = 'inactive_clients'
	
	selected_skill = Client_Skills.objects.get(skill_id=skill_id)
	
	context = {'title':'{} at {}'.format(selected_skill.title, selected_skill.educational_istitution),
			   'selected_skill':selected_skill, 'main_menu':main_menu, 'sub_menu':sub_menu}
	
	return render(request, 'employer/en/profile/client_skill.html', context)
#-----------------------------------------------------

#------------ Create Client's Skill ----------------
@login_required(login_url='login')
@admin_only
def client_skill_create(request, client_id):
	main_menu = 'clients'
	sub_menu = 'inactive_clients'
	
	client = Clients.objects.get(client_id=client_id)
	formset = ClientSkillsForm()
	
	if request.method == 'POST':
		title = request.POST['title']
		progress = request.POST['progress']
		formset = Client_Skills(title=title, progress=progress, client=client)
		if formset:
			formset.save()
			return redirect('client_profile', client_id)

	context = {'title':'Create course', 'formset':formset, 'client_id':client_id,
			   'main_menu':main_menu, 'sub_menu':sub_menu}

	return render(request, 'employer/en/profile/client_skill_create.html', context)
#-----------------------------------------------------

#------------ Update Client's Skill ----------------
@login_required(login_url='login')
@admin_only
def client_skill_update(request, client_id, skill_id):
	main_menu = 'clients'
	sub_menu = 'inactive_clients'
	
	client_skill = Client_Skills.objects.get(skill_id=skill_id)
	client = Clients.objects.get(client_id=client_id)
	formset = ClientSkillsForm(instance=client_skill)
	
	if request.method == 'POST':
		title = request.POST['title']
		progress = request.POST['progress']
		formset = Client_Skills(title=title, progress=progress, client=client, skill_id=client_skill.skill_id)
		if formset:
			formset.save()
			return redirect('client_profile', client_id)

	context = {'title':'Update Course', 'formset':formset, 'skill_id':skill_id, 'client_id':client_id,
			   'main_menu':main_menu, 'sub_menu':sub_menu}

	return render(request, 'employer/en/profile/client_skill_update.html', context)
#-----------------------------------------------------

#------------ Delete Client's Skill ----------------
@login_required(login_url='login')
@admin_only
def client_skill_delete(request, client_id, skill_id):
	main_menu = 'clients'
	sub_menu = 'inactive_clients'
	
	selected_client_skills = Client_Skills.objects.get(skill_id=skill_id)
	
	if request.method == 'POST':
		selected_client_skills.delete()
		return redirect('/client/{}/profile/'.format(client_id))

	context = {'title':'Delete {}'.format(selected_client_skills.title), 'item':selected_client_skills,
			   'client_id':client_id, 'main_menu':main_menu, 'sub_menu':sub_menu}

	return render(request, 'employer/en/profile/client_skill_delete.html', context)
#-----------------------------------------------------
#=====================================================
#=====================================================
#=====================================================