from django.shortcuts import render, redirect
from .forms import AdminsForm
from .models import *
from .client_forms import *
from .client_models import *
from .decorators import admin_only, admin_permission
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from django.db.models import Q
import bcrypt
from django.contrib.auth.hashers import PBKDF2PasswordHasher



#=====================================================
#================== Admin Profile ====================
#=====================================================
#-------------- Update Admin Profile -----------------
@login_required(login_url='login')
def admin_information_update(request):
	main_menu = 'settings'
	sub_menu = 'admin_information_update'
	
	user_logged_in = request.user

	formset = AdminsForm(instance=user_logged_in)
	if request.method == 'POST':
		if request.user.check_password(request.POST["admin_password"]):
			admin_information = user_logged_in
			admin_information.first_name = request.POST['first_name']
			admin_information.last_name = request.POST['last_name']
			admin_information.email = request.POST['email']
			admin_information.username = request.POST['username']
			if formset:
				admin_information.save(update_fields=["first_name","last_name","email","username"])
				return redirect('dashboard')
		else:
			return redirect('admin_information_update')


	context = {'title': 'Update Your Information', 'formset':formset, 
				'main_menu':main_menu, 'sub_menu':sub_menu}

	return render(request, 'employer/en/admins/admin_information_update.html', context)
#-----------------------------------------------------


#-------------- Update Admin Profile -----------------
@login_required(login_url='login')
def admin_password_update(request):
	main_menu = 'settings'
	sub_menu = 'admin_password_update'
	
	user_logged_in = request.user

	if request.method == 'POST':
		if request.user.check_password(request.POST["admin_password"]):
			if request.POST['new_password'] == request.POST['confirm_new_password']:
				admin_information = user_logged_in
				admin_information.password = PBKDF2PasswordHasher().encode(request.POST['new_password'], 'pbkdf2_sha256')
				if admin_information:
					admin_information.save(update_fields=["password"])
					return redirect('dashboard')
		else:
			return redirect('admin_password_update')


	context = {'title': 'Update Your Information', 
				'main_menu':main_menu, 'sub_menu':sub_menu}

	return render(request, 'employer/en/admins/admin_password_update.html', context)
#-----------------------------------------------------
#=====================================================
#=====================================================
#=====================================================


#=====================================================
#===================== Admin =========================
#=====================================================
#-------------------- Admins -------------------------
@login_required(login_url='login')
@admin_permission('admin_read')
def admins(request):
	main_menu = 'admins'
	sub_menu = 'all_admins'
	
	admins_group = Group.objects.filter(~Q(name='Client')).all()
	# admins_group = Group.objects.all()
	admins = []
	for group in admins_group:
		for user in group.user_set.all():
	  		admins.append(user.id)

	all_admins = User.objects.filter(groups__in=admins_group).all()
	all_admins = set(all_admins)

	context = {'title':'Active Clients', 'all_admins':all_admins, 
			   'main_menu':main_menu, 'sub_menu':sub_menu}

	return render(request, 'employer/en/admins/admins.html', context)
#-----------------------------------------------------

#-------------------- Admins -------------------------
@login_required(login_url='login')
@admin_permission('admin_write')
def add_admin(request):
	main_menu = 'admins'
	sub_menu = 'add_admin'
	groups = Group.objects.order_by('name').all()
	if request.method == 'POST':
		if request.user.check_password(request.POST["admin_password"]):
			form = RegisterForm(request.POST)
			if form.is_valid():
				form.save()
				client = User.objects.get(username=request.POST["username"])
				for group in request.POST.getlist("group"):
					client.groups.add(Group.objects.get(name=group))
				return redirect('admins')
		else:
			return redirect('add_admin')
	else:
		form = RegisterForm()

	context = {'title':'New Admin', 'form':form, 'groups':groups, 
			   'main_menu':main_menu, 'sub_menu':sub_menu}

	return render(request, 'employer/en/admins/admin_register.html', context)
#-----------------------------------------------------

#------------------- Delete Client -------------------
@login_required(login_url='login')
@admin_permission('admin_write')
def admin_delete(request, admin_id):
	main_menu = 'admins'
	sub_menu = 'all_admins'

	selected_admin = User.objects.get(id=admin_id)
	
	if request.method == 'POST':
		if request.user.check_password(request.POST["admin_password"]):
			selected_admin.delete()
			return redirect('admins')
		else:
			return redirect('admin_delete', admin_id)

	context = {'title':'Delete Admin', 'item':selected_admin,
			   'main_menu':main_menu, 'sub_menu':sub_menu}

	return render(request, 'employer/en/admins/admin_delete.html', context)
#-----------------------------------------------------

#------------------- Update Client -------------------
@login_required(login_url='login')
@admin_permission('admin_write')
def admin_update(request, admin_id):
	main_menu = 'admins'
	sub_menu = 'all_admins'
	
	groups = Group.objects.all()
	selected_admin = User.objects.get(id=admin_id)
	formset = AdminsForm(instance=selected_admin)
	if request.method == 'POST':
		if request.user.check_password(request.POST["admin_password"]):
			first_name = request.POST['first_name']
			last_name = request.POST['last_name']
			email = request.POST['email']
			username = request.POST['username']
			
			selected_admin = User(first_name=first_name,last_name=last_name,
								id=selected_admin.id, password=selected_admin.password,
								last_login=selected_admin.last_login, is_superuser=selected_admin.is_superuser,
								username=username, email=email,
								is_staff=selected_admin.is_staff, is_active=selected_admin.is_active,
								date_joined=selected_admin.date_joined)
			if selected_admin:
				selected_admin.save()
				for group in selected_admin.groups.all():
					selected_admin.groups.remove(group)
				for group in request.POST.getlist("group"):
					selected_admin.groups.add(Group.objects.get(name=group))
				return redirect('admins')
		else:
			return redirect('admin_update', selected_admin.id)

	context = {'title': selected_admin.first_name, 'sub_menu':sub_menu,
				'formset':formset, 'main_menu':main_menu, 'groups':groups,
				'selected_admin':selected_admin}

	return render(request, 'employer/en/admins/admin_update.html', context)
#-----------------------------------------------------

#--------------------- Roles -------------------------
@login_required(login_url='login')
@admin_permission('admin_read')
def all_roles(request):
	main_menu = 'admins'
	sub_menu = 'all_roles'
	
	all_roles = Group.objects.all()

	context = {'title':'Active Clients', 'all_roles':all_roles, 
			   'main_menu':main_menu, 'sub_menu':sub_menu}

	return render(request, 'employer/en/admins/roles.html', context)
#-----------------------------------------------------

#--------------------- Roles -------------------------
@login_required(login_url='login')
@admin_permission('admin_write')
def role_create(request):
	main_menu = 'admins'
	sub_menu = 'add_role'
	all_permissions = ES_Permission.objects.all()
	if request.method == 'POST':
		if request.user.check_password(request.POST["admin_password"]):
			group = Group(name=request.POST["role_name"])
			if group:
				group.save()

				for permission in request.POST.getlist("permission"):
					add_permission = Admin_Permission(group=group, permission=ES_Permission.objects.get(permission_id=permission))
					if add_permission:
						add_permission.save()
				return redirect('all_roles')
		else:
			return redirect('add_role')

	context = {'title':'New Role', 'main_menu':main_menu, 'sub_menu':sub_menu,
				'all_permissions':all_permissions}

	return render(request, 'employer/en/admins/role_create.html', context)
#-----------------------------------------------------

#--------------------- Roles -------------------------
@login_required(login_url='login')
@admin_permission('admin_write')
def role_update(request, role_id):
	main_menu = 'admins'
	sub_menu = 'all_roles'
	all_permissions = ES_Permission.objects.all()
	selected_group = Group.objects.get(id=role_id)
	admin_permissions = Admin_Permission.objects.filter(group=selected_group).all()
	if request.method == 'POST':
		if request.user.check_password(request.POST["admin_password"]):
			group = Group(id=role_id, name=request.POST["role_name"])
			if group:
				group.save()
				for permission in Admin_Permission.objects.filter(group=selected_group).all():
					permission.delete()

				for permission in request.POST.getlist("permission"):
					add_permission = Admin_Permission(group=group, permission=ES_Permission.objects.get(permission_id=permission))
					if add_permission:
						add_permission.save()
				return redirect('all_roles')
		else:
			return redirect('add_role')

	context = {'title':'Update Role', 'main_menu':main_menu, 'sub_menu':sub_menu,
				'all_permissions':all_permissions, 'admin_permissions':admin_permissions,
				'selected_group':selected_group}

	return render(request, 'employer/en/admins/role_update.html', context)
#-----------------------------------------------------

#------------------- Delete Client -------------------
@login_required(login_url='login')
@admin_permission('admin_write')
def role_delete(request, role_id):
	main_menu = 'admins'
	sub_menu = 'all_roles'

	selected_role = Group.objects.get(id=role_id)
	
	if request.method == 'POST':
		if request.user.check_password(request.POST["admin_password"]):
			selected_role.delete()
			return redirect('all_roles')
		else:
			return redirect('role_delete', role_id)

	context = {'title':'Delete Role', 'item':selected_role,
			   'main_menu':main_menu, 'sub_menu':sub_menu}

	return render(request, 'employer/en/admins/role_delete.html', context)
#-----------------------------------------------------
#=====================================================
#=====================================================
#=====================================================