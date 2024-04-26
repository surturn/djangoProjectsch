from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from dashboard.models import Student
from .forms import TaskForm

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
def save(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')

    obj = Student(name= name , email= email)
    obj.save()


    data =Student.objects.all();
    context = {'data': data}
    return render(request, 'outline.html', context)

def students(request):
    if request.method == 'POST':
            form = TaskForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('Register')
            else:
                form = TaskForm()
    return render(request, 'outline.html', {'form': form})
    # Create your views here.
