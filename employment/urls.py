from django.urls import path
from . import views, staff_inactive_clients, staff_active_clients, staff_jobs, staff_mails, staff_partners, staff_pdf, staff_interviews, staff_specializations, home, staff_admins, pdf
from django.contrib.auth import views as auth_views

urlpatterns =[

	path('login/redirect/', home.login_redirect_page, name="login_redirect_page"),
#=====================================================
#===================== Home ==========================
#=====================================================

	path('', home.home, name='home'),
	path("password_reset/", home.password_reset_request, name="password_reset"),
	path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='registration/Password_Reset_Done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="registration/Password_Reset_Confirm.html"), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='registration/Password_Reset_Complete.html'), name='password_reset_complete'), 

    path('contact/', home.contact, name='contact'),

#=====================================================
#=====================================================
#=====================================================


#=====================================================
#==================== Admins =========================
#=====================================================
	
	path('admins/roles/', staff_admins.all_roles, name='all_roles'),
	path('admins/role/add/', staff_admins.role_create, name='role_create'),
	path('admins/roles/<str:role_id>/delete/', staff_admins.role_delete, name='role_delete'),
	path('admins/roles/<str:role_id>/update/', staff_admins.role_update, name='role_update'),
	path('admins/', staff_admins.admins, name='admins'),
	path('admins/information/update/', staff_admins.admin_information_update, name='admin_information_update'),
	path('admins/password/update/', staff_admins.admin_password_update, name='admin_password_update'),
	path('admins/add/', staff_admins.add_admin, name='add_admin'),
	path('admins/<str:admin_id>/delete/', staff_admins.admin_delete, name='admin_delete'),
	path('admins/<str:admin_id>/update/', staff_admins.admin_update, name='admin_update'),

#=====================================================
#=====================================================
#=====================================================


#=====================================================
#=================== Dashboard =======================
#=====================================================

	path('dashboard/', views.dashboard, name='dashboard'),

#=====================================================
#=====================================================
#=====================================================


#=====================================================
#===================== Mails =========================
#=====================================================

	path('mail/sent/replays/', staff_mails.mail_replays, name='mail_replays'),
	path('mail/sent/', staff_mails.sent_mails, name='sent_mails'),
	path('mail/inbox/', staff_mails.mail_inbox, name='mail_inbox'),
	path('mail/trash/', staff_mails.trash_sent_mails, name='trash_sent_mails'),
	path('mail/read/<str:mail_id>/', staff_mails.read_sent_mail, name='read_sent_mail'),
	path('mail/<str:mail_id>/trash/', staff_mails.sent_mail_trash, name='sent_mail_trash'),
	path('client/active/<str:client_id>/mail/send/', staff_mails.send_mail, name='send_mail'),
	path('client/mail/send/', staff_mails.send_mail_client_id, name='send_mail_client_id'),
	path('send/group/', staff_mails.send_message_group, name='send_message_group'),
	path('sent/<str:mail_id>/to_inbox/', staff_mails.to_inbox, name='to_inbox'),

#=====================================================
#=====================================================
#=====================================================


#=====================================================
#================= Active Clients ====================
#=====================================================

	path('clients/active/', staff_active_clients.active_clients, name='active_clients'),
	path('client/active/<str:client_id>/profile/', staff_active_clients.active_client_profile, name='active_client_profile'),
	path('clients/active/export/csv/', staff_active_clients.export_active_clients_csv, name='export_active_clients_csv'),
	path('client/active/profile/experiences/<str:experience_id>/', staff_active_clients.active_client_experience, name='active_client_experience'),
	path('client/active/profile/educations/<str:education_id>/', staff_active_clients.active_client_education, name='active_client_education'),
	path('client/active/profile/courses/<str:course_id>/', staff_active_clients.active_client_course, name='active_client_course'),

#=====================================================
#=====================================================
#=====================================================


#=====================================================
#================ Inactive Clients ===================
#=====================================================

	path('clients/inactive/', staff_inactive_clients.clients, name='clients'),
	path('client/create/', staff_inactive_clients.client_create, name='client_create'),
	path('client/<str:client_id>/profile/', staff_inactive_clients.client_profile, name='client_profile'),
	path('client/<str:client_id>/update/', staff_inactive_clients.client_update, name='client_update'),
	path('client/<str:client_id>/delete/', staff_inactive_clients.client_delete, name='client_delete'),
	path('clients/export/csv/', staff_inactive_clients.export_clients_csv, name='export_clients_csv'),
	# path('client/login/', staff_registrations.client_login, name='client_login'),
	# path('client/register/', staff_registrations.client_register, name='client_register'),
	# path('client/recoverpassword/', staff_registrations.client_recoverpassword, name='client_recoverpassword'),
	# # path('clients/download/', staff_inactive_clients.clients_download, name='clients_download'),

#=====================================================
#=====================================================
#=====================================================


#=====================================================
#================== Experiences ======================
#=====================================================

	path('client/<str:client_id>/experiences/create/', staff_inactive_clients.client_experience_create, name='client_experience_create'),
	path('client/<str:client_id>/experiences/<str:experience_id>/update/', staff_inactive_clients.client_experience_update, name='client_experience_update'),
	path('experiences/<str:experience_id>/', staff_inactive_clients.client_experience, name='client_experience'),
	path('client/<str:client_id>/experiences/<str:experience_id>/delete/', staff_inactive_clients.client_experience_delete, name='client_experience_delete'),

#=====================================================
#=====================================================
#=====================================================


#=====================================================
#================== Educations =======================
#=====================================================

	path('client/<str:client_id>/educations/create/', staff_inactive_clients.client_education_create, name='client_education_create'),
	path('client/<str:client_id>/educations/<str:education_id>/update/', staff_inactive_clients.client_education_update, name='client_education_update'),
	path('educations/<str:education_id>/', staff_inactive_clients.client_education, name='client_education'),
	path('client/<str:client_id>/educations/<str:education_id>/delete/', staff_inactive_clients.client_education_delete, name='client_education_delete'),

#=====================================================
#=====================================================
#=====================================================


#=====================================================
#==================== Courses ========================
#=====================================================

	path('client/<str:client_id>/courses/create/', staff_inactive_clients.client_course_create, name='client_course_create'),
	path('client/<str:client_id>/courses/<str:course_id>/update/', staff_inactive_clients.client_course_update, name='client_course_update'),
	path('courses/<str:course_id>/', staff_inactive_clients.client_course, name='client_course'),
	path('client/<str:client_id>/courses/<str:course_id>/delete/', staff_inactive_clients.client_course_delete, name='client_course_delete'),

#=====================================================
#=====================================================
#=====================================================


#=====================================================
#===================== Skills ========================
#=====================================================

	path('client/<str:client_id>/skills/create/', staff_inactive_clients.client_skill_create, name='client_skill_create'),
	path('client/<str:client_id>/skills/<str:skill_id>/update/', staff_inactive_clients.client_skill_update, name='client_skill_update'),
	path('skills/<str:skill_id>/', staff_inactive_clients.client_skill, name='client_skill'),
	path('client/<str:client_id>/skills/<str:skill_id>/delete/', staff_inactive_clients.client_skill_delete, name='client_skill_delete'),

#=====================================================
#=====================================================
#=====================================================


#=====================================================
#====================== Jobs =========================
#=====================================================

	path('jobs/explore/', staff_jobs.jobs, name='jobs'),
	path('job/create/', staff_jobs.job_create, name='job_create'),
	path('job/<str:job_id>/update/', staff_jobs.job_update, name='job_update'),
	path('job/<str:job_id>/delete/', staff_jobs.job_delete, name='job_delete'),
	path('job/<str:job_id>/details/', staff_jobs.job_details, name='job_details'),
	path('jobs/clients/applied/', staff_jobs.clients_applied, name='clients_applied'),
	path('jobs/<str:job_id>/clients/applied/', staff_jobs.clients_job_applied, name='clients_job_applied'),
	path('jobs/client/applied/<str:apply_id>/details/', staff_jobs.applied_job_details, name='applied_job_details'),

#=====================================================
#=====================================================
#=====================================================


#=====================================================
#================ Specializations ====================
#=====================================================

	path('specializations/', staff_specializations.specializations, name='specializations'),
	path('specialization/create/', staff_specializations.specialization_create, name='specialization_create'),
	path('specialization/<str:specialization_id>/update/', staff_specializations.specialization_update, name='specialization_update'),
	path('specialization/<str:specialization_id>/delete/', staff_specializations.specialization_delete, name='specialization_delete'),

#=====================================================
#=====================================================
#=====================================================


#=====================================================
#================= Phone Interviews ==================
#=====================================================

	path('submitted_jobs/', staff_interviews.submitted_jobs, name='submitted_jobs'),
	path('phone_interview/', staff_interviews.add_phone_interview, name='add_phone_interview'),
	path('phone_interview/client/<str:client_id>/', staff_interviews.phone_interview, name='phone_interview'),
	path('ended_interviews/', staff_interviews.ended_interviews, name='ended_interviews'),

#=====================================================
#=====================================================
#=====================================================


#=====================================================
#===================== partners ======================
#=====================================================

	path('partners/', staff_partners.partners, name='partners'),
	path('partner/create/', staff_partners.partner_create, name='partner_create'),
	path('partner/<str:partner_id>/update/', staff_partners.partner_update, name='partner_update'),
	path('partner/<str:partner_id>/delete/', staff_partners.partner_delete, name='partner_delete'),

#=====================================================
#=====================================================
#=====================================================


#=====================================================
#======================= PDF =========================
#=====================================================

	path('pdf/mail/<str:mail_id>/view/', staff_pdf.pdf_mail_view, name='pdf_mail_view'),
	path('pdf/mail/<str:mail_id>/download/', staff_pdf.pdf_mail_download, name='pdf_mail_download'),

	path('cv/active/client/<str:client_id>/view/', staff_pdf.pdf_client_cv_view, name='pdf_client_cv_view'),
	path('cv/active/client/<str:client_id>/download/', staff_pdf.pdf_client_cv_download, name='pdf_client_cv_download'),
	
	path('cv/<str:client_id>/view/', staff_pdf.pdf_cv_view, name='pdf_cv_view'),
	path('cv/<str:client_id>/download/', staff_pdf.pdf_cv_download, name='pdf_cv_download'),

	path('pdf/download/', pdf.export_pdf, name='export_pdf'),
#=====================================================
#=====================================================
#=====================================================


#=====================================================
#==================== Charts =========================
#=====================================================
	path('data/jobs_applies/json/', views.jobs_applies_chart, name='jobs_applies_chart'),
	path('data/new_users/json/', views.new_users_chart, name='new_users_chart'),
	path('data/nationalities/json/', views.nationalities_chart, name='nationalities_chart'),
	path('data/resumes/json/', views.resumes_chart, name='resumes_chart'),
	# path('data/active_clients/json/', views.active_clients_chart, name='active_clients_chart'),
	# path('data/all_jobs_applies/json/', views.all_jobs_applies_chart, name='all_jobs_applies_chart'),
	# path('data/available_jobs/json/', views.available_jobs_chart, name='available_jobs_chart'),
	# path('data/inactive_clients/json/', views.inactive_clients_chart, name='inactive_clients_chart'),


#=====================================================
#=====================================================
#=====================================================
]