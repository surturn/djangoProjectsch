<<<<<<< HEAD
from django import forms
from .models import Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description']

=======
from django.db import models

class MyModel(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
>>>>>>> 60fc96f5085673b32a2bb709a0ca5311e2174ebc
