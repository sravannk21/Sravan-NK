from django.db import models

# Create your models here.
class registration_tb(models.Model):
    first_name=models.CharField(max_length=200,default='')
    last_name=models.CharField(max_length=200,default='')
    username=models.CharField(max_length=200,default='')
    phone=models.CharField(max_length=10,default='')
    email=models.CharField(max_length=200,default='')
    password=models.CharField(max_length=200,default='')
    confirm_password=models.CharField(max_length=200,default='')