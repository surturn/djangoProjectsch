from django.db import models
class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True,blank=False)
<<<<<<< HEAD
class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    completed = models.BooleanField(default=False)
=======

>>>>>>> 60fc96f5085673b32a2bb709a0ca5311e2174ebc
# Create your models here.
