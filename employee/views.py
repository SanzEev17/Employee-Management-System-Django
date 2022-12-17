from django.shortcuts import render, redirect
from django.contrib import auth
from .models import Project, EmpLeave
from accounts.models import User

# Create your views here.
def dashboard(request):
    if request.user.is_authenticated:
        project = Project.objects.filter(employee=request.user.id)
        leavestatus = EmpLeave.objects.filter(employee = request.user.id)
        contents = {
            'projects' : project,
            'leavestatus' : leavestatus
        }
        return render(request, 'employee/dashboard.html', contents)
    else:
        return redirect('login')

def myprofile(request):
    if request.user.is_authenticated:
        user = User.objects.filter(id=request.user.id)
        contents = {
            'users' : user,
        }
        return render(request, 'employee/myprofile.html', contents)
    else:
        return redirect('login')

def myprojects(request):
    if request.user.is_authenticated:
        project = Project.objects.filter(employee=request.user.id)
        contents = {
            'projects' : project,
        }
        return render(request, 'employee/myprojects.html', contents)
    else:
        return redirect('login')

def eleave(request):
    if request.method == 'POST':
        if request.user.is_authenticated:
            employee = User.objects.filter(id = request.user.id)
            subject = request.POST['subject']
            reason = request.POST['reason']
            start_date = request.POST['start']
            end_date = request.POST['end']
            leave = EmpLeave(employee = employee[0], subject = subject, reason = reason, start_date = start_date, end_date = end_date)
            leave.save()
            return redirect('eleave')
        else:
            return redirect('login')
    return render(request, 'employee/applyleave.html')

def leavestatus(request):
    if request.user.is_authenticated:
        leavestatus = EmpLeave.objects.filter(employee = request.user.id)
        contents = {
            'leavestatus' : leavestatus
        }
        return render(request, 'employee/leavestatus.html', contents)
    return redirect('login')

def submit(request):
    if request.method == 'POST':
        pid = request.POST['pid']
        if request.user.is_authenticated:
            Project.objects.filter(id = pid).update(status = "Submitted")
            return redirect('myprojects')
    
def updateinfo(request):
    if request.method == 'POST':
        first_name = request.POST['firstName']
        last_name = request.POST['lastName']
        email = request.POST['email']
        username = request.POST['username']
        gender = request.POST['gender']
        phone = request.POST['contact']
        address = request.POST['address']
        department = request.POST['dept']
        degree = request.POST['degree']
        if request.user.is_authenticated:
            User.objects.filter(id = request.user.id).update(first_name = first_name, last_name = last_name, email = email, username = username, gender = gender, phone = phone, address=address, department = department, degree = degree)
            return redirect('myprofile')
    