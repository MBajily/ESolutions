from django.shortcuts import render, redirect
from .forms import AdminsForm
from .models import *
from .client_forms import *
from .client_models import *
from .decorators import admin_only, superadmin_only
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, JsonResponse


#=====================================================
#=================== Dashboard =======================
#=====================================================
#------------------- Dashboard -----------------------
@login_required(login_url='login')
@admin_only
def dashboard(request):
	main_menu = 'dashboard'
	sub_menu = ''

	sent_mails = Sent_Mail.objects.filter(is_trash=0).order_by('-date_sent')[:5]
	clients_applied = Job_Applied.objects.order_by('-date')[:5]
	clients_applied_count = Job_Applied.objects.all().count()
	jobs_count = Jobs.objects.filter(is_available='1').count()
	active_clients_count = User.objects.filter(groups=2).count()
	inactive_clients_count = Clients.objects.all().count()


	context = {'title':'Dashboard', 'clients_applied':clients_applied, 
	'clients_applied_count':clients_applied_count, 'main_menu':main_menu, 
	'sub_menu':sub_menu, 'sent_mails':sent_mails, 'jobs_count':jobs_count,
	'active_clients_count':active_clients_count, 'inactive_clients_count':inactive_clients_count}
	
	return render(request, 'employer/en/dashboard/dashboard.html', context)
#-----------------------------------------------------
#=====================================================
#=====================================================
#=====================================================


#=====================================================
#==================== Charts =========================
#=====================================================
#-------------- Jobs' Applies Chart ------------------
@login_required(login_url='login')
@admin_only
def jobs_applies_chart(request):
	data = []

	for d in (datetime.date.today() - datetime.timedelta(days=x) for x in reversed(range(0,30))):
		job_applied_count = Job_Applied.objects.filter(date=d.strftime("%Y-%m-%d")).count()
		if job_applied_count:
			data.append({'{}'.format(d.strftime("%b, %d")): job_applied_count})
		else:
			data.append({'{}'.format(d.strftime("%b, %d")): 0})
	
	return JsonResponse(data, safe=False)
#-----------------------------------------------------

#-------------- Jobs' Applies Chart ------------------
@login_required(login_url='login')
@admin_only
def new_users_chart(request):
	data = []

	for d in (datetime.date.today() - datetime.timedelta(days=x) for x in reversed(range(0,30))):
		new_users_count = User.objects.filter(date_joined__lte=d.strftime("%Y-%m-%d"), date_joined__gt=d-datetime.timedelta(days=1)).count()
		if new_users_count:
			data.append({'{}'.format(d.strftime("%b, %d")): new_users_count})
		else:
			data.append({'{}'.format(d.strftime("%b, %d")): 0})
	# print(data)
	return JsonResponse(data, safe=False)
#-----------------------------------------------------


#-------------- Nationalities Chart ------------------
@login_required(login_url='login')
@admin_only
def nationalities_chart(request):
	data_to_sort = {}

	for nationality in Nationalities.objects.all():
		nationalities_count = Client_CV.objects.filter(nationality=nationality).all().count()
		if nationalities_count:
			data_to_sort['{}'.format(nationality.english_name)] = nationalities_count
		else:
			data_to_sort['{}'.format(nationality.english_name)] = 0
	data_to_sort = sorted(data_to_sort.items(), key=lambda x: x[1], reverse=True)

	data = []
	for key, value in data_to_sort:
		data.append({key: value})

	return JsonResponse(data[:5], safe=False)
#-----------------------------------------------------


#-------------- Jobs' Applies Chart ------------------
@login_required(login_url='login')
@admin_only
def resumes_chart(request):
	data = []

	for d in (datetime.date.today() - datetime.timedelta(days=x) for x in reversed(range(0,30))):
		resumes_count = Clients.objects.filter(create_date__lte=d.strftime("%Y-%m-%d"), create_date__gt=d-datetime.timedelta(days=1)).count()
		if resumes_count:
			data.append({'{}'.format(d.strftime("%b, %d")): resumes_count})
		else:
			data.append({'{}'.format(d.strftime("%b, %d")): 0})
	# print(data)
	return JsonResponse(data, safe=False)
#-----------------------------------------------------


# #-------------- Jobs' Applies Chart ------------------
# @login_required(login_url='login')
# @admin_only
# def active_clients_chart(request):
# 	# items = User.objects.filter(date_joined__lte=datetime.datetime.today(), date_joined__gt=datetime.datetime.today()-datetime.timedelta(days=30)).all()

# 	data = []
# 	for d in (datetime.date.today() - datetime.timedelta(days=x) for x in reversed(range(0,10))):
# 		active_clients_count = User.objects.filter(date_joined__lte=d.strftime("%Y-%m-%d")).count()
# 		if active_clients_count:
# 			data.append({'{}'.format(d.strftime("%b, %d")): active_clients_count})
# 		else:
# 			data.append({'{}'.format(d.strftime("%b, %d")): 0})
# 	# print(data)
# 	return JsonResponse(data, safe=False)
# #-----------------------------------------------------

# #-------------- Jobs' Applies Chart ------------------
# @login_required(login_url='login')
# @admin_only
# def all_jobs_applies_chart(request):
# 	data = []

# 	for d in (datetime.date.today() - datetime.timedelta(days=x) for x in reversed(range(0,10))):
# 		job_applied_count = Job_Applied.objects.filter(date__lte=d + datetime.timedelta(days=1)).count()
# 		if job_applied_count:
# 			data.append({'{}'.format(d.strftime("%b, %d")): job_applied_count})
# 		else:
# 			data.append({'{}'.format(d.strftime("%b, %d")): 0})
	
# 	return JsonResponse(data, safe=False)
# #-----------------------------------------------------


# #-------------- Jobs' Applies Chart ------------------
# @login_required(login_url='login')
# @admin_only
# def available_jobs_chart(request):
# 	data = []

# 	for d in (datetime.date.today() - datetime.timedelta(days=x) for x in reversed(range(0,10))):
# 		jobs_count = Jobs.objects.filter(start_date__lte=d + datetime.timedelta(days=1)).count()
# 		if jobs_count:
# 			data.append({'{}'.format(d.strftime("%b, %d")): jobs_count})
# 		else:
# 			data.append({'{}'.format(d.strftime("%b, %d")): 0})
	
# 	return JsonResponse(data, safe=False)
# #-----------------------------------------------------


# #-------------- Jobs' Applies Chart ------------------
# @login_required(login_url='login')
# @admin_only
# def inactive_clients_chart(request):
# 	data = []

# 	for d in (datetime.date.today() - datetime.timedelta(days=x) for x in reversed(range(0,10))):
# 		inactive_clients_count = Clients.objects.filter(create_date__lte=d + datetime.timedelta(days=1)).count()
# 		if inactive_clients_count:
# 			data.append({'{}'.format(d.strftime("%b, %d")): inactive_clients_count})
# 		else:
# 			data.append({'{}'.format(d.strftime("%b, %d")): 0})
	
# 	return JsonResponse(data, safe=False)
# #-----------------------------------------------------
#=====================================================
#=====================================================
#=====================================================