from django.db import models
class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True,blank=False)
class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    completed = models.BooleanField(default=False)
# Create your models here.
