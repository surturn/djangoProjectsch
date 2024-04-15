from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template import loader
from django.views.decorators.csrf import csrf_exempt

from sydney.models import myuser
from .forms import TaskForm


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


@csrf_exempt
def addsuser(request):     # Save data
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        course = request.POST['course']
        password = request.POST['password']

        obj = myuser(name=name, email=email, phone=phone, course=course, password=password)
        obj.save()

                                #Data to be displayed
    data = myuser.objects.all();
    context = {'data': data}
    return render(request, 'Register.html', context)


@csrf_exempt
def add_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Register')  # Redirect to a view that displays all tasks
    else:
        form = TaskForm()
    return render(request, 'Register.html', {'form': form})

