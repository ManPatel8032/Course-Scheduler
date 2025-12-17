from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),              
    path('generate/', views.generate_schedule, name='generate_schedule'),
]
