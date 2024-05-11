from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    path('', views.logo, name="logo"),
    path('home', views.show_homepage, name="show_homepage"),
    path('admin-login', views.admin_login, name='admin-login'),
    path('menu', views.menu, name="menu"),
    path('menu/delete/<int:item_id>/', views.delete_menu_item, name='delete_menu_item'),
    path('menu/delete_confirmation/<int:item_id>/', views.delete_confirmation, name='delete_confirmation'),
    path('about', views.about, name="about"),
    path('contact', views.contact, name="contact"),
    path('employee-of-the-month', views.employee, name="employee"),
    path('franchise', views.franchise, name="franchise"),
    path('nicole', views.nicole, name="nicole"),    
    path('logout/', views.logout_view, name='logout'),
]
