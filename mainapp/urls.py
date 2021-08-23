from django.http.response import HttpResponse
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('ielts/', views.ieltsView),
    path('teanegers/', views.teanegerView),
    path('intencive/', views.intensiveView),
    path('thank-you-page/',views.thankYouPageView, name="thankYouUrl"),
    path('teacher/<int:pk>', views.teacherView, name='teacherUrl')
]

urlpatterns += [
    path('leed/add/',views.leedAddView, name="addLead"),
]