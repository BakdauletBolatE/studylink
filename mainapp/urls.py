from django.http.response import HttpResponse
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('one-page-view/',views.one_page_view),
    path('ielts/', views.ieltsView),
    path('teanegers/', views.teanegerView),
    path('intencive/', views.intensiveView),
    path('thank-you-page/',views.thank_you_page_view, name="thankYouUrl"),
    path('teacher/<int:pk>', views.teacherView, name='teacherUrl')
]


urlpatterns += [
    path('instagram-re/', views.instagram_redirect),
    path('whatsapp-re/', views.whatsapp_redirect),
    path('telegram-re/', views.telegram_redirect),
    path('facebook-re/', views.facebook_redirect),
]

urlpatterns += [
    path('leed/add/',views.leedAddView, name="addLead"),
]