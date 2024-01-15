
from django.shortcuts import render, redirect
from .models import *
from .forms import *
from .decorators import admin_only
from django.contrib.auth.decorators import login_required


#=====================================================
#==================== partners =======================
#=====================================================
#------------------ Show partners --------------------
@login_required(login_url='login')
@admin_only
def partners(request):
	main_menu = 'partners'
	sub_menu = 'all_partners'
	
	all_partners = Partners.objects.order_by('english_name').all()
	
	context = {'title':'Our partners','all_partners':all_partners,
				'main_menu':main_menu, 'sub_menu':sub_menu}
	
	return render(request, 'employer/en/partners/Partners.html', context)
#-----------------------------------------------------

#----------------- Update partner --------------------
@login_required(login_url='login')
@admin_only
def partner_update(request, partner_id):
	main_menu = 'partners'
	sub_menu = 'all_partners'
	
	selected_partner = Partners.objects.get(partner_id=partner_id)
	formset = PartnersForm(instance=selected_partner)
	
	if request.method == 'POST':
		english_name = request.POST['english_name']
		arabic_name = request.POST['arabic_name']
		category = request.POST['category']
		logo = request.FILES['logo']
		if selected_partner.logo:
			selected_partner.logo.delete()
		formset = partners(partner_id=partner_id, english_name=english_name, arabic_name=arabic_name,
							category=category, logo=logo)
		if formset:
			formset.save()
			return redirect('/partners/')
	
	context = {'title': selected_partner.english_name + " - Edit", 'selected_partner':selected_partner,
				'formset':formset, 'main_menu':main_menu, 'sub_menu':sub_menu}
	
	return render(request, 'employer/en/partners/partner_update.html', context)
#----------------------------------------------------

#----------------- Delete partner -------------------
@login_required(login_url='login')
@admin_only
def partner_delete(request, partner_id):
	main_menu = 'partners'
	sub_menu = 'all_partners'
	
	selected_partner = Partners.objects.get(partner_id=partner_id)
	
	if request.method == 'POST':
		if selected_partner.logo:
			selected_partner.logo.delete()
		selected_partner.delete()
		return redirect('/partners/')
	
	context = {'title': selected_partner.english_name + " - Delete", 'item':selected_partner,
				'main_menu':main_menu, 'sub_menu':sub_menu}
	
	return render(request, 'employer/en/partners/partner_delete.html', context)
#----------------------------------------------------

#----------------- Create partner -------------------
@login_required(login_url='login')
@admin_only
def partner_create(request):
	main_menu = 'partners'
	sub_menu = 'add_partner'
	
	formset = PartnersForm()
	
	if request.method == 'POST':
		english_name = request.POST['english_name']
		arabic_name = request.POST['arabic_name']
		category = request.POST['category']
		logo = request.FILES['logo']
		formset = partners(english_name=english_name, arabic_name=arabic_name,
							category=category, logo=logo)
		if formset:
			formset.save()
			return redirect('/partners/')
	
	context = {'title':'Add partner', 'formset':formset,
				'main_menu':main_menu, 'sub_menu':sub_menu}
	
	return render(request, 'employer/en/partners/partner_create.html', context)
#-----------------------------------------------------
#=====================================================
#=====================================================
#=====================================================