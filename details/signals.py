from django.db.models.signals import post_save, pre_save, pre_delete
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.core.mail import send_mail
from .models import *



@receiver(post_save, sender=Student)
def create_profile(sender, instance, created, **kwargs):
    if created:
       print("created")

@receiver(pre_save, sender=Mark)
def saveprofile(sender, instance, **kwargs):
    if instance.id is None:
        print('pre saved')
    else:
        global mark1
        mark1 = Mark.objects.get(id = instance.id)

@receiver(post_save, sender=Mark)
def save_profile(sender, instance, **kwargs):
    
    print('saved')
    ob = Mark.objects.filter(id = instance.id).values('student_num__mail')
    mail_qs = ob[0]['student_num__mail']
    send_mail('update', 'your {} mark has updated to {}'.format( instance.subject,instance.mark), 'cmadiam@abc.com', [mail_qs])

@receiver(pre_delete, sender=Mark)
def Del_profile(instance, **kwargs):
    print("deleted")
    ob = Mark.objects.filter(id = instance.id).values('student_num__mail')
    mail_qs = ob[0]['student_num__mail']
    print(ob)
    send_mail('deleted', 'your {} mark has deleted'.format(instance.subject), 'cmadiam@abc.com', [mail_qs])