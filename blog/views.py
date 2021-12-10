#from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader #added by me for Templates


# Create your views here.

def tester(request):
	html_template= loader.get_template("test.html")
	context = {}
	context['variable_name'] = 100
	#return HttpResponse('hi my panda pup!')
	return HttpResponse(html_template.render(context,request))