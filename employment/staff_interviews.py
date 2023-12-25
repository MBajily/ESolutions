from django.shortcuts import render, redirect
from .models import *
from .forms import *
from .filters import *
from .decorators import admin_only
from django.contrib.auth.decorators import login_required
import datetime

#=====================================================
#================= Phone Interviews ==================
#=====================================================
#------------------ Submitted Jobs -------------------
@login_required(login_url='login')
@admin_only
def submitted_jobs(request):
	main_menu = 'phone_interviews'
	sub_menu = 'submitted_jobs'
	
	all_jobs = Jobs.objects.all().order_by('-start_date')
	all_jobs_count = all_jobs.count()
	all_jobs_filter = JobsFilter(request.GET, queryset=all_jobs)
	all_jobs = all_jobs_filter.qs
	results_number = all_jobs.count()

	context = {'title':'Submitted Jobs', 'Job_Applied':Job_Applied,
			   'all_jobs':all_jobs, 'all_jobs_count':all_jobs_count,
			   'all_jobs_filter':all_jobs_filter,
			   'results_number':results_number,
			   'main_menu':main_menu, 'sub_menu':sub_menu}

	return render(request, 'employer/en/interviews/submitted_jobs.html', context)
#-----------------------------------------------------

#------------------ Create Client --------------------
@login_required(login_url='login')
@admin_only
def add_phone_interview(request):
	main_menu = 'phone_interviews'
	sub_menu = 'do_interview'

	if request.method == 'POST':
		return redirect('phone_interview', request.POST['client_id'])

	context = {'title':'Phone Interview',
				'main_menu':main_menu, 'sub_menu':sub_menu}

	return render(request, 'employer/en/interviews/add_phone_interview.html', context)
#-----------------------------------------------------

#------------------ Create Client --------------------
@login_required(login_url='login')
@admin_only
def phone_interview(request, client_id):
	main_menu = 'phone_interviews'
	sub_menu = 'do_interview'
	
	selected_client = User.objects.get(id=client_id)
	ended_interview = Phone_Interviews.objects.get(client=selected_client)
	
	if ended_interview is not None:
		formset = PhoneInterviewsForm(instance=ended_interview)
	else:
		formset = PhoneInterviewsForm()
	
	if request.method == 'POST':
		how_heared_about_job = request.POST['how_heared_about_job']
		hear_speak_problem = request.POST['hear_speak_problem']
		has_health_condition = request.POST['has_health_condition']
		want_to_work = request.POST['want_to_work']
		live_in_riyadh = request.POST['live_in_riyadh']
		have_transportation = request.POST['have_transportation']
		call_behavior = request.POST['call_behavior']
		future_goal = request.POST['future_goal']
		why_this_job = request.POST['why_this_job']
		saudi_driving_license = request.POST['saudi_driving_license']
		note = request.POST['note']
		result = request.POST['result']
		suited_job = Jobs.objects.get(job_id=request.POST['suited_job'])
		position = Specializations.objects.get(specialization_id=request.POST['position'])
		if ended_interview is not None:
			formset = Phone_Interviews(interview_id=ended_interview.interview_id, how_heared_about_job=how_heared_about_job, hear_speak_problem=hear_speak_problem, has_health_condition=has_health_condition, 
				want_to_work=want_to_work, live_in_riyadh=live_in_riyadh, have_transportation=have_transportation, call_behavior=call_behavior, 
				future_goal=future_goal, why_this_job=why_this_job, saudi_driving_license=saudi_driving_license,
				note=note, client=selected_client, result=result, suited_job=suited_job, position=position, 
				interview_date=ended_interview.interview_date, latest_update=datetime.datetime.now())
		else:
			formset = Phone_Interviews(how_heared_about_job=how_heared_about_job, hear_speak_problem=hear_speak_problem, has_health_condition=has_health_condition, 
				want_to_work=want_to_work, live_in_riyadh=live_in_riyadh, have_transportation=have_transportation, call_behavior=call_behavior, 
				future_goal=future_goal, why_this_job=why_this_job, saudi_driving_license=saudi_driving_license,
				note=note, client=selected_client, result=result, suited_job=suited_job, position=position)
		if formset:
			formset.save()
			return redirect('ended_interviews')

	context = {'title':'Phone Interview', 'formset':formset,
				'main_menu':main_menu, 'sub_menu':sub_menu,
				'selected_client':selected_client}

	if ended_interview is not None:
		context['latest_update']=ended_interview.latest_update 

	return render(request, 'employer/en/interviews/phone_interview.html', context)
#-----------------------------------------------------

#----------------- Ended Interviews ------------------
@login_required(login_url='login')
@admin_only
def ended_interviews(request):
	main_menu = 'phone_interviews'
	sub_menu = 'ended_interviews'
	
	all_ended_interviews = Phone_Interviews.objects.all().order_by("-interview_date")
	all_ended_interviews_count = all_ended_interviews.count()
	all_ended_interviews_filter = EndedInterviewsFilter(request.GET, queryset=all_ended_interviews)
	all_ended_interviews = all_ended_interviews_filter.qs

	context = {'title':'Active Clients', 'all_ended_interviews':all_ended_interviews, 
			   'all_ended_interviews_count':all_ended_interviews_count, 
			   'all_ended_interviews_filter':all_ended_interviews_filter,
			   'main_menu':main_menu, 'sub_menu':sub_menu}
			   
	return render(request, 'employer/en/interviews/ended_interviews.html', context)
#------------------------------------------------------
#=====================================================
#=====================================================
#=====================================================