from django.shortcuts import render
from .models import Contact

def index(request):
    return render(request, 'pages/index.html')


def about(request):
    return render(request, 'pages/about.html')
    
def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        address = request.POST['address']
        message = request.POST['message']
        contact = Contact(name = name, email =email, phone=phone, address= address, message=message)
        contact.save()
    return render(request, 'pages/contact.html')