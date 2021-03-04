from django.shortcuts import render
import random

# Create your views here.
def gensis(request):
	return render(request,"generators/genmain.html")

def password(request):

	strings = list('abcdefghijklmnopqrstuvwxyz')


	if request.GET.get('uppercase'):
		strings.extend('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
	if request.GET.get('Specialcase'):
		strings.extend('!@#$%^&*()')
	if request.GET.get('number'):
		strings.extend('0123456789')

	length = int(request.GET.get('length',12))
	thepassword = ''
	for x in range(length):
		thepassword += random.choice(strings)



	return render(request,'generators/password.html',{'password':thepassword})



