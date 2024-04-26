from django import forms
<<<<<<< HEAD
=======

>>>>>>> 60fc96f5085673b32a2bb709a0ca5311e2174ebc
from .models import Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description']

