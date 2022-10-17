from django.db.models.signals import post_save, pre_delete
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.core.mail import send_mail
from .models import *


@receiver(post_save, sender=Student)
def create_profile(sender, instance, created, **kwargs):
    if created:
       print("created")
       Mark.objects.create(student_num=instance)
        

@receiver(post_save, sender=Mark)
def save_profile(sender, instance, **kwargs):
        print('saved')
        instance.student_num.save()
        send_mail('update', 'your mark is {} updated'.format(instance.mark), ['cmadiam@abc.com'], [instance.mail])
