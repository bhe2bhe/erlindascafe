from django.contrib import admin
from .models import Menu, Employee, Quote


admin.site.site_header = "Erlinda's Cafe" 
admin.site.site_title = "Private"
admin.site.index_title = "Nicole's Admin Page"

admin.site.register(Menu)
admin.site.register(Employee)
admin.site.register(Quote)