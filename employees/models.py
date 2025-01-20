from django.db import models
from django.contrib.auth.models import User

# Create your models here.

import uuid
from django.db import models

class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    email = models.EmailField(max_length=355, unique=True)
    phone_number = models.CharField(max_length=25, null=True, blank=True)
    country = models.CharField(max_length=40)
    username = models.CharField(max_length=25, unique=True)
    password = models.CharField(max_length=128)
    confirm_password = models.CharField(max_length=128, null=True, blank=True)
    hire_date = models.DateField(auto_now_add=True)
    profile_picture = models.ImageField(upload_to='employees/', null=True, blank=True)
    reset_token = models.UUIDField(default=uuid.uuid4, unique=True, null=True, blank=True)



# class Employee(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
#     first_name = models.CharField(max_length=25)
#     last_name = models.CharField(max_length=25)
#     email = models.EmailField(max_length=355, unique=True,) 
#     phone_number = models.CharField(max_length=25, null=True, blank=True)
#     country = models.CharField(max_length=40)
#     username = models.CharField(max_length=25, unique=True)
#     password = models.CharField(max_length=128)
#     confirm_password = models.CharField(max_length=128)
#     hire_date = models.DateField(auto_now_add=True)
#     profile_picture = models.ImageField(upload_to='employees/', null=True, blank=True)




class Attendance(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=[
        ('Present', 'Present'),
        ('Absent', 'Absent'),
        ('Late', 'Late')
    ])
    check_in = models.TimeField(null=True, blank=True)
    check_out = models.TimeField(null=True, blank=True)
    


class Payroll(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    allowances = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    deductions = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    net_pay = models.DecimalField(max_digits=10, decimal_places=2)
    payment_date = models.DateField()
    payment_status = models.CharField(
        max_length=10,
        choices=[('Pending', 'Pending'), ('Paid', 'Paid')],
        default='Pending'
    )



class Task(models.Model):
    task_title = models.CharField(max_length=255)
    task_description = models.TextField()
    due_date = models.DateField()
    priority = models.CharField(max_length=20, choices=[('Low', 'Low'), ('Medium', 'Medium'), ('High', 'High')])
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)



class Comment(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='comments')
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

