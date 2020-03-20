from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
import random
def home(request):
	return render(request,'generator/home.html')
def game(request):
	return HttpResponse('This one is a First game you are playing.\n <h1>plz subscribe it!!!!!!</h1>')
def password(request):
	ch=[]
	for i in range(ord('a'),ord('z')+1):
		ch.append(chr(i))
	password=''
	# n=[i for i in range(0,10)]
	leng=request.GET.get('length',12)
	# upper=
	# number=
	# special=
	if request.GET.get('number'):
		ch.extend(list('1234567890'))
	if request.GET.get('uppercase'):
		ch.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
	if request.GET.get('specialcase'):
		ch.extend(list('!@#$%^&*()+_-<>?:";'))

	for i in range(int(leng)):
		password+=random.choice(ch)
	return render(request,'generator/password.html',{'password':password})

def about(request):
	res=''
	for i in range(5):
		for j in range(i,5):
			res+='*'
		res+=' '
	return render(request,'generator/about.html',{'result':res})