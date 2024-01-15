from django import forms
from .models import *
from django.forms import inlineformset_factory
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


#=====================================================
#=================== Admins Form ====================
#=====================================================
class AdminsForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ['first_name', 'last_name', 'email', 'username', 'groups']
		widgets = {
			'first_name': forms.TextInput(attrs={'name':'first_name', 'class': 'form-control', 'id': 'inputName', 'required': 'True'}),
			'last_name': forms.TextInput(attrs={'name':'last_name', 'class': 'form-control', 'id': 'inputName', 'required': 'True'}),
			'email': forms.EmailInput(attrs={'name':'email', 'class':"form-control", 'id':"inputEmail", 'placeholder':"Email", 'data-error':"Bruh, that email address is invalid", 'required':'True'}),
			'username': forms.TextInput(attrs={'name':'username', 'type':"text", 'class': "form-control", 'id': "validationCustom08", 'placeholder':"Primary Number", 'oninput':"check(this)", 'required':'True'}),
		}
#=====================================================
#=====================================================
#=====================================================

#=====================================================
#=================== Clients Form ====================
#=====================================================
class ClientsForm(forms.ModelForm):
	class Meta:
		model = Clients
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
			# 'specialization': forms.Select(attrs={'name':'specialization', 'class': "form-select form-select-lg mb-3", 'required': 'True'}),
			# 'city': forms.Select(attrs={'name':'city', 'class': "form-select form-select-lg mb-3", 'required': 'True'}),
			# 'photo': forms.FileInput(attrs={'name':'photo', 'id':"input-file-to-destroy", 'class':"dropify", 'data-allowed-formats':"portrait square", 'data-max-file-size':"2M", 'data-max-height':"2000", 'required':'True'})
		}
#=====================================================
#=====================================================
#=====================================================


#=====================================================
#==================== Jobs Form ======================
#=====================================================
class JobsForm(forms.ModelForm):
	class Meta:
		model = Jobs
		fields = '__all__'
		widgets = {
			'title': forms.TextInput(attrs={'class': 'form-control', 'id': 'inputName', 'placeholder': 'Cina Saffary', 'required': 'True'}),
			'salary': forms.TextInput(attrs={'class': 'form-control', 'id': 'inputName', 'placeholder': 'Cina Saffary', 'required': 'True'}),
			'description': forms.Textarea(attrs={'class': 'form-control', 'id': 'inputName', 'placeholder': 'Cina Saffary', 'required': 'True'}),
			'requirements': forms.Textarea(attrs={'class': 'form-control', 'id': 'inputName', 'placeholder': 'Cina Saffary', 'required': 'True'}),
			'what_we_expect_from_you': forms.Textarea(attrs={'class': 'form-control', 'id': 'inputName', 'placeholder': 'Cina Saffary', 'required': 'True'}),
			'what_you_have_got': forms.Textarea(attrs={'class': 'form-control', 'id': 'inputName', 'placeholder': 'Cina Saffary', 'required': 'True'}),
			'start_date': forms.DateInput(attrs={'class':"form-control", 'name':'start_date', 'placeholder':"Start Date (yyyy-mm-dd)", 'id':"datepicker", 'required':"True", 'data-date-format':"yyyy-mm-dd"}),
			'end_date': forms.DateInput(attrs={'class':"form-control", 'autocomplete':"off", 'name':'end_date', 'placeholder':"End Date (yyyy-mm-dd)", 'id':"datepicker", 'required': 'False', 'data-date-format':"yyyy-mm-dd"}),
			'nationality': forms.Select(attrs={'class': "form-select form-select-lg mb-3", 'required': 'True'}),
			'gender': forms.Select(attrs={'class': "form-select form-select-lg mb-3", 'required': 'True'}),
			'job_type': forms.Select(attrs={'class': "form-select form-select-lg mb-3", 'required': 'True'}),
			'specialization': forms.Select(attrs={'class': "form-select form-select-lg mb-3", 'required': 'True'}),
			'company': forms.Select(attrs={'class': "form-select form-select-lg mb-3", 'required': 'True'}),
			'city': forms.Select(attrs={'class': "form-select form-select-lg mb-3", 'required': 'True'}),
		}
#=====================================================
#=====================================================
#=====================================================


#=====================================================
#============== Client Experiences Form ==============
#=====================================================
class ClientExperiencesForm(forms.ModelForm):
	class Meta:
		model = Client_Experiences
		fields = '__all__'
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
class ClientEducationsForm(forms.ModelForm):
	class Meta:
		model = Client_Educations
		fields = '__all__'
		widgets = {
			'educational_istitution': forms.TextInput(attrs={'name':'educational_istitution', 'class': 'form-control', 'id': 'inputName', 'placeholder': 'Ex. University of Harvard', 'required': 'True'}),
			'title': forms.TextInput(attrs={'name':'title', 'class': 'form-control', 'id': 'inputName', 'placeholder': 'Title', 'required': 'True'}),
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
class ClientCoursesForm(forms.ModelForm):
	class Meta:
		model = Client_Courses
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

class ClientSkillsForm(forms.ModelForm):
	class Meta:
		model = Client_Skills
		fields = '__all__'
		widgets = {
			'title': forms.TextInput(attrs={'name':'title', 'class': 'form-control', 'id': 'inputName', 'placeholder': 'Ex. Become a Software Developer', 'required': 'True'}),
			'progress': forms.Select(attrs={'name':'progress', 'class': "form-select form-select-lg mb-3", 'required': 'True'})
		}
#=====================================================
#=====================================================
#=====================================================


#=====================================================
#============== Specializations Form =================
#=====================================================
class SpecializationsForm(forms.ModelForm):
	class Meta:
		model = Specializations
		fields = '__all__'
		widgets = {
			'english_name': forms.TextInput(attrs={'name':'english_name', 'class': 'form-control', 'id': 'inputName', 'placeholder': 'English Name', 'required': 'True'}),
			'arabic_name': forms.TextInput(attrs={'name':'arabic_name', 'class': 'form-control', 'id': 'inputName', 'placeholder': 'Arabic Name', 'required': 'True'}),
			}
#=====================================================
#=====================================================
#=====================================================


#=====================================================
#================== Partners Form ====================
#=====================================================
class PartnersForm(forms.ModelForm):
	class Meta:
		model = Partners
		fields = '__all__'
		widgets = {
			'english_name': forms.TextInput(attrs={'name':'english_name', 'class': 'form-control', 'id': 'inputName', 'placeholder': 'English Name', 'required': 'True'}),
			'arabic_name': forms.TextInput(attrs={'name':'arabic_name', 'class': 'form-control', 'id': 'inputName', 'placeholder': 'Arabic Name', 'required': 'True'}),
			'category': forms.Select(attrs={'class': "form-select form-select-lg mb-3", 'required': 'True'}),
			'logo': forms.FileInput(attrs={'name':'logo', 'id':"input-file-to-destroy", 'class':"dropify", 'data-max-file-size':"2M", 'data-max-height':"2000", 'required':'True'}),
			}
#=====================================================
#=====================================================
#=====================================================


#=====================================================
#============== Phone Interview Form =================
#=====================================================
class PhoneInterviewsForm(forms.ModelForm):
	class Meta:
		model = Phone_Interviews
		fields = '__all__'
		exclude=('client',)
		widgets = {
			'how_heared_about_job': forms.Select(attrs={'name':'how_heared_about_job', 'class': "form-select form-select-lg", 'required': 'True'}),
			'hear_speak_problem': forms.Select(attrs={'name':'hear_speak_problem', 'class': "form-select form-select-lg", 'required': 'True'}),
			'has_health_condition': forms.Select(attrs={'name':'has_health_condition', 'class': "form-select form-select-lg", 'required': 'True'}),
			'want_to_work': forms.Select(attrs={'name':'want_to_work', 'class': "form-select form-select-lg", 'required': 'True'}),
			'live_in_riyadh': forms.Select(attrs={'name':'live_in_riyadh', 'class': "form-select form-select-lg", 'required': 'True'}),
			'have_transportation': forms.Select(attrs={'name':'have_transportation', 'class': "form-select form-select-lg", 'required': 'True'}),
			'call_behavior': forms.Select(attrs={'name':'call_behavior', 'class': "form-select form-select-lg", 'required': 'True'}),
			'future_goal': forms.Select(attrs={'name':'future_goal', 'class': "form-select form-select-lg", 'required': 'True'}),
			'why_this_job': forms.Select(attrs={'name':'why_this_job', 'class': "form-select form-select-lg", 'required': 'True'}),
			'saudi_driving_license': forms.Select(attrs={'name':'saudi_driving_license', 'class': "form-select form-select-lg", 'required': 'True'}),
			'result': forms.Select(attrs={'name':'result', 'class': "form-select form-select-lg", 'required': 'True'}),
			'suited_job': forms.Select(attrs={'name':'suited_job', 'class': "form-select form-select-lg", 'required': 'True'}),
			'position': forms.Select(attrs={'name':'position', 'class': "form-select form-select-lg", 'required': 'True'}),
			'note': forms.Textarea(attrs={'name':'note', 'class': 'form-control', 'id': 'inputName', 'placeholder': 'Write your notes about this client'}),
			}
#=====================================================
#=====================================================
#=====================================================