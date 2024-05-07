from django.shortcuts import render

# Create your views here.

def logo(request):
    return render(request, 'users/logo.html')

def show_homepage(request):
    return render(request, 'users/index.html')

def menu(request):
    return render(request,'users/menu.html')

def about(request):
    return render(request,'users/about.html')