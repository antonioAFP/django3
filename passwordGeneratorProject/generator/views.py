from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.
def home(request):
	return render(request, 'generator/home.html')

def password(request):
	thepassword = ''
	charset = list('abcdefgklmnopqrstuwxyz')
	length = int(request.GET.get('length'))

	if request.GET.get('uppercase'):
		charset.extend('ABCDEFGKLMNOPQRSTUWXYZ')

	if request.GET.get('special'):
		charset.extend('!@#$%^&*()_+><')

	if request.GET.get('numbers'):
		charset.extend('0123456789')

	for x in range(length):
		thepassword += random.choice(charset)

	return render(request, 'generator/password.html', {'password': thepassword})

def about(request):
	return render(request, 'generator/about.html')
