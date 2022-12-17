from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    email = models.EmailField(unique=True)
    dob = models.DateField(null=True)
    gender = models.CharField(max_length=20, null=True)
    phone = models.CharField(max_length=14, null=True)
    address = models.CharField(max_length=50, null=True)
    department = models.CharField(max_length=30, null=True)
    degree = models.CharField(max_length=20, null=True)
    salary = models.CharField(max_length=20, null=True)
    is_employee = models.BooleanField(default=True)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', default='no.jpg')
    def __str__(self):
        return self.first_name+" "+self.last_name