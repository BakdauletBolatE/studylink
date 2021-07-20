from django.http.response import HttpResponse
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('ielts/', views.ieltsView),
]