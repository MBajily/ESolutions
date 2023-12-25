from django.shortcuts import render, redirect
from .models import *
from .forms import *
from .decorators import admin_only
from django.contrib.auth.decorators import login_required


#=====================================================
#================= Specializations ===================
#=====================================================
#-------------- Show Specializations -----------------
@login_required(login_url='login')
@admin_only
def specializations(request):
	main_menu = 'specialties'
	sub_menu = 'all_specialties'
	
	all_specializations = Specializations.objects.order_by('english_name').all()

	context={ 'title':'Specializations','all_specializations':all_specializations,
				'main_menu':main_menu, 'sub_menu':sub_menu}

	return render(request, 'employer/en/specializations/specializations.html', context)
#-----------------------------------------------------

#------------- Update specialization -----------------
@login_required(login_url='login')
@admin_only
def specialization_update(request, specialization_id):
	main_menu = 'specialties'
	sub_menu = 'all_specialties'
	
	selected_specialization = Specializations.objects.get(specialization_id=specialization_id)
	formset = SpecializationsForm(instance=selected_specialization)
	if request.method == 'POST':
		formset = SpecializationsForm(request.POST, instance=selected_specialization)
		if formset.is_valid():
			formset.save()
			return redirect('/specializations/')

	context = {'title': selected_specialization.english_name, 'selected_specialization':selected_specialization,
				'formset':formset, 'main_menu':main_menu, 'sub_menu':sub_menu}

	return render(request, 'employer/en/specializations/specialization_update.html', context)
#----------------------------------------------------

#------------- Delete specialization ----------------
@login_required(login_url='login')
@admin_only
def specialization_delete(request, specialization_id):
	main_menu = 'specialties'
	sub_menu = 'all_specialties'
	
	selected_specialization = Specializations.objects.get(specialization_id=specialization_id)
	if request.method == 'POST':
		selected_specialization.delete()
		return redirect('/specializations/')

	context = {'title':'Delete specialization', 'item':selected_specialization,
				'main_menu':main_menu, 'sub_menu':sub_menu}

	return render(request, 'employer/en/specializations/specialization_delete.html', context)
#----------------------------------------------------

#------------- Create specialization ----------------
@login_required(login_url='login')
@admin_only
def specialization_create(request):
	main_menu = 'specialties'
	sub_menu = 'add_specialty'
	
	formset = SpecializationsForm()
	if request.method == 'POST':
		english_name = request.POST['english_name']
		arabic_name = request.POST['arabic_name']
		formset = Specializations(english_name=english_name, arabic_name=arabic_name)
		if formset:
			formset.save()
			return redirect('/specializations/')

	context = {'title':'Create specialization', 'formset':formset,
				'main_menu':main_menu, 'sub_menu':sub_menu}
				
	return render(request, 'employer/en/specializations/specialization_create.html', context)
#-----------------------------------------------------
#=====================================================
#=====================================================
#=====================================================