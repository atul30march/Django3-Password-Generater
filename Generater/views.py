from django.shortcuts import render
import random
def home(request):
  return render(request,'./generater/home.html')

def password(request):

  charectores = list('abcdefghijklmnopqrstuvwxyz')

  if request.GET.get('uppercase'):
    charectores.extend('ABCDEFGHIJKLMNOPQUSTUVWXYZ')

  if request.GET.get('number'):
    charectores.extend('1234567890')

  if request.GET.get('specail'):
    charectores.extend('!@#$%^&*()')

  length = int(request.GET.get('length'))

  thepassword = ''

  for x in range(length):

    thepassword += random.choice(charectores)

  return render(request,'./generater/password.html',{'password':thepassword})


def about(request):
  return render(request,'./generater/about.html')