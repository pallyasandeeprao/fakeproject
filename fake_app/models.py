from django.db import models

# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=100)
    roll=models.IntegerField()
    marks=models.IntegerField()
    avg=models.FloatField()
    email=models.EmailField()
    address=models.CharField(max_length=200)