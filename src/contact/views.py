# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.conf import settings
from django.core.mail import send_mail

from .forms import contactForm

# Create your views here.
def contact(request):
	title ='Contact'
	form = contactForm(request.POST or None)
	context ={'title':title, 'form':form,}
	confirm_message =None

	if form.is_valid():
		name=form.cleaned_data['name']
		comment=form.cleaned_data['comment']
		subject='Message from Ditex.com'
		message='%s %s' %(comment, name)
		emailFrom= form.cleaned_data['email']
		emailTo=[settings.EMAIL_HOST_USER]
		send_mail(subject, message, emailFrom,emailTo, fail_silently=True)
		title="Thanks!"
		confirm_message="Thanks for the message."
		form =None
		
	else:
		pass
	context={'title':title, 'form':form, 'confirm_message':confirm_message,}
	template_name='contact.html'
	return render(request, template_name, context)