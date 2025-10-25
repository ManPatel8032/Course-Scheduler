from django.urls import path
from . import views

urlpatterns = [
    path('generate/', views.generate_schedule, name='generate_schedule'),
]
