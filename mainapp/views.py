from django.shortcuts import render
from .models import Block, Teacher, Title
# Create your views here.


def index(request):

    title = Title.objects.get(category__name="main")
    blocks = Block.objects.filter(category__name="main")
    teachers = Teacher.objects.all()
    data = {
        'title': title,
        'teachers':teachers,
        'blocks': blocks
    }
    return render(request,'mainapp/index.html',data)

def ieltsView(request):

    title = Title.objects.get(category__name="ielts")
    blocks = Block.objects.filter(category__name="main")
    teachers = Teacher.objects.all()
    data = {
        'title': title,
        'blocks': blocks,
        'teachers':teachers,
    }
    return render(request,'mainapp/ielts.html',data)

def teacherView(request, pk):

    teacher = Teacher.objects.get(id=pk)

    data = {
        'teacher': teacher
    }

    return render(request,'mainapp/teacherProfile.html',data)