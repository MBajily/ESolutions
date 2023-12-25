from django import forms
from .client_models import *
from django.forms import inlineformset_factory
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegisterForm(UserCreationForm):

	class Meta:
		model = User
		fields = ['first_name', 'last_name', 'username', 'email']


#=====================================================
#=================== Clients Form ====================
#=====================================================
class ClientCVForm(forms.ModelForm):
	class Meta:
		model = Client_CV
		fields = '__all__'
		widgets = {
			'first_name': forms.TextInput(attrs={'name':'first_name', 'class': 'form-control', 'id': 'inputName', 'required': 'True'}),
			'second_name': forms.TextInput(attrs={'name':'second_name', 'class': 'form-control', 'id': 'inputName', 'required': 'True'}),
			'third_name': forms.TextInput(attrs={'name':'third_name', 'class': 'form-control', 'id': 'inputName', 'required': 'True'}),
			'last_name': forms.TextInput(attrs={'name':'last_name', 'class': 'form-control', 'id': 'inputName', 'required': 'True'}),
			'bio': forms.Textarea(attrs={'name':'Write About Yourself', 'class': 'form-control', 'id': 'inputName', 'placeholder': 'Cina Saffary'}),
			'email': forms.EmailInput(attrs={'name':'email', 'class':"form-control", 'id':"inputEmail", 'placeholder':"Email", 'data-error':"Bruh, that email address is invalid", 'required':'True'}),
			'personal_id': forms.TextInput(attrs={'name':'personal_id', 'type':"tel", 'class': "form-control", 'id': "validationCustom08", 'placeholder':"Primary Number", 'oninput':"check(this)", 'required':'True'}),
			'phone_primary': forms.TextInput(attrs={'name':'phone_primary', 'type':"tel", 'class': "form-control", 'id': "validationCustom08", 'placeholder':"Primary Number", 'oninput':"check(this)", 'required':'True'}),
			'phone_secondary': forms.TextInput(attrs={'name':'phone_secondary', 'type':"tel", 'class': "form-control", 'id': "validationCustom08", 'placeholder':"Secondary Number", 'oninput':"check(this)", 'required':'True'}),
			'birth_date': forms.DateInput(attrs={'name':'birth_date', 'class':"form-control", 'placeholder':"yyyy-mm-dd", 'id':"datepicker", 'required':"True", 'data-date-format':"yyyy-mm-dd"}),
			'gender': forms.Select(attrs={'name':'gender', 'class': "form-select form-select-lg mb-3", 'required': 'True'}),
			'nationality': forms.Select(attrs={'name':'nationality', 'class': "form-select form-select-lg mb-3", 'required': 'True'}),
			'specialization': forms.Select(attrs={'name':'specialization', 'class': "form-select form-select-lg mb-3", 'required': 'True'}),
			'degree': forms.Select(attrs={'name':'degree', 'class': "form-select form-select-lg mb-3", 'required': 'True'}),
			'city': forms.Select(attrs={'name':'city', 'class': "form-select form-select-lg mb-3", 'required': 'True'}),
			'photo': forms.FileInput(attrs={'name':'photo', 'id':"input-file-to-destroy", 'class':"dropify", 'data-allowed-formats':"portrait square", 'data-max-file-size':"2M", 'data-max-height':"2000", 'required':'True'})
		}
#=====================================================
#=====================================================
#=====================================================


#=====================================================
#============== Client Experiences Form ==============
#=====================================================
class ClientCVExperiencesForm(forms.ModelForm):
	class Meta:
		model = Client_CV_Experiences
		fields = '__all__'
		exclude=('full_name',)
		widgets = {
			'company_name': forms.TextInput(attrs={'name':'company_name', 'class': 'form-control', 'id': 'inputName', 'placeholder': 'Ex. Excelent Solution co.', 'required': 'True'}),
			'job_title': forms.TextInput(attrs={'name':'job_title', 'class': 'form-control', 'id': 'inputName', 'placeholder': 'Ex. Data Entry', 'required': 'True'}),
			'description': forms.Textarea(attrs={'name':'description', 'class': 'form-control', 'id': 'inputName', 'placeholder': 'Job Details', 'required': 'True'}),
			'start_date': forms.DateInput(attrs={'name':'start_date', 'class':"form-control", 'placeholder':"Start Date (yyyy-mm-dd)", 'id':"datepicker", 'required':"True", 'data-date-format':"yyyy-mm-dd"}),
			'end_date': forms.DateInput(attrs={'name':'end_date', 'class':"form-control", 'placeholder':"End Date (yyyy-mm-dd)", 'id':"datepicker", 'required':"True", 'data-date-format':"yyyy-mm-dd"}),
		}
#=====================================================
#=====================================================
#=====================================================


#=====================================================
#============= Client Educations Form ================
#=====================================================
class ClientCVEducationsForm(forms.ModelForm):
	class Meta:
		model = Client_CV_Educations
		fields = '__all__'
		widgets = {
			'educational_istitution': forms.TextInput(attrs={'name':'educational_istitution', 'class': 'form-control', 'id': 'inputName', 'placeholder': 'Ex. University of Harvard', 'required': 'True'}),
			'title': forms.TextInput(attrs={'name':'title', 'class': 'form-control', 'id': 'inputName', 'placeholder': 'Title', 'required': 'True'}),
			'description': forms.Textarea(attrs={'name':'description', 'class': 'form-control', 'id': 'inputName', 'placeholder': 'Job Details', 'required': 'True'}),
			'start_date': forms.DateInput(attrs={'name':'start_date', 'class':"form-control", 'placeholder':"Start Date (yyyy-mm-dd)", 'id':"datepicker", 'required':"True", 'data-date-format':"yyyy-mm-dd"}),
			'end_date': forms.DateInput(attrs={'name':'end_date', 'class':"form-control", 'placeholder':"End Date (yyyy-mm-dd)", 'id':"datepicker", 'required':"True", 'data-date-format':"yyyy-mm-dd"}),
			'pdf_file': forms.FileInput(attrs={'name':'pdf_file', 'id':"input-file-to-destroy", 'class':"dropify", 'data-allowed-formats':"portrait square", 'data-max-file-size':"2M", 'data-max-height':"2000", 'required':'True'}),
		}
#=====================================================
#=====================================================
#=====================================================


#=====================================================
#=============== Client Courses Form =================
#=====================================================
class ClientCVCoursesForm(forms.ModelForm):
	class Meta:
		model = Client_CV_Courses
		fields = '__all__'
		widgets = {
			'educational_istitution': forms.TextInput(attrs={'name':'educational_istitution', 'class': 'form-control', 'id': 'inputName', 'placeholder': 'Ex. University of Harvard', 'required': 'True'}),
			'title': forms.TextInput(attrs={'name':'title', 'class': 'form-control', 'id': 'inputName', 'placeholder': 'Ex. Become a Software Developer', 'required': 'True'}),
			'description': forms.Textarea(attrs={'name':'description', 'class': 'form-control', 'id': 'inputName', 'placeholder': 'Cina Saffary'}),
			'date': forms.DateInput(attrs={'name':'date', 'class':"form-control", 'placeholder':"yyyy-mm-dd", 'id':"datepicker", 'required':"True", 'data-date-format':"yyyy-mm-dd"}),
			'pdf_file': forms.FileInput(attrs={'name':'pdf_file', 'id':"input-file-to-destroy", 'class':"dropify", 'data-allowed-formats':"portrait square", 'data-max-file-size':"2M", 'data-max-height':"2000", 'required':'True'}),
			'total_hours': forms.NumberInput(attrs={'name':'total_hours', 'id':"demo2", 'type':"int", 'value':"0", 'class':"col-md-8 form-control"}),
		}
#=====================================================
#=====================================================
#=====================================================


#=====================================================
#================ Client Skills Form =================
#=====================================================
progress = (
			(100, 'Expert (100%)'),
			(80, 'Advanced (80%)'),
			(60, 'Excelent (60%)'),
			(40, 'Good (40%)'),
			(20, 'Beigener (20%)')
		)

class ClientCVSkillsForm(forms.ModelForm):
	class Meta:
		model = Client_CV_Skills
		fields = '__all__'
		widgets = {
			'title': forms.TextInput(attrs={'name':'title', 'class': 'form-control', 'id': 'inputName', 'placeholder': 'Ex. Become a Software Developer', 'required': 'True'}),
			'progress': forms.Select(attrs={'name':'progress', 'class': "form-select form-select-lg mb-3", 'required': 'True'})
		}
#=====================================================
#=====================================================
#=====================================================


#=====================================================
#=============== Client Courses Form =================
#=====================================================
class JobApplyForm(forms.ModelForm):
	class Meta:
		model = Job_Applied
		fields = '__all__'
		widgets = {
			'first_name': forms.TextInput(attrs={'name':'first_name', 'class': 'form-control', 'id': 'inputName', 'required': 'True'}),
			'second_name': forms.TextInput(attrs={'name':'second_name', 'class': 'form-control', 'id': 'inputName', 'required': 'True'}),
			'third_name': forms.TextInput(attrs={'name':'third_name', 'class': 'form-control', 'id': 'inputName', 'required': 'True'}),
			'last_name': forms.TextInput(attrs={'name':'last_name', 'class': 'form-control', 'id': 'inputName', 'required': 'True'}),
			'email': forms.EmailInput(attrs={'name':'email', 'class':"form-control", 'id':"inputEmail", 'placeholder':"Email", 'data-error':"Bruh, that email address is invalid", 'required':'True'}),
			'personal_id': forms.TextInput(attrs={'name':'personal_id', 'type':"tel", 'class': "form-control", 'id': "validationCustom08", 'placeholder':"Primary Number", 'oninput':"check(this)", 'required':'True'}),
			'phone_primary': forms.TextInput(attrs={'name':'phone_primary', 'type':"tel", 'class': "form-control", 'id': "validationCustom08", 'placeholder':"Primary Number", 'oninput':"check(this)", 'required':'True'}),
			'phone_secondary': forms.TextInput(attrs={'name':'phone_secondary', 'type':"tel", 'class': "form-control", 'id': "validationCustom08", 'placeholder':"Secondary Number", 'oninput':"check(this)", 'required':'True'}),
			'birth_date': forms.DateInput(attrs={'name':'birth_date', 'class':"form-control", 'placeholder':"yyyy-mm-dd", 'id':"datepicker", 'required':"True", 'data-date-format':"yyyy-mm-dd"}),
			'gender': forms.Select(attrs={'name':'gender', 'class': "form-select form-select-lg mb-3", 'required': 'True'}),
			'nationality': forms.Select(attrs={'name':'nationality', 'class': "form-select form-select-lg mb-3", 'required': 'True'}),
			'degree': forms.Select(attrs={'name':'degree', 'class': "form-select form-select-lg mb-3", 'required': 'True'}),
			'specialization': forms.Select(attrs={'name':'specialization', 'class': "form-select form-select-lg mb-3", 'required': 'True'}),
			'city': forms.Select(attrs={'name':'city', 'class': "form-select form-select-lg mb-3", 'required': 'True'}),
			'cv_file': forms.FileInput(attrs={'name':'cv_file', 'id':"input-file-to-destroy", 'class':"dropify", 'data-allowed-formats':"portrait square", 'data-max-file-size':"2M", 'data-max-height':"2000", 'required':'True'})
		}
#=====================================================
#=====================================================
#=====================================================