from django.contrib import admin
from .models import *

class Created_user(admin.ModelAdmin): 
    readonly_fields = ['created_by']
    
admin.site.register(Student)
admin.site.register(Mark)