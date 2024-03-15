from django.db import models

# Create your models here.
class login(models.Model):
    name = models.CharField(max_length=40)
    password = models.CharField(max_length=8)

class Survey(models.Model):
    text = models.TextField(default=None)

class Sign(models.Model):
    username=models.CharField(max_length=30)
    email=models.EmailField(max_length=20)
    password=models.CharField(max_length=10)
    cnfpass=models.CharField(max_length=10)

class Client(models.Model):
    com_name=models.CharField(max_length=30)
    location=models.EmailField(max_length=20)
    duration=models.CharField(max_length=20)
    services=models.CharField(max_length=20)

class Enquiry(models.Model):
    enq_name=models.CharField(max_length=30)
    enq_email=models.EmailField(max_length=20)
    enq_phone=models.CharField(max_length=20)
    enq_location=models.CharField(max_length=20)
    enq_service=models.CharField(max_length=20)