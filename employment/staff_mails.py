from django.shortcuts import render, redirect
from .models import *
from .forms import *
from .client_models import *
from .filters import ActiveClientsFilter
from .decorators import admin_only
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator


#=====================================================
#====================== Messages ========================
#=====================================================

#-------------------- Inbox ------------------------
@login_required(login_url='login')
@admin_only
def mail_inbox(request):
	main_menu = 'mail'
	sub_menu = 'inbox'
	
	all_replays = Sent_Mail_Replay.objects.all().exclude(is_admin=1).order_by('-date')
	pagination = Paginator(all_replays, 12)
	page = request.GET.get('page')
	all_replays = pagination.get_page(page)
	count = len(all_replays)
	context = {'title':'Inbox', 'all_replays':all_replays,
				'sub_menu':sub_menu, 'count':count,
				'main_menu':main_menu}
	
	return render(request, 'employer/en/mails/inbox.html', context)
#-----------------------------------------------------


#-------------------- Send Mail ----------------------
@login_required(login_url='login')
@admin_only
def send_mail(request, client_id):
	main_menu = 'mail'
	sub_menu = 'send_message'
	
	selected_client = User.objects.get(id=client_id)
	
	if request.method == 'POST':
		title = request.POST['title']
		message = request.POST['message']
		receiver_mail = Mail(receiver=selected_client, title=title, message=message)
		if receiver_mail:
			receiver_mail.save()
		sender_mail = Sent_Mail(mail_id=receiver_mail.mail_id, receiver=selected_client, title=title, message=message)
		if sender_mail:
			sender_mail.save()
			return redirect('sent_mails')

	context = {'title':'Send Message', 'selected_client':selected_client, 
				'main_menu':main_menu, 'sub_menu':sub_menu}

	return render(request, 'employer/en/mails/send_mail.html', context)
#-----------------------------------------------------

#------------------ Create Client --------------------
@login_required(login_url='login')
@admin_only
def send_mail_client_id(request):
	main_menu = 'mail'
	sub_menu = 'send_message'

	if request.method == 'POST':
		return redirect('send_mail', request.POST['client_id'])

	context = {'title':'Send a Message',
			   'main_menu':main_menu, 'sub_menu':sub_menu}

	return render(request, 'employer/en/mails/send_mail_client_id.html', context)
#-----------------------------------------------------

#------------------- Sent Messages ----------------------
@login_required(login_url='login')
@admin_only
def sent_mails(request):
	main_menu = 'mail'
	sub_menu = 'sent_mails'
	
	all_mails = Sent_Mail.objects.filter(is_trash=0).order_by('-date_sent').all()
	mails_count = all_mails.count()

	pagination = Paginator(all_mails, 12)
	page = request.GET.get('page')
	all_mails = pagination.get_page(page)

	context = {'title':'Sent Messages', 'all_mails':all_mails, 'mail_nav':'sent',
			'mails_count':mails_count,
			'main_menu':main_menu, 'sub_menu':sub_menu}

	return render(request, 'employer/en/mails/sent.html', context)
#-----------------------------------------------------

#------------------ Trash Messages ----------------------
@login_required(login_url='login')
@admin_only
def trash_sent_mails(request):
	main_menu = 'mail'
	sub_menu = 'trash_mails'
	
	all_mails = Sent_Mail.objects.filter(is_trash=1).order_by('-date_sent').all()
	mails_count = all_mails.count()

	pagination = Paginator(all_mails, 12)
	page = request.GET.get('page')
	all_mails = pagination.get_page(page)

	context = {'title':'Trash Messages', 'all_mails':all_mails, 'mail_nav':'trash',
			'mails_count':mails_count,
			'main_menu':main_menu, 'sub_menu':sub_menu}

	return render(request, 'employer/en/mails/sent.html', context)
#-----------------------------------------------------

#--------------- Read Sent Messages ---------------------
@login_required(login_url='login')
@admin_only
def read_sent_mail(request, mail_id):
	main_menu = 'mail'
	
	mails_unread_count = Sent_Mail.objects.filter(is_trash=0).all().count()
	selected_mail = Sent_Mail.objects.get(mail_id=mail_id)
	all_replays = Sent_Mail_Replay.objects.filter(mail=selected_mail).all()
	
	if selected_mail.is_trash == '1':
		sub_menu = 'trash_mails'
	else:
		sub_menu = 'sent_mails'

	if request.method == 'POST':
		message = request.POST['message']
		receiver_mail_replay = Mail_Replay(sender='Support',
			mail=Mail.objects.get(mail_id=mail_id),
			message=message, is_admin=1)
		if receiver_mail_replay:
			receiver_mail_replay.save()
		sender_mail_replay = Sent_Mail_Replay(replay_id=receiver_mail_replay.replay_id,
			sender='Support', mail=Sent_Mail.objects.get(mail_id=mail_id),
			message=message, is_admin=0)
		if sender_mail_replay:
			sender_mail_replay.save()
			return redirect('read_sent_mail', mail_id)
	context = {'title':'{}'.format(selected_mail.title), 'selected_mail':selected_mail, 
				'mails_unread_count':mails_unread_count, 'all_replays':all_replays,
				'main_menu':main_menu, 'sub_menu':sub_menu}
				
	return render(request, 'employer/en/mails/mail_read.html', context)
#-----------------------------------------------------

#--------------- Sent Messages Trash --------------------
@login_required(login_url='login')
@admin_only
def sent_mail_trash(request, mail_id):
	selected_mail = Sent_Mail.objects.get(mail_id=mail_id)
	selected_mail.is_trash = 1
	
	if selected_mail:
		selected_mail.save()
		
		return redirect('trash_sent_mails')
#-----------------------------------------------------

#-------------- Send Mail to Inbox -------------------
@login_required(login_url='login')
@admin_only
def to_inbox(request, mail_id):
	main_menu = 'mail'
	sub_menu = 'sent_mails'
	
	selected_mail = Sent_Mail.objects.get(mail_id=mail_id)
	formset = Sent_Mail(mail_id=mail_id, receiver=selected_mail.receiver, 
	sender=selected_mail.sender, message=selected_mail.message, 
	date_sent=selected_mail.date_sent, title=selected_mail.title, 
	is_trash=0)
	
	if formset:
		formset.save()
		
		return redirect('sent_mails')
#-----------------------------------------------------


#-------------------- Send Mail ----------------------
@login_required(login_url='login')
@admin_only
def send_message_group(request):
	main_menu = 'mail'
	sub_menu = 'send_message_group'

	all_cvs = Client_CV.objects.all()
	# all_clients_count = all_cvs.count()
	all_clients_filter = ActiveClientsFilter(request.POST, queryset=all_cvs)
	all_cvs = all_clients_filter.qs
	
	if request.method == 'POST':
		all_clients_filter = ActiveClientsFilter(request.POST, queryset=all_cvs)
		all_cvs = all_clients_filter.qs
		title = request.POST['title']
		message = request.POST['message']
		for selected_client in all_cvs:
			receiver_mail = Mail(receiver=selected_client.client, title=title, message=message)
			if receiver_mail:
				receiver_mail.save()
			sender_mail = Sent_Mail(mail_id=receiver_mail.mail_id, receiver=selected_client.client, 
									title=title, message=message)
			if sender_mail:
				sender_mail.save()
		return redirect('send_message_group')

	context = {'title':'Send Message', 'all_clients_filter':all_clients_filter, 
				'main_menu':main_menu, 'sub_menu':sub_menu}

	return render(request, 'employer/en/mails/send_message_group.html', context)
#-----------------------------------------------------


#-------------------- Replays ------------------------
@login_required(login_url='login')
@admin_only
def mail_replays(request):
	main_menu = 'mail'
	sub_menu = 'replays'
	
	# all_mails = Sent_Mail.objects.filter(receiver=request.user).all()
	all_replays = Sent_Mail_Replay.objects.filter(is_admin=1).order_by('-date').all()
	# mails_unread_count = Sent_Mail.objects.filter(receiver=request.user).filter(is_trash=0).all().count()
	pagination = Paginator(all_replays, 12)
	page = request.GET.get('page')
	all_replays = pagination.get_page(page)
	context = {'title':'Replays', 'all_replays':all_replays, 
				'sub_menu':sub_menu,
				'main_menu':main_menu}
	
	return render(request, 'employer/en/mails/replays.html', context)
#-----------------------------------------------------



#------------------- Mail Replay ---------------------
# @login_required(login_url='login')
# @admin_only
# def sent_mail_replay(request, mail_id):
# 	main_menu = 'mail'
	
# 	selected_message = Sent_Mail.objects.get(id=mail_id)
	
# 	if request.method == 'POST':
# 		message = request.POST['message']
# 		receiver_mail_replay = Mail_Replay(sender='Excelent Solutions', mail=Mail.objects.get(mail_id=mail_id), message=message)
# 		if receiver_mail_replay:
# 			receiver_mail_replay.save()
# 		sender_mail = Sent_Mail_Replay(replay_id=receiver_mail_replay.replay_id, sender='Excelent Solutions', mail=Sent_Mail.objects.get(mail_id=mail_id), message=message)
# 		if sender_mail:
# 			sender_mail_replay.save()
# 			return redirect('sent_mails')

# 	context = {'title':'Send Message', 'selected_message':selected_message, 'main_menu':main_menu}

# 	return render(request, 'employer/en/mails/send_mail.html', context)
#-----------------------------------------------------
#=====================================================
#=====================================================
#=====================================================