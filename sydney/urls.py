from django.urls import path

from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('Home/', views.home, name='home'),
    path('Login/', views.login, name='login'),
    path('Courses/', views.courses, name='courses'),
    path('Register/', views.register, name='register'),
    path('base/', views.base, name='base'),
    path('adduser', views.addsuser, name='adduser'),
    path('add_task', views.add_task, name='add_task'),
]