from django.shortcuts import render
from .models import *
from .client_models import *
from .decorators import admin_only
from django.contrib.auth.decorators import login_required
#================ Export As PDF ======================
from io import BytesIO
from django.http import HttpResponse
from django.template.loader import get_template
from django.views import View
from xhtml2pdf import pisa
#=====================================================


#=====================================================
#===================== Mail PDF ======================
#=====================================================
#------------------ PDF Mail view --------------------
@login_required(login_url='login')
@admin_only
def pdf_mail_view(request, mail_id):
	template = get_template('en/staff/pdf/PDF_Mail.html')
	selected_mail = Sent_Mail.objects.get(mail_id=mail_id)
	data = {
			'title':selected_mail.title,
			'receiver':selected_mail.receiver,
			'sender':selected_mail.sender,
			'message':selected_mail.message,
			'date_sent':selected_mail.date_sent
			}
	html = template.render(data)
	result = BytesIO()
	pdf = pisa.pisaDocument(BytesIO(html.encode('cp1252')), result)
	
	if not pdf.err:
		pdf = HttpResponse(result.getvalue(), content_type='application/pdf')
	
	return HttpResponse(pdf, content_type='application/pdf')
#-----------------------------------------------------

#--------------- PDF Mail Download -------------------
@login_required(login_url='login')
@admin_only
def pdf_mail_download(request, mail_id):
	template = get_template('en/staff/pdf/PDF_Mail.html')
	selected_mail = Sent_Mail.objects.get(mail_id=mail_id)
	data = {
			'title':selected_mail.title,
			'receiver':selected_mail.receiver,
			'sender':selected_mail.sender,
			'message':selected_mail.message,
			'date_sent':selected_mail.date_sent
			}
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
#============== Active Clients' CVs PDF ==============
#=====================================================
#--------------- Clients' CVs PDF View ---------------
@login_required(login_url='login')
@admin_only
def pdf_client_cv_view(request, client_id):
	template = get_template('en/staff/pdf/cv_pdf.html')
	selected_client = User.objects.get(id=client_id)
	client_cv = Client_CV.objects.get(client_id=client_id)
	client_experience = Client_CV_Experiences.objects.filter(client_id=client_id).all()
	client_courses = Client_CV_Courses.objects.filter(client_id=client_id).all()
	client_skills = Client_CV_Skills.objects.filter(client_id=client_id).all()
	client_educations = Client_CV_Educations.objects.filter(client_id=client_id).all()
	data = {
			'selected_client':selected_client,
			'client_cv':client_cv,
			'client_experience':client_experience,
			'client_courses':client_courses,
			'client_skills':client_skills,
			'client_educations':client_educations
			}
	html = template.render(data)
	result = BytesIO()
	pdf = pisa.pisaDocument(BytesIO(html.encode('cp1252')), result)
	
	if not pdf.err:
		pdf = HttpResponse(result.getvalue(), content_type='application/pdf')
	
	return HttpResponse(pdf, content_type='application/pdf')
#-----------------------------------------------------

#------------ Clients' CVs PDF Download --------------
@login_required(login_url='login')
@admin_only
def pdf_client_cv_download(request, client_id):
	template = get_template('en/staff/pdf/cv_pdf.html')
	selected_client = User.objects.get(id=client_id)
	client_cv = Client_CV.objects.filter(client_id=client_id).all()
	client_experience = Client_CV_Experiences.objects.filter(client_id=client_id).all()
	client_courses = Client_CV_Courses.objects.filter(client_id=client_id).all()
	client_skills = Client_CV_Skills.objects.filter(client_id=client_id).all()
	client_educations = Client_CV_Educations.objects.filter(client_id=client_id).all()
	data = {
			'selected_client':selected_client,
			'client_cv':client_cv,
			'client_experience':client_experience,
			'client_courses':client_courses,
			'client_skills':client_skills,
			'client_educations':client_educations,
			'client_id':client_id
			}

	html = template.render(data)
	result = BytesIO()
	pdf = pisa.pisaDocument(BytesIO(html.encode('cp1252')), result)
	
	if not pdf.err:
		pdf = HttpResponse(result.getvalue(), content_type='application/pdf')
	response = HttpResponse(pdf, content_type='application/pdf')
	file_name = "%s" %(selected_client.first_name)
	content = "attachment; filename='%s.pdf'" %(file_name)
	response['Content-Disposition'] = content
	
	return response
#-----------------------------------------------------
#=====================================================
#=====================================================
#=====================================================


#=====================================================
#====================== CVs PDF ======================
#=====================================================
#------------------- CVs PDF View --------------------
@login_required(login_url='login')
def pdf_cv_view(request, client_id):
	template = get_template('en/staff/pdf/cv_pdf.html')
	selected_client = Clients.objects.filter(client_id=client_id).all()
	client_experience = Client_Experiences.objects.filter(client_id=client_id).all()
	client_courses = Client_Courses.objects.filter(client_id=client_id).all()
	client_skills = Client_Skills.objects.filter(client_id=client_id).all()
	client_educations = Client_Educations.objects.filter(client_id=client_id).all()
	data = {
			'selected_client':selected_client,
			'client_experience':client_experience,
			'client_courses':client_courses,
			'client_skills':client_skills,
			'client_educations':client_educations
			}
	result = BytesIO()
	pdf = pisa.pisaDocument(BytesIO(html.encode('cp1252')), result)
	
	if not pdf.err:
		pdf = HttpResponse(result.getvalue(), content_type='application/pdf')
	
	return HttpResponse(pdf, content_type='application/pdf')
#-----------------------------------------------------

#----------------- CVs PDF Download ------------------
@login_required(login_url='login')
def pdf_cv_download(request, client_id):
	template = get_template('en/staff/pdf/cv_pdf.html')
	selected_client = Clients.objects.filter(client_id=client_id).all()
	client_experience = Client_Experiences.objects.filter(client_id=client_id).all()
	client_courses = Client_Courses.objects.filter(client_id=client_id).all()
	client_skills = Client_Skills.objects.filter(client_id=client_id).all()
	client_educations = Client_Educations.objects.filter(client_id=client_id).all()
	data = {
			'selected_client':selected_client,
			'client_experience':client_experience,
			'client_courses':client_courses,
			'client_skills':client_skills,
			'client_educations':client_educations
			}
	result = BytesIO()
	pdf = pisa.pisaDocument(BytesIO(html.encode('cp1252')), result)
	
	if not pdf.err:
		pdf = HttpResponse(result.getvalue(), content_type='application/pdf')
	response = HttpResponse(pdf, content_type='application/pdf')
	file_name = "%s" %(selected_client.title)
	content = "attachment; filename='%s.pdf'" %(file_name)
	response['Content-Disposition'] = content
	
	return response
#-----------------------------------------------------
#=====================================================
#=====================================================
#=====================================================