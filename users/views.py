from django.shortcuts import render

# Create your views here.

def logo(request):
    return render(request, 'users/logo.html')

def show_homepage(request):
    return render(request, 'users/index.html')