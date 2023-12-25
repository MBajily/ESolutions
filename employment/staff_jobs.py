from django.shortcuts import render, redirect
from .models import *
from .forms import *
from .filters import *
from .decorators import admin_only
from django.contrib.auth.decorators import login_required



#=====================================================
#====================== Jobs =========================
#=====================================================
#-------------------- Show Jobs ----------------------
@login_required(login_url='login')
@admin_only
def jobs(request):
	main_menu = 'jobs'
	sub_menu = 'all_jobs'
	
	all_jobs = Jobs.objects.filter(is_available='1').order_by('-start_date')
	all_jobs_count = all_jobs.count()
	all_jobs_filter = JobsFilter(request.GET, queryset=all_jobs)
	all_jobs = all_jobs_filter.qs
	results_number = all_jobs.count()

	context = {'title':'Jobs', 'all_jobs':all_jobs, 'all_jobs_count':all_jobs_count,
			   'all_jobs_filter':all_jobs_filter, 'results_number':results_number,
				'main_menu':main_menu, 'sub_menu':sub_menu}

	return render(request, 'employer/en/jobs/jobs.html', context)
#-------------------------------------------------------

#---------------------- Update Job ---------------------
@login_required(login_url='login')
@admin_only
def job_update(request, job_id):
	main_menu = 'jobs'
	sub_menu = 'all_jobs'
	
	selected_job = Jobs.objects.get(job_id=job_id)
	formset = JobsForm(instance=selected_job)
	
	if request.method == 'POST':
		formset = JobsForm(request.POST, instance=selected_job)
		if formset.is_valid():
			formset.save()
			return redirect('jobs')

	context = {'title': selected_job.title, 'selected_job':selected_job,
				'formset':formset,
				'main_menu':main_menu, 'sub_menu':sub_menu}

	return render(request, 'employer/en/jobs/job_update.html', context)
#-------------------------------------------------------

#--------------------- Delete Job ----------------------
@login_required(login_url='login')
@admin_only
def job_delete(request, job_id):
	main_menu = 'jobs'
	sub_menu = 'all_jobs'
	
	selected_job = Jobs.objects.get(job_id=job_id)
	
	if request.method == 'POST':
		formset = selected_job
		formset.is_available = '0'
		if formset:
			formset.save(update_fields=["is_available"])
			return redirect('jobs')

	context = {'title':'Delete job', 'item':selected_job,
				'main_menu':main_menu, 'sub_menu':sub_menu}

	return render(request, 'employer/en/jobs/job_delete.html', context)
#-------------------------------------------------------

#-------------------- Create Job -----------------------
@login_required(login_url='login')
@admin_only
def job_create(request):
	main_menu = 'jobs'
	sub_menu = 'add_job'
	
	formset = JobsForm()
	
	if request.method == 'POST':
		title = request.POST['title']
		description = request.POST['description']
		company = Partners.objects.get(partner_id=request.POST['company'])
		salary = request.POST['salary']
		end_date = request.POST['end_date']
		city = Cities.objects.get(city_id=request.POST['city'])
		specialization = Specializations.objects.get(specialization_id=request.POST['specialization'])
		nationality = Nationalities.objects.get(nationality_id=request.POST['nationality'])
		formset = Jobs(title=title, description=description, company=company, 
			salary=salary, end_date=end_date, nationality=nationality, 
			specialization=specialization, city=city)
		if formset:
			formset.save()
			all_cvs = Client_CV.objects.filter(specialization=specialization, nationality=nationality)
			for selected_client in all_cvs:
				message = """
				<p>There is a job added recently, it may be suitable for you, read the details.</p>
				"""
				notification = Notification(receiver=selected_client.client, title='New Job for You',
											message=message, job=formset)
				if notification:
					notification.save()

			return redirect('jobs')

	context = {'title':'Create Job', 'formset':formset,
				'main_menu':main_menu, 'sub_menu':sub_menu}

	return render(request, 'employer/en/jobs/job_create.html', context)
#-----------------------------------------------------

#-------------------- Job Details ----------------------
@login_required(login_url='login')
@admin_only
def job_details(request, job_id):
	main_menu = 'jobs'
	sub_menu = 'all_jobs'
	
	selected_job = Jobs.objects.get(job_id=job_id)
	clients_applied = Job_Applied.objects.filter(job_id=job_id).count()
	date_now = datetime.datetime.now().date()

	context = {'title':'{} - {}'.format(selected_job.company.english_name, selected_job.title), 'date_now':date_now,
			   'selected_job':selected_job, 'clients_applied':clients_applied,
				'main_menu':main_menu, 'sub_menu':sub_menu}

	return render(request, 'employer/en/jobs/job_details.html', context)
#-------------------------------------------------------

#-----------------  Clients Applied --------------------
@login_required(login_url='login')
@admin_only
def clients_applied(request):
	main_menu = 'jobs'
	sub_menu = 'applied_clients'
	
	all_clients_applied = Job_Applied.objects.all().order_by('-date')
	results_number = all_clients_applied.count()

	context = {'title':'Applied Clients', 'all_clients_applied':all_clients_applied,
			   'results_number':results_number,
				'main_menu':main_menu, 'sub_menu':sub_menu}

	return render(request, 'employer/en/jobs/job_clients_applied.html', context)
#-------------------------------------------------------

#-------------  Clients Applied in Job -----------------
@login_required(login_url='login')
@admin_only
def clients_job_applied(request, job_id):
	main_menu = 'jobs'
	sub_menu = 'applied_clients'
	
	all_clients_applied = Job_Applied.objects.filter(job_id=job_id).order_by('-date')
	clients_filter = ClientsFilter(request.GET, queryset=all_clients_applied)
	all_clients_applied = clients_filter.qs
	results_number = all_clients_applied.count()

	context = {'title':'{}'.format(Jobs.objects.get(job_id=job_id).title),
			   'all_clients_applied':all_clients_applied, 'clients_filter':clients_filter,
			   'results_number':results_number, 'Clients':Clients, 'Jobs':Jobs,
			   'main_menu':main_menu, 'sub_menu':sub_menu}

	return render(request, 'employer/en/jobs/job_clients_applied.html', context)


#---------------- Applied Job Details ------------------
@login_required(login_url='login')
@admin_only
def applied_job_details(request, apply_id):
	main_menu = 'jobs'
	sub_menu = 'applied_clients'
	
	applied_job = Job_Applied.objects.get(apply_id=apply_id)

	context = {'title':'{} - {}'.format(applied_job.job.company.english_name, applied_job.job.title), 
			   'applied_job':applied_job, 'main_menu':main_menu, 'sub_menu':sub_menu}

	return render(request, 'employer/en/jobs/applied_job_details.html', context)
#-----------------------------------------------------
#=====================================================
#=====================================================
#=====================================================