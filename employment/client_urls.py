from django.urls import path
from . import client_views, home

urlpatterns =[
	path('register/', client_views.register, name='register'),
	path('register/information/', client_views.second_step_register, name='second_step_register'),


	path('profile/<str:client_id>/', home.candidate_profile, name='candidate_profile'),
	path('job/<str:job_id>/', home.public_job_details, name='public_job_details'),
	path('employer/<str:partner_id>/', home.employer_details, name='employer_details'),

	path('cv/download/', client_views.cv_download, name='cv_download'),

	
	path('inbox/', client_views.inbox, name='inbox'),
	path('mail/replays/', client_views.replays, name='replays'),
	path('inbox/mail/read/', client_views.read_mails, name='read_mails'),
	path('inbox/mail/unread/', client_views.unread_mails, name='unread_mails'),
	path('inbox/mail/trash/', client_views.trash_mails, name='trash_mails'),
	# path('inbox/mail/read/<str:mail_id>/<str:mail_nav>/replay/', client_views.mail_replay, name='mail_replay'),
	path('inbox/mail/read/<str:mail_id>/<str:mail_nav>/', client_views.mail_read, name='mail_read'),
	path('inbox/mail/<str:mail_id>/delete/', client_views.mail_delete, name='mail_delete'),
	path('inbox/mail/trash/<str:mail_id>/', client_views.mail_trash, name='mail_trash'),
	path('inbox/mail/<str:mail_id>/to_inbox/', client_views.mail_to_inbox, name='mail_to_inbox'),
	path('inbox/mail/<str:mail_id>/to_unread/', client_views.mail_to_unread, name='mail_to_unread'),
	path('accounts/profile/', client_views.c_client_profile, name='c_client_profile'),
	path('cv/update/', client_views.client_cv_update, name='client_cv_update'),

	path('jobs/', client_views.c_jobs, name='c_jobs'),
	path('jobs/applied/', client_views.client_applied_jobs, name='client_applied_jobs'),
	path('jobs/<str:job_id>/details/', client_views.c_job_details, name='c_job_details'),
	path('jobs/applied/<str:job_id>/details/', client_views.c_applied_job_details, name='c_applied_job_details'),
	path('jobs/<str:job_id>/apply/', client_views.c_job_apply, name='c_job_apply'),
	path('jobs/<str:job_id>/apply/cancel/', client_views.c_job_cancel_apply, name='c_job_cancel_apply'),
	path('jobs/<str:job_apply_id>/apply/update/', client_views.c_job_update_apply, name='c_job_update_apply'),

	# For visitors:
	path('jobs/explorer/', home.home_jobs, name='home_jobs'),
	path('employers/explorer/', home.home_employers, name='home_employers'),
	path('candidates/', home.home_candidates, name='home_candidates'),
#=====================================================
#============= Client's Experiences ==================
#=====================================================
	path('cv/experiences/create/', client_views.client_cv_experience_create, name='client_cv_experience_create'),
	path('cv/experiences/<str:experience_id>/update/', client_views.client_cv_experience_update, name='client_cv_experience_update'),
	path('cv/experiences/<str:experience_id>/', client_views.client_cv_experience, name='client_cv_experience'),
	path('cv/experiences/<str:experience_id>/delete/', client_views.client_cv_experience_delete, name='client_cv_experience_delete'),
#=====================================================
#=====================================================
#=====================================================


#=====================================================
#============= Client's Educations ===================
#=====================================================
	path('cv/educations/create/', client_views.client_cv_education_create, name='client_cv_education_create'),
	path('cv/educations/<str:education_id>/update/', client_views.client_cv_education_update, name='client_cv_education_update'),
	path('cv/educations/<str:education_id>/', client_views.client_cv_education, name='client_cv_education'),
	path('cv/educations/<str:education_id>/delete/', client_views.client_cv_education_delete, name='client_cv_education_delete'),
#=====================================================
#=====================================================
#=====================================================


#=====================================================
#============== Client's Courses =====================
#=====================================================
	path('cv/courses/create/', client_views.client_cv_course_create, name='client_cv_course_create'),
	path('cv/courses/<str:course_id>/update/', client_views.client_cv_course_update, name='client_cv_course_update'),
	path('cv/courses/<str:course_id>/', client_views.client_cv_course, name='client_cv_course'),
	path('cv/courses/<str:course_id>/delete/', client_views.client_cv_course_delete, name='client_cv_course_delete'),
#=====================================================
#=====================================================
#=====================================================


#=====================================================
#=============== Client's Skills =====================
#=====================================================
	path('cv/skills/create/', client_views.client_cv_skill_create, name='client_cv_skill_create'),
	path('cv/skills/<str:skill_id>/update/', client_views.client_cv_skill_update, name='client_cv_skill_update'),
	path('cv/skills/<str:skill_id>/', client_views.client_cv_skill, name='client_cv_skill'),
	path('cv/skills/<str:skill_id>/delete/', client_views.client_cv_skill_delete, name='client_cv_skill_delete'),
#=====================================================
#=====================================================
#=====================================================

	path('mail/<str:mail_id>/view/', client_views.pdf_client_mail_view, name='pdf_client_mail_view'),
	path('mail/<str:mail_id>/download/', client_views.pdf_client_mail_download, name='pdf_client_mail_download'),
 #====================================================
 #====================================================
 	path('notifications/all/', client_views.notifications, name='notifications'),
 	path('notifications/mark_all_as_read/', client_views.mark_notifications_read, name='mark_notifications_read'),
 	path('notifications/unread/', client_views.unread_notifications, name='unread_notifications'),
	path('notification/<str:notification_id>/read/', client_views.notification_read, name='notification_read'),
	# path('inbox/mail/unread/', client_views.unread_mails, name='unread_mails'),
	# path('inbox/mail/trash/', client_views.trash_mails, name='trash_mails'),
	# path('inbox/mail/<str:mail_id>/read/<str:mail_nav>/', client_views.mail_read, name='mail_read'),
	path('notificaion/<str:notification_id>/delete/', client_views.notification_delete, name='notification_delete'),
]