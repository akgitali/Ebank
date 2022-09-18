from django.db import models

# Create your models here.


class Account(models.Model):
    acno=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=50)
    address=models.CharField(max_length=100)
    contectno=models.CharField(max_length=12)
    email=models.EmailField(max_length=50)
    panno=models.CharField(max_length=10)
    aadharno=models.CharField(max_length=12)
    balance=models.IntegerField()
    password=models.CharField(max_length=20)