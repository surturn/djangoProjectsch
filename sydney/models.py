from django.db import models
# Create your models here.
class myuser(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True,blank=False)
    phone = models.IntegerField(null=False, blank=False)
    course = models.CharField(max_length=100)
    password = models.CharField(max_length=100, default='<PASSWORD>')

class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    completed = models.BooleanField(default=False)

