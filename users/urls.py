from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    path('', views.logo, name="logo"),
    path('home', views.show_homepage, name="show_homepage")
]
