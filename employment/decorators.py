from django.http import HttpResponse
from django.shortcuts import redirect
from .models import Admin_Permission, ES_Permission

def unauthenticated_user(view_func):
	def wrapper_func(request, *args, **kwargs):
		if request.user.is_authenticated:
			return redirect('c_client_profile')
		else:
			return view_func(request, *args, **kwargs)

	return wrapper_func


def allowed_users(allowed_roles=[]):
	def decorator(view_func):
		def wrapper_func(request, *args, **kwargs):

			group = None
			if request.user.groups.exists():
				group = request.user.groups.all()[0].name

			if group in allowed_roles:
				return view_func(request,*args, **kwargs)
			else:
				return HttpResponse("You are not authenticated to view this page!")

		return wrapper_func
	return decorator


def admin_permission(allowed_page):
	def decorator(view_func):
		def wrapper_func(request, *args, **kwargs):

			group = None
			if request.user.groups.exists():
				group = request.user.groups.all()
			
			selected_permission = ES_Permission.objects.get(codename=allowed_page).permission_id
			admin_permissions = Admin_Permission.objects.filter(group__in=group).filter(permission_id=selected_permission).all()

			if admin_permissions:
				return view_func(request,*args, **kwargs)
			else:
				print(admin_permissions)
				print(list(admin_permissions))
				return HttpResponse("You are not authenticated to view this page!")

		return wrapper_func
	return decorator


def admin_only(view_func):
	def wrapper_function(request, *args, **kwargs):
		
		groups = []
		if request.user.groups.exists():
			all_groups = request.user.groups.all()
			for group in all_groups:
				groups.append(group.name)

		if 'Admin' in groups or 'Superadmin' in groups:
			return view_func(request, *args, **kwargs)
		else:
			return HttpResponse("You are not authenticated to view this page!")

	return wrapper_function


def superadmin_only(view_func):
	def wrapper_function(request, *args, **kwargs):
		
		group = None
		if request.user.groups.exists():
			group = request.user.groups.filter(name='Superadmin').first()
		if group:
			if group.name == 'Superadmin':
				return view_func(request, *args, **kwargs)
			else:
				return HttpResponse("You are not authenticated to view this page!")
		else:
			return HttpResponse("You are not authenticated to view this page!")
			
	return wrapper_function