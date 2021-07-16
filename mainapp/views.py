from django.shortcuts import render
from .models import Title
# Create your views here.


def index(request):

    title = Title.objects.get(category__name="main")
    
    return render(request,'mainapp/index.html',{'title': title})