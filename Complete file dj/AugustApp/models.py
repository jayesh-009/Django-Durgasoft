from django.db import models

# Create your models here.

class Employee(models.Model):
    eno=models.IntegerField()
    ename=models.CharField(max_length=30)
    esal=models.FloatField()
    eaddr=models.CharField(max_length=30)

class Student(models.Model):
    name=models.CharField(max_length=30)
    marks=models.IntegerField()

class Stud(models.Model):

    name=models.CharField(max_length=30)
    marks=models.IntegerField()

    
class Movie(models.Model):

    rdate=models.IntegerField()
    moviename=models.CharField(max_length=30)
    hero=models.CharField(max_length=30)
    heroine=models.CharField(max_length=30)
    rating=models.IntegerField()







    
