from django.shortcuts import render, redirect
from django.contrib import auth
from .models import User

# Create your views here.
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password = password)
        
        # print(users)
        # print(user)
        if user is not None:
            users = User.objects.filter(is_employee=True)
            if user in users:
                auth.login(request, user)
                return redirect('dashboard')
            else:
                return redirect('ems/admin')
        else:
            return redirect('login')
    return render(request, 'accounts/login.html')


def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('index')