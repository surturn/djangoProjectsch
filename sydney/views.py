from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from sydney.models import Users


def main(request):
    return HttpResponse("<h1>Sydney</h1>")

def base(request):
    template = loader.get_template('base.html')
    return HttpResponse(template.render())

def home(request):
    template = loader.get_template('home.html')
    return HttpResponse(template.render())

def login(request):
    template = loader.get_template('login.html')
    return HttpResponse(template.render())

def register(request):
    template = loader.get_template('register.html')
    return HttpResponse(template.render())

def courses(request):
    template = loader.get_template('Courses.html')
    return HttpResponse(template.render())


def addsuser(request):     # Save data
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        course = request.POST['course']
        password = request.POST['password']

        obj = Users(name=name, email=email, phone=phone, course=course, password=password)
        obj.save()

                                #Data to be displayed
    data = Users.objects.all();
    context = {'data': data}
    return render(request, 'Register.html', context)
