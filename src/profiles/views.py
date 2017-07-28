# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render


# Create your views here.
def home(request):
	context={}
	template_name= 'home.html'
	return render(request, template_name, context)

def about(request):
	context={}
	template_name= 'about.html'
	return render(request, template_name, context)
	
