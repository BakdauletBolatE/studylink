from django.shortcuts import render
from .models import Block, Title
# Create your views here.


def index(request):

    title = Title.objects.get(category__name="main")
    blocks = Block.objects.filter(category__name="main")
    data = {
        'title': title,
        'blocks': blocks
    }
    return render(request,'mainapp/index.html',data)