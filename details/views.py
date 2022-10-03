from django.shortcuts import render,redirect
from .form import *
from .models import *
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages

def show(request):

    stud = Student.objects.all()
    marks1 = Mark.objects.all()
    context = {'stu':stud,'mar':marks1}
    return render(request, 'show_details.html', context)  

def home(request):
    return render(request, "home.html")
    
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
        
def Form_out(request):
    logout(request)
    return redirect('Form_in')


def add_form(request):

    form = Student_form(request.POST or None, request.FILES or None)
    
    if form.is_valid():
        form.save()
        
    return render(request, 'add_student.html', {'data':form})
    
    
def add_marks(request):

    form1 = Mark_form(request.POST or None, request.FILES or None)
    
    if form1.is_valid():
        form1.save()
        
    return render(request, 'add_marks.html', {'mark':form1})  

    
def show_mark(request,id):

    mar = Mark.objects.filter(student_num_id = id).values()
    return render(request, 'show_mark.html',{'mar':mar})
    return redirect('show')
    
    
def update_stu(request,id):

    mar = Student.objects.get(id = id)
    form2 = Student_form(request.POST or None, request.FILES or None, instance = mar) 
    if form2.is_valid():
        form2.save()  
    return render(request, 'update_stu.html',{'form':form2})
    
    
def update_mark(request,id):

    mar1 = Mark.objects.get(id = id)
    mark1 = Mark_form(request.POST or None, request.FILES or None, instance = mar1) 
    print(mark1)
    if mark1.is_valid():
        mark1.save()  
    return render(request, 'update_mark.html',{'mark1':mark1})
    return redirect('/show/')  

    
    
def del_student(request,id):

    stu = Student.objects.get(id = id)
    stu.delete()
    return HttpResponse("deleted")
    
def del_mark(request,id):

    mark_del = Mark.objects.get(id = id)
    mark_del.delete()
    return HttpResponse("mark deleted")