from django.shortcuts import render
from random import *

# Create your views here.

def generator(request):
    return render(request, 'generator/generator.html')

def password(request):
    p=list('abcdefghijklmnopqrstuvwxyz')

    if request.GET.get('uppercase'):
        p.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))

    if request.GET.get('numbers'):
        p.extend(list('0123456789'))

    if request.GET.get('special'):
        p.extend(list('!@#$%^&*()'))

    length = int(request.GET.get('length'))

    genpass=''

    for item in range(length):
        genpass += choice(p)


    return render(request, 'generator/password.html', {'password': genpass})
