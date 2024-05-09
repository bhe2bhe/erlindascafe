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

def contact(request):
    return render(request,'users/contact.html')

def employee(request):
    return render(request,'users/employee.html')

def franchise(request):
    return render(request,'users/franchise.html')