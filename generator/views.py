from django.shortcuts import render
import random

def home(request):
    return render(request, 'home.html')


def password(request):

    characters = list('abcdefghijklmnopqrstuvwxyz')
    # varaible where store character
    generated_password = ''

    # get query string and convert
    length = int(request.GET.get('length'))

    # Validation
    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    
    if request.GET.get('special'):
        characters.extend(list('~`!@#$%^-\/&*_+'))

    if request.GET.get('number'):
        characters.extend(list('1234567890'))

    # Generate random password
    for x in range(length):
        generated_password += random.choice(characters)

    return render(request, 'password.html', {'password': generated_password})


def about(request):
    return render(request, 'about.html')