from django.http import HttpResponse
from django.shortcuts import render
from faker import Faker
from.models import Student
# Create your views here.
#pip install faker
def display(request):
  for i in range(10):
     fake=Faker()
     name=fake.name()
     roll=fake.random.randint(1,100)
     marks=fake.random.randint(60,100)
     avg=fake.random.uniform(60,100)
     email=fake.email()
     address=fake.address()
     z=Student(name=name,roll=roll,marks=marks,avg=avg,email=email,address=address)
     z.save()
  return HttpResponse('data added')
