from django.urls import path
from . import views


urlpatterns = [
    path("Dashboard/", views.major, name="dashboard"),
    path('Admissions/', views.Admissions, name="Admissions"),
    path('Programs/', views.Programs, name="Programs"),
    path('outline/', views.outline, name="outlines"),
]