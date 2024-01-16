from django.db import models
import datetime
from ES.settings import MEDIA_ROOT
from django import forms
from django.contrib.auth.models import User
from .models import *


#===============================================================
#=======================  Client CV  ===========================
#===============================================================
class Client_CV(models.Model):
	Genders = (
			('Male', 'Male'),
			('Female', 'Female')
		)

	Degrees = (
			('Intermediate School', 'Intermediate School'),
			('High School', 'High School'),
			('Deploma', 'Deploma'),
			("Bachelor's Degree", "Bachelor's Degree"),
			("Master's Degree", "Master's Degree"),
			("PHD's Degree", "PHD's Degree")
		)

	cv_id = models.AutoField(primary_key=True)
	personal_id = models.CharField(unique=True, max_length=10, null=False)
	client = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
	first_name = models.CharField(max_length=25, null=True)
	second_name = models.CharField(max_length=25, null=True)
	third_name = models.CharField(max_length=25, null=True)
	last_name = models.CharField(max_length=25, null=True)
	email = models.EmailField(max_length=200, null=True)
	phone_primary = models.CharField(max_length=20, null=True)
	phone_secondary = models.CharField(max_length=20, null=True)
	birth_date = models.DateField()
	bio = models.TextField(max_length=1000, null=True)
	gender = models.CharField(max_length=200, null=True, choices=Genders)
	degree = models.CharField(max_length=200, null=True, choices=Degrees)
	nationality = models.ForeignKey(Nationalities, null=True, on_delete=models.SET_NULL)
	specialization = models.ForeignKey(Specializations, null=True, on_delete=models.SET_NULL)
	city = models.ForeignKey(Cities, null=True, on_delete=models.SET_NULL)
	photo = models.ImageField(null=True, blank=True)

	@property
	def age(self):
		if self.birth_date is None:
			self.birth_date = datetime.datetime.now().date()
		return int((datetime.datetime.now().date() - self.birth_date).days / 365.25)
	def __str__(self):
		return self.client.first_name


#-------------------  Client Courses  ------------------------
class Client_CV_Courses(models.Model):
	course_id = models.AutoField(primary_key=True)
	client = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
	educational_istitution = models.CharField(max_length=200, null=True)
	title = models.CharField(max_length=200, null=True)
	date = models.DateField(null=True)
	description = models.CharField(max_length=2000, null=True)
	total_hours = models.IntegerField(null=True)
	# pdf_file = models.FileField(upload_to='MEDIA_ROOT/Clients/Certificates/', max_length=2000, null=True)
	
	def __str__(self):
		return "{} | {}".format(self.educational_istitution, self.title)


#------------------  Client Educations  ----------------------
class Client_CV_Educations(models.Model):
	education_id = models.AutoField(primary_key=True)
	client = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
	educational_istitution = models.CharField(max_length=200, null=True)
	title = models.CharField(max_length=200, null=True)
	start_date = models.DateField(null=True)
	description = models.CharField(max_length=2000, null=True)
	end_date = models.DateField(null=True)
	# pdf_file = models.FileField(upload_to=MEDIA_ROOT+'/Clients/Certificates/', max_length=2000, null=True)
	
	def __str__(self):
		return "{} | {}".format(self.educational_istitution, self.title)


#------------------  Client Experiences  ----------------------
class Client_CV_Experiences(models.Model):
	experience_id = models.AutoField(primary_key=True)
	client = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
	company_name = models.CharField(max_length=200, null=True)
	job_title = models.CharField(max_length=200, null=True)
	description = models.CharField(max_length=2000, null=True)
	start_date = models.DateField(null=True)
	end_date = models.DateField(null=True)
	
	def __str__(self):
		return "{} | {}".format(self.company_name, self.job_title)


#--------------------  Client Skills  ------------------------
class Client_CV_Skills(models.Model):
	progress = (
			(100, 'Expert (100%)'),
			(80, 'Advanced (80%)'),
			(60, 'Excelent (60%)'),
			(40, 'Good (40%)'),
			(20, 'Beigener (20%)')
		)
	skill_id = models.AutoField(primary_key=True)
	client = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
	title = models.CharField(max_length=200, null=True)
	progress = models.IntegerField(null=True, choices=progress)
	
	def __str__(self):
		return "{}  ({}%)".format(self.title, self.progress)


#===============================================================
#======================  Job Applied  ==========================
#===============================================================
class Job_Applied(models.Model):
	Genders = (
			('Male', 'Male'),
			('Female', 'Female')
		)

	Degrees = (
			('Intermediate School', 'Intermediate School'),
			('High School', 'High School'),
			('Deploma', 'Deploma'),
			("Bachelor's Degree", "Bachelor's Degree"),
			("Master's Degree", "Master's Degree"),
			("PHD's Degree", "PHD's Degree")
		)

	apply_id = models.AutoField(primary_key=True)
	job = models.ForeignKey(Jobs, on_delete=models.DO_NOTHING)
	client = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=True)
	date = models.DateField(auto_now_add=True, blank=True)
	personal_id = models.CharField(max_length=10, null=True)
	first_name = models.CharField(max_length=25, null=True)
	second_name = models.CharField(max_length=25, null=True)
	third_name = models.CharField(max_length=25, null=True)
	last_name = models.CharField(max_length=25, null=True)
	email = models.EmailField(max_length=200, null=True)
	phone_primary = models.CharField(max_length=20, null=True)
	phone_secondary = models.CharField(max_length=20, null=True)
	birth_date = models.DateField(null=True)
	gender = models.CharField(max_length=200, null=True, choices=Genders)
	degree = models.CharField(max_length=200, null=True, choices=Degrees)
	nationality = models.ForeignKey(Nationalities, null=True, on_delete=models.SET_NULL)
	cover_letter = models.CharField(max_length=2000, null=True)
	specialization = models.ForeignKey(Specializations, null=True, on_delete=models.SET_NULL)
	city = models.ForeignKey(Cities, null=True, on_delete=models.SET_NULL)
	resume = models.FileField(null=True, blank=True, upload_to=MEDIA_ROOT, max_length=100)

	def __str__(self):
		return "{}  ({}%)".format(self.apply_id, self.job.title)

#===============================================================
#=========================  Mail  ==============================
#===============================================================
class Mail(models.Model):
	mail_id = models.AutoField(primary_key=True)
	receiver = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
	sender = models.CharField(max_length=50, null=True, default='Jobs Solutions')
	title = models.CharField(max_length=50, null=True)
	message = models.CharField(max_length=2000, null=True)
	date_receive = models.DateTimeField(auto_now_add=True, blank=True)
	is_read = models.CharField(max_length=10, null=True, default='0')
	is_trash = models.CharField(max_length=10, null=True, default='0')
	
	def __str__(self):
		return "{} | {}".format(self.title, self.sender)

#===============================================================
#=========================  Replays  ==============================
#===============================================================
class Mail_Replay(models.Model):
	replay_id = models.AutoField(primary_key=True)
	mail = models.ForeignKey(Mail, null=True, on_delete=models.CASCADE)
	sender = models.CharField(max_length=50, null=True)
	message = models.CharField(max_length=2000, null=True)
	date = models.DateTimeField(auto_now_add=True, blank=True)
	is_admin = models.BooleanField(default=False, null=True)
	
	def __str__(self):
		return "{} | {}".format(self.sender, self.message)


#===============================================================
#======================  Notification  ==============================
#===============================================================
class Notification(models.Model):
	notification_id = models.AutoField(primary_key=True)
	job = models.ForeignKey(Jobs, on_delete=models.DO_NOTHING)
	receiver = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
	title = models.CharField(max_length=50, null=True)
	message = models.CharField(max_length=2000, null=True)
	date_receive = models.DateTimeField(auto_now_add=True, blank=True)
	is_read = models.CharField(max_length=10, null=True, default='0')
	
	def __str__(self):
		return "{} | {}".format(self.title, self.receiver)