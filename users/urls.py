from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    path('', views.logo, name="logo"),
    path('home', views.show_homepage, name="show_homepage"),
    path('menu', views.menu, name="menu"),
    path('about', views.about, name="about"),
    path('contact', views.contact, name="contact"),
    path('employee-of-the-month', views.employee, name="employee"),
    path('franchise', views.franchise, name="franchise"),
]
