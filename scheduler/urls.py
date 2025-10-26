from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),              # ← homepage
    path('generate/', views.generate_schedule, name='generate_schedule'),
]
    