from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


def major(request):
    return HttpResponse("Hello, world. You're at the polls major.")

def Admissions(request):
    template = loader.get_template('admissions.html')
    return HttpResponse(template.render())
def Programs(request):
    template = loader.get_template('programs.html')
    return HttpResponse(template.render())
def outline(request):
    template = loader.get_template('outline.html')
    return HttpResponse(template.render())


# Create your views here.
