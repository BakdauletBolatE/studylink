from django.http.response import HttpResponse
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('ielts/', views.ieltsView),
    path('teanegers/', views.teanegerView),
    path('intencive/', views.intensiveView),
    path('teacher/<int:pk>', views.teacherView, name='teacherUrl')
]