from textwrap import indent
from django.shortcuts import render,redirect
from matplotlib.style import context
from .form import *
from .models import *
from django.http import HttpResponse, JsonResponse
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
import json   
from django.views.generic.list import ListView
from django.db.models import Sum
from django.core import serializers


@login_required()
def show(request):
    stud = Student.objects.all()
    marks1 = Mark.objects.all()
    context = {'stu':stud,'mar':marks1}
    return render(request, 'show_details.html', context)  
@login_required()
def home(request):
    return render(request, "home.html")
@login_required() 
def web(request):
    return render(request, "web.html")


def Form_in(request):
    
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username =username, password = password)
        if user is not None:
            login(request,user)
            return redirect('details')
        else:
            
            form = AuthenticationForm()
            messages.info(request, 'username or password is incorrect')
            return render(request,'log_in.html',{'form':form})
     
    else:
        form = AuthenticationForm()
        return render(request, 'log_in.html', {'form':form})
@login_required()     
def Form_out(request):
    logout(request)
    return redirect('Form_in')

@login_required(redirect_field_name='F',login_url='Form_in')
def add_form(request):

    form = Student_form(request.POST or None, request.FILES or None)
    
    if form.is_valid():
        form.save()
        
    return render(request, 'add_student.html', {'data':form})
    
@login_required() 
def add_marks(request):

    form1 = Mark_form(request.POST or None, request.FILES or None)
    
    if form1.is_valid():
        if form1.is_valid():
            form1 = form1.save(commit = False)
            form1.created_by = (request.user).username
            form1.save()  
    return render(request, 'add_marks.html', {'mark':form1})  

@login_required()  
def show_mark(request,id):
   
    mar = Mark.objects.filter(student_num_id = id).values()
    return render(request, 'show_mark.html',{'mar':mar})
    
@login_required()  
def update_stu(request,id):
    mar = Student.objects.get(id = id)
    form2 = Student_form(request.POST or None, request.FILES or None, instance = mar) 
    if form2.is_valid():
        form2.save()  
    return render(request, 'update_stu.html',{'form':form2})
    
@login_required()   
def update_mark(request,id):

    mar1 = Mark.objects.get(id = id)
    mark1 = Mark_form(request.POST or None, request.FILES or None, instance = mar1)
    if mark1.is_valid():
        mark1 = mark1.save(commit = False)
        mark1.updated_by = (request.user).username
        mark1.save() 
        return redirect('/') 
    return render(request, 'update_mark.html',{'mark1':mark1})

@login_required() 
def del_student(request,id):

    stu = Student.objects.get(id = id)
    stu.delete()
    return HttpResponse("deleted")

@login_required()
def del_mark(request,id):

    mark_del = Mark.objects.get(id = id)
    mark_del.delete()
    return HttpResponse("mark deleted")
def json_view(request,id):

    stu_qs = Student.objects.filter(id = id).values()
    student_json = Mark.objects.filter(student_num_id = id).values('subject', 'mark')
    sum_total = Mark.objects.filter(student_num_id = id).aggregate(Total = Sum('mark'))
    final_json =  list(stu_qs) + list(student_json) + list(sum_total.items())
    data = json.dumps(final_json, default = str, indent =6)
    print(sum_total)
    return HttpResponse(data, content_type='application/json')


class Json_show(ListView):
    
    model = Mark
    def render_to_response(self, *args, **kwargs):
        stu_qs = Student.objects.all().values()
        student_json = Mark.objects.all().values().order_by('student_num_id')
        #sum_total = Mark.objects.all().aggregate(Sum('mark'))
        #print(sum_total)
        final_json = list(stu_qs) + list(student_json)
        print(final_json)
        data = json.dumps(final_json, default = str, indent =6)
        print(data)
        return HttpResponse(data, content_type = 'application/json')
