from django.conf.urls import include
from django.urls import path
from . import views

urlpatterns = [
    path('', include('home.urls')),
    path('app-health-check/', views.health_check, name='health_check'),
]
