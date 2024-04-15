from django.db import models
# Create your models here.
class Users(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True,blank=False)
    phone = models.IntegerField(max_length=15)
    course = models.CharField(max_length=100)

