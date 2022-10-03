from django.db import models
from django.contrib.auth.models import User
from django_currentuser.middleware import ( get_current_user, get_current_authenticated_user)

class Student(models.Model):

    name = models.CharField(max_length = 20)
    roll_no = models.IntegerField()
    profile = models.ImageField(upload_to = "images/", null=True)
    
    def __str__(self):
    	return "{}".format(self.id)
    
    
class Mark(models.Model):
    
    student_num = models.ForeignKey(Student, null = True, on_delete = models.CASCADE)
    subject = models.CharField(max_length = 20)
    mark = models.IntegerField()
    Created_at = models.DateTimeField(auto_now_add=True)
    Modified_at = models.DateTimeField(auto_now=True)
    #created_by = CurrentUserField()
    #updated_by = CurrentUserField(on_update=True)


    
    def __str__(self):
    	return "{}".format(self.student_num)    