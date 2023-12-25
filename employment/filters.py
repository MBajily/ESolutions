import django_filters
from django_filters import DateFilter, CharFilter, ChoiceFilter

from .models import *
from .client_models import *


class ClientsFilter(django_filters.FilterSet):

	
	end_date = DateFilter(
		field_name='birth_date', 
		lookup_expr='lte', 
		widget=forms.DateInput(attrs={'class':"form-control", 'name':'birth_date', 'placeholder':"yyyy-mm-dd", 'id':"datepicker", 'data-date-format':"yyyy-mm-dd"}),
		)
	# Email = CharFilter(field_name='email', lookup_expr='icontains')
	# Full_Name = CharFilter(field_name='full_name', lookup_expr='icontains')
	Genders = [
		('Male', 'Male'),
		('Female', 'Female')
	]

	Degrees = [
		('Intermediate School', 'Intermediate School'),
		('High School', 'High School'),
		('Deploma', 'Deploma'),
		("Bachelor's Degree", "Bachelor's Degree"),
		("Master's Degree", "Master's Degree"),
		("PHD's Degree", "PHD's Degree")
	]

	nationality = ChoiceFilter( 
		choices=[(item.nationality_id, item.english_name) for item in Nationalities.objects.all()],
		widget=forms.Select(attrs={'class':'form-select form-select-lg d-block'}))
	
	specialization = ChoiceFilter( 
		choices=[(item.specialization_id, item.english_name) for item in Specializations.objects.all()],
		widget=forms.Select(attrs={'class':'form-select form-select-lg d-block'}))

	gender = ChoiceFilter( 
		choices=Genders,
		widget=forms.Select(attrs={'class':'form-select form-select-lg d-block'}))

	degree = ChoiceFilter( 
		choices=Degrees,
		widget=forms.Select(attrs={'class':'form-select form-select-lg d-block'}))
	
	city = ChoiceFilter( 
		choices=[(item.city_id, item.english_name) for item in Cities.objects.all()],
		widget=forms.Select(attrs={'class':'form-select form-select-lg d-block'}))
	
	class Meta:
		model = Clients
		fields = '__all__'
		exclude = ['create_date', 'photo', 'cv_file', 'email', 'first_name', 'second_name', 'third_name', 'last_name', 'birth_date', 'phone_primary', 'phone_secondary', 'is_active', 'personal_id']


class ActiveClientsFilter(django_filters.FilterSet):
	Genders = [
		('Male', 'Male'),
		('Female', 'Female')
	]

	Degrees = [
		('Intermediate School', 'Intermediate School'),
		('High School', 'High School'),
		('Deploma', 'Deploma'),
		("Bachelor's Degree", "Bachelor's Degree"),
		("Master's Degree", "Master's Degree"),
		("PHD's Degree", "PHD's Degree")
	]

	nationality = ChoiceFilter( 
		choices=[(item.nationality_id, item.english_name) for item in Nationalities.objects.all()],
		widget=forms.Select(attrs={'class':'form-select form-select-lg d-block mb-3'}))
	
	specialization = ChoiceFilter( 
		choices=[(item.specialization_id, item.english_name) for item in Specializations.objects.all()],
		widget=forms.Select(attrs={'class':'form-select form-select-lg d-block mb-3'}))

	gender = ChoiceFilter( 
		choices=Genders,
		widget=forms.Select(attrs={'class':'form-select form-select-lg d-block mb-3'}))

	degree = ChoiceFilter( 
		choices=Degrees,
		widget=forms.Select(attrs={'class':'form-select form-select-lg d-block mb-3'}))
	
	city = ChoiceFilter( 
		choices=[(item.city_id, item.english_name) for item in Cities.objects.all()],
		widget=forms.Select(attrs={'class':'form-select form-select-lg d-block mb-3'}))

	class Meta:
		model = Client_CV
		fields = ['specialization', 'nationality', 'gender', 'city', 'degree']
		exclude = ['personal_id']



class JobsFilter(django_filters.FilterSet):
	# start_date = DateFilter(field_name='date', lookup_expr='gte')
	# end_date = DateFilter(field_name='date', lookup_expr='lte')
	
	company = ChoiceFilter( 
		choices=[(item.partner_id, item.english_name) for item in Partners.objects.all()],
		widget=forms.Select(attrs={'class':'form-select form-select-sm d-block mb-3'}))
	
	nationality = ChoiceFilter( 
		choices=[(item.nationality_id, item.english_name) for item in Nationalities.objects.all()],
		widget=forms.Select(attrs={'class':'form-select form-select-sm d-block mb-3'}))
	
	specialization = ChoiceFilter( 
		choices=[(item.specialization_id, item.english_name) for item in Specializations.objects.all()],
		widget=forms.Select(attrs={'class':'form-select form-select-sm d-block mb-3'}))
	
	city = ChoiceFilter( 
		choices=[(item.city_id, item.english_name) for item in Cities.objects.all()],
		widget=forms.Select(attrs={'class':'form-select form-select-sm d-block mb-3'}))
	
	class Meta:
		model = Jobs
		fields = '__all__'
		exclude = ['title', 'description', 'requirements', 'what_we_expect_from_you', 'what_you_have_got', 'salary', 'start_date', 'end_date', 'is_available']



class EndedInterviewsFilter(django_filters.FilterSet):
	start_date = DateFilter(field_name='interview_date', lookup_expr='gte')
	end_date = DateFilter(field_name='interview_date', lookup_expr='lte')
	HearedAboutJob = [
		('Friend', 'Friend - صديق'),
		('ES Website', 'ES Website - موقع الحلول الممتازة'),
		('Social Media', 'Social Media - منصات التواصل الإجتماعي')
	]
	CallBehavior = [
		('Excelent', 'Excelent - ممتاز'),
		('Not Interested', 'Not Interested - غير مهتم'),
		('Careless', 'Careless - غير مبالي'),
		('Weak', 'Weak - ضعيف'),
		('Playboy', 'Playboy - مستهتر'),
		('Not Serious', 'Not Serious - غير جاد'),
	]
	FutureGoal = [
		('Seeking for Administration Position', 'Seeking for Administration Position - يبحث عن منصب إداري'),
		('Waiting for Another Profession', 'Waiting for Another Profession - ينتظر مهنة أخرى'),
		('Looking Forward to Higher Education', 'Looking Forward to Higher Education - متطلع للتعليم العالي'),
		('Interested in a Government Job', 'Interested in a Government Job - مهتم بوظيفة حكومية'),
		("Doesn't Want to Disclose", "Doesn't Want to Disclose - لا يرغب بالإفصاح"),
	]
	WhyThisJob = [
		('Seeking for Administration Position', 'Seeking for Administration Position - يبحث عن منصب إداري'),
		('Waiting for Another Profession', 'Waiting for Another Profession - ينتظر مهنة أخرى'),
		('Looking Forward to Higher Education', 'Looking Forward to Higher Education - متطلع للتعليم العالي'),
		('Interested in a Government Job', 'Interested in a Government Job - مهتم بوظيفة حكومية'),
		('For Marriage', 'For Marriage - الزواج'),
		("Develop Himself", "Develop Himself - تطوير نفسه"),
		("Gain Experience", "Gain Experience - إكتساب خبرة"),
		("Improving the Financial Situation", "Improving the Financial Situation - تحسين الوضع المالي"),
	]
	Results = [
		('Successed', 'Successed - ناجح'),
		('Failed', 'Failed - راسب'),
	]
	YesNoAnswer = [
		('Yes', 'Yes - نعم'),
		('No', 'No - لا')
	]

	how_heared_about_job = ChoiceFilter( 
		choices=HearedAboutJob,
		widget=forms.Select(attrs={'class':'form-select form-select-lg d-block mb-3'}))
	hear_speak_problem = ChoiceFilter( 
		choices=YesNoAnswer,
		widget=forms.Select(attrs={'class':'form-select form-select-lg d-block mb-3'}))
	want_to_work = ChoiceFilter( 
		choices=YesNoAnswer,
		widget=forms.Select(attrs={'class':'form-select form-select-lg d-block mb-3'}))
	live_in_riyadh = ChoiceFilter( 
		choices=YesNoAnswer,
		widget=forms.Select(attrs={'class':'form-select form-select-lg d-block mb-3'}))
	have_transportation = ChoiceFilter( 
		choices=YesNoAnswer,
		widget=forms.Select(attrs={'class':'form-select form-select-lg d-block mb-3'}))
	cal_behavior = ChoiceFilter( 
		choices=CallBehavior,
		widget=forms.Select(attrs={'class':'form-select form-select-lg d-block mb-3'}))
	future_goal = ChoiceFilter( 
		choices=FutureGoal,
		widget=forms.Select(attrs={'class':'form-select form-select-lg d-block mb-3'}))
	why_this_job = ChoiceFilter( 
		choices=WhyThisJob,
		widget=forms.Select(attrs={'class':'form-select form-select-lg d-block mb-3'}))
	saudi_driving_license = ChoiceFilter( 
		choices=YesNoAnswer,
		widget=forms.Select(attrs={'class':'form-select form-select-lg d-block mb-3'}))
	has_health_condition = ChoiceFilter( 
		choices=YesNoAnswer,
		widget=forms.Select(attrs={'class':'form-select form-select-lg d-block mb-3'}))
	result = ChoiceFilter( 
		choices=Results,
		widget=forms.Select(attrs={'class':'form-select form-select-lg d-block mb-3'}))
	
	class Meta:
		model = Phone_Interviews
		fields = '__all__'
		exclude = ['client', 'future_goal', 'why_this_job', 'note', 'how_heared_about_job', 'interview_date']