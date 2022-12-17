from django.db import models
from accounts.models import User

# Create your models here.
class Project(models.Model):
    employee = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    project_name = models.CharField(max_length=30)
    description = models.TextField(max_length=200)
    due_date = models.DateField()
    sub_date = models.DateField(null=True)
    choices = [
        ('Not Submitted', 'Not Submitted'),
        ('Submitted', 'Submitted'),
    ]
    status = models.CharField(max_length=20, choices=choices,default='Not Submitted')
    def __str__(self):
        return self.project_name

class EmpLeave(models.Model):
    employee = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    subject = models.CharField(max_length=50)
    reason = models.TextField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField()
    choices = [
        ('Pending', 'Pending'),
        ('Approved', 'Approve'),
        ('Rejected', 'Reject'),
    ]
    status = models.CharField(max_length=20, choices=choices,default='Pending')
    def __str__(self):
        return self.subject