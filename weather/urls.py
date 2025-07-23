from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Make sure you have a view named `home`
]
