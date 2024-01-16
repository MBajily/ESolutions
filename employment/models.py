from django.db import models
import datetime
from ES.settings import MEDIA_ROOT, MEDIA_URL
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from django.contrib.auth.models import AbstractUser


#===============================================================
#========================  Cities  =============================
#===============================================================
class Cities(models.Model):
	city_id = models.AutoField(primary_key=True)
	arabic_name = models.CharField(max_length=200, null=True)
	english_name = models.CharField(max_length=200, null=True)
	
	def __str__(self):
		return self.english_name


#===============================================================
#====================  Nationalities  ==========================
#===============================================================
class Nationalities(models.Model):
	nationality_id = models.AutoField(primary_key=True)
	arabic_name = models.CharField(max_length=200, null=True)
	english_name = models.CharField(max_length=200, null=True)
	
	def __str__(self):
		return self.english_name


#===============================================================
#===================  Specializations  =========================
#===============================================================
class Specializations(models.Model):
	specialization_id = models.AutoField(primary_key=True)
	arabic_name = models.CharField(max_length=200, null=True)
	english_name = models.CharField(max_length=200, null=True)
	
	def __str__(self):
		return self.english_name


#===============================================================
#========================  Clients  ============================
#===============================================================
class Clients(models.Model):
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

	client_id = models.AutoField(primary_key=True)
	personal_id = models.CharField(unique=True, max_length=10, null=False)
	first_name = models.CharField(max_length=25, null=True)
	second_name = models.CharField(max_length=25, null=True)
	third_name = models.CharField(max_length=25, null=True)
	last_name = models.CharField(max_length=25, null=True)
	email = models.EmailField(max_length=200, null=True)
	phone_primary = models.CharField(max_length=20, null=True)
	phone_secondary = models.CharField(max_length=20, null=True)
	birth_date = models.DateField()
	gender = models.CharField(max_length=200, null=True, choices=Genders)
	degree = models.CharField(max_length=200, null=True, choices=Degrees)
	nationality = models.ForeignKey(Nationalities, null=True, on_delete=models.SET_NULL)
	specialization = models.ForeignKey(Specializations, null=True, on_delete=models.SET_NULL)
	city = models.ForeignKey(Cities, null=True, on_delete=models.SET_NULL)
	create_date = models.DateTimeField(auto_now_add=True, null=True)
	is_active = models.IntegerField(default='0')
	photo = models.ImageField(null=True, blank=True)

	@property
	def age(self):
		if self.birth_date is None:
			self.birth_date = datetime.datetime.now().date()
		return int((datetime.datetime.now().date() - self.birth_date).days / 365.25)
	def __str__(self):
		return (self.first_name + " " + self.last_name)


#-------------------  Client Courses  -----------------------
class Client_Courses(models.Model):
	course_id = models.AutoField(primary_key=True)
	client = models.ForeignKey(Clients, null=True, on_delete=models.SET_NULL)
	educational_istitution = models.CharField(max_length=200, null=True)
	title = models.CharField(max_length=200, null=True)
	date = models.DateField(null=True)
	description = models.CharField(max_length=2000, null=True)
	total_hours = models.IntegerField(null=True)
	
	def __str__(self):
		return "{} | {}".format(self.educational_istitution, self.title)


#------------------  Client Educations  ----------------------
class Client_Educations(models.Model):
	education_id = models.AutoField(primary_key=True)
	client = models.ForeignKey(Clients, null=True, on_delete=models.SET_NULL)
	educational_istitution = models.CharField(max_length=200, null=True)
	title = models.CharField(max_length=200, null=True)
	description = models.CharField(max_length=2000, null=True)
	start_date = models.DateField(null=True)
	end_date = models.DateField(null=True)
	
	def __str__(self):
		return "{} | {}".format(self.educational_istitution, self.title)


#------------------  Client Experiences  ----------------------
class Client_Experiences(models.Model):
	experience_id = models.AutoField(primary_key=True)
	client = models.ForeignKey(Clients, null=True, on_delete=models.SET_NULL)
	company_name = models.CharField(max_length=200, null=True)
	job_title = models.CharField(max_length=200, null=True)
	description = models.CharField(max_length=2000, null=True)
	start_date = models.DateField(null=True)
	end_date = models.DateField(null=True)
	
	def __str__(self):
		return "{} | {}".format(self.company_name, self.job_title)


#--------------------  Client Skills  ------------------------
class Client_Skills(models.Model):
	progress = (
		(100, 'Expert (100%)'),
		(80, 'Advanced (80%)'),
		(60, 'Excelent (60%)'),
		(40, 'Good (40%)'),
		(20, 'Beigener (20%)')
	)
	
	skill_id = models.AutoField(primary_key=True)
	client = models.ForeignKey(Clients, null=True, on_delete=models.SET_NULL)
	title = models.CharField(max_length=200, null=True)
	progress = models.IntegerField(null=True, choices=progress)
	
	def __str__(self):
		return "{}  ({}%)".format(self.title, self.progress)

#===============================================================
#========================  Partners  ===========================
#===============================================================
class Partners(models.Model):
	Categories = (
		('ministries','Ministries'),
		('banks','Banks'),
		('companies','Companies'),
		('communications','Communications'),
		('hospital','Hospital'),
	)

	partner_id = models.AutoField(primary_key=True)
	arabic_name = models.CharField(max_length=100, null=True)
	english_name = models.CharField(max_length=100, null=True)
	category = models.CharField(max_length=200, null=True, choices=Categories)
	logo = models.ImageField(null=True, blank=True)

	def __str__(self):
		return self.english_name + " | " + self.arabic_name

#===============================================================
#===========================  Jobs  ============================
#===============================================================
class Jobs(models.Model):
	Genders = (
		('Male', 'Male'),
		('Female', 'Female')
	)

	Job_Type = (
		('Full-time', 'Full-time'),
		('Part-time', 'Part-time'),
	)

	job_id = models.AutoField(primary_key=True)
	title = models.CharField(max_length=100, null=True)
	description = models.CharField(max_length=2000, null=True)
	salary = models.IntegerField(null=True)
	start_date = models.DateTimeField(auto_now_add=True, blank=True)
	end_date = models.DateField(null=True)
	company = models.ForeignKey(Partners, null=True, on_delete=models.SET_NULL)
	nationality = models.ForeignKey(Nationalities, null=True, on_delete=models.SET_NULL)
	specialization = models.ForeignKey(Specializations, null=True, on_delete=models.SET_NULL)
	city = models.ForeignKey(Cities, null=True, on_delete=models.SET_NULL)
	requirements = models.CharField(max_length=1000, null=True)
	what_we_expect_from_you = models.CharField(max_length=1000, null=True)
	what_you_have_got = models.CharField(max_length=1000, null=True)
	# gender = models.CharField(max_length=200, null=True, choices=Genders)
	# job_type = models.CharField(max_length=200, null=True, choices=Job_Type)
	is_available = models.CharField(max_length=10, null=True, default='1')
	
	def __str__(self):
		return self.title



#===============================================================
#==========================  Mails  ============================
#===============================================================
class Sent_Mail(models.Model):
	mail_id = models.AutoField(primary_key=True)
	receiver = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
	sender = models.CharField(max_length=50, null=True, default='Excelent Solutions')
	title = models.CharField(max_length=50, null=True)
	message = models.CharField(max_length=2000, null=True)
	date_sent = models.DateTimeField(auto_now_add=True, blank=True)
	is_trash = models.CharField(max_length=10, null=True, default='0')
	
	def __str__(self):
		return "{} TO {}".format(self.title, self.receiver)


#===============================================================
#=========================  Replays  ===========================
#===============================================================
class Sent_Mail_Replay(models.Model):
	replay_id = models.AutoField(primary_key=True)
	mail = models.ForeignKey(Sent_Mail, null=True, on_delete=models.CASCADE)
	sender = models.CharField(max_length=50, null=True)
	message = models.CharField(max_length=2000, null=True)
	date = models.DateTimeField(auto_now_add=True, blank=True)
	is_admin = models.BooleanField(default=False, null=True)
	
	def __str__(self):
		return "{} TO {}".format(self.sender, self.message)


#===============================================================
#=======================  Interview  ===========================
#===============================================================
class Phone_Interviews(models.Model):
	HearedAboutJob = (
		('Friend', 'Friend'),
		('ES Website', 'ES Website'),
		('Social Media', 'Social Media')
	)

	YesNoAnswer = (
		('Yes', 'Yes'),
		('No', 'No')
	)

	CallBehavior = (
		('Excelent', 'Excelent'),
		('Not Interested', 'Not Interested'),
		('Careless', 'Careless'),
		('Weak', 'Weak'),
		('Playboy', 'Playboy'),
		('Not Serious', 'Not Serious'),
	)

	FutureGoal = (
		('Seeking for Administration Position', 'Seeking for Administration Position'),
		('Waiting for Another Profession', 'Waiting for Another Profession'),
		('Looking Forward to Higher Education', 'Looking Forward to Higher Education'),
		('Interested in a Government Job', 'Interested in a Government Job'),
		("Doesn't Want to Disclose", "Doesn't Want to Disclose"),
	)

	WhyThisJob = (
		('Seeking for Administration Position', 'Seeking for Administration Position'),
		('Waiting for Another Profession', 'Waiting for Another Profession'),
		('Looking Forward to Higher Education', 'Looking Forward to Higher Education'),
		('Interested in a Government Job', 'Interested in a Government Job'),
		('For Marriage', 'For Marriage'),
		("Develop Himself", "Develop Himself"),
		("Gain Experience", "Gain Experience"),
		("Improving the Financial Situation", "Improving the Financial Situation"),
	)

	Results = (
		('Successed', 'Successed'),
		('Failed', 'Failed'),
	)

	interview_id = models.AutoField(primary_key=True)
	client = models.OneToOneField(User, null=True, on_delete=models.SET_NULL)
	how_heared_about_job = models.CharField(max_length=200, null=True, choices=HearedAboutJob)
	hear_speak_problem = models.CharField(max_length=200, null=True, choices=YesNoAnswer)
	has_health_condition = models.CharField(max_length=200, null=True, choices=YesNoAnswer)
	want_to_work = models.CharField(max_length=200, null=True, choices=YesNoAnswer)
	live_in_riyadh = models.CharField(max_length=200, null=True, choices=YesNoAnswer)
	have_transportation = models.CharField(max_length=200, null=True, choices=YesNoAnswer)
	call_behavior = models.CharField(max_length=200, null=True, choices=CallBehavior)
	future_goal = models.CharField(max_length=200, null=True, choices=FutureGoal)
	why_this_job = models.CharField(max_length=200, null=True, choices=WhyThisJob)
	saudi_driving_license = models.CharField(max_length=200, null=True, choices=YesNoAnswer)
	interview_date = models.DateTimeField(auto_now_add=True, blank=True)
	result = models.CharField(max_length=200, null=True, choices=Results)
	suited_job = models.ForeignKey(Jobs, null=True, on_delete=models.SET_NULL)
	position = models.ForeignKey(Specializations, null=True, on_delete=models.SET_NULL)
	latest_update = models.DateTimeField(null=True)
	note = models.CharField(max_length=2000, null=True)
	
	def __str__(self):
		return "{} TO {}".format(self.client.first_name)



class ES_Permission(models.Model):
	permission_id = models.AutoField(primary_key=True)
	name = models.CharField(max_length=200)
	codename = models.CharField(max_length=200, null=True)

	def __str__(self):
		return self.codename

#===============================================================
#========================  Clients  ============================
#===============================================================
class Admin_Permission(models.Model):

	id = models.AutoField(primary_key=True)
	group = models.ForeignKey(Group, null=True, on_delete=models.CASCADE)
	permission = models.ForeignKey(ES_Permission, null=True, on_delete=models.CASCADE)
