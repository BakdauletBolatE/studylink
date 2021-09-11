from django.shortcuts import render
from .models import Block, Teacher, Title,ClicksSocial
from .forms import LeedForm
import requests
from django.shortcuts import redirect
import json
import telebot
from django.conf import settings
from django.contrib import messages

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

def teanegerView(request):

    teachers = Teacher.objects.all()
    data = {
        'teachers':teachers,
    }

    return render(request,'mainapp/1316.html',data)

def intensiveView(request):

    teachers = Teacher.objects.all()
    data = {
        'teachers':teachers,
    }

    return render(request,'mainapp/intensive.html',data)

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
    form = LeedForm()
    data = {    
        'teacher': teacher,
        'form':form
    }

    return render(request,'mainapp/teacherProfile.html',data)


def leedAddView(request):


    if request.method == 'POST':
        form = LeedForm(request.POST)

        data = {
            "fullName": request.POST.get('fullName'),
            "phone": request.POST.get('numberPhone'),
            "description": request.POST.get('description'),
            "teacher": request.POST.get('teacherName')
        }

        dataJson = json.dumps(data)
        print(dataJson) 
        headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}

        res = requests.post('https://studylink.t8s.ru/Api/V2/AddStudyRequest/',data=dataJson,headers=headers)

        # print(res)

        

        if form.is_valid():
            TOKEN = settings.TELEGRAM_BOT_AUTH_KEY
            GROUPID = settings.GROUPID
            form.save(commit=False)
            form.teacher = request.POST.get('teacher')
            created_lead = form.save()
            messages.info(request, created_lead.fullName)
            if created_lead.fullName is None:
                fullName = ""
            else:
                fullName = f"Имя: {created_lead.fullName}"

            if created_lead.teacher is None:
                teacherName = ''
            else:
                teacherName = f"Учитель: {created_lead.teacher.name}"
            message_text = f"""У нас новая заявка №{created_lead.id}\nТип заявки - {created_lead.description}\n{fullName}\nТелефон номера: {created_lead.numberPhone}\n{teacherName}"""
            bot = telebot.TeleBot(TOKEN, parse_mode=None)

            bot.send_message(GROUPID,message_text)
            
        else:
            print('Ошибка')
            messages.info(request, "При отправка ошибка")
            return redirect('thankYouUrl')

        return redirect('thankYouUrl')


def one_page_view(request):
    return render(request, 'one-page.html')

def thank_you_page_view(request):

    return render(request,'thank-you.html')



def instagram_redirect(request):
    
    click_social = ClicksSocial.objects.create(
        category_name="instagram"
    )
    click_social.save()

    TOKEN = settings.TELEGRAM_BOT_AUTH_KEY

    bot = telebot.TeleBot(TOKEN, parse_mode=None)

    message_text = f"""У нас новый клик по сайту №{click_social.id}\nТип клика - {click_social.category_name}"""

    bot.send_message(settings.PRIVATE_GROUPID,message_text)

    return redirect('https://www.instagram.com/studylink_sever_shymkent/?hl=ru')


def whatsapp_redirect(request):
    
    click_social = ClicksSocial.objects.create(
        category_name="whatsapp"
    )
    click_social.save()

    TOKEN = settings.TELEGRAM_BOT_AUTH_KEY

    bot = telebot.TeleBot(TOKEN, parse_mode=None)

    message_text = f"""У нас новый клик по сайту №{click_social.id}\nТип клика - {click_social.category_name}"""

    bot.send_message(settings.PRIVATE_GROUPID,message_text)

    return redirect('https://wa.me/message/J36DWARSI7ZJP1')


def facebook_redirect(request):
    
    click_social = ClicksSocial.objects.create(
        category_name="facebook"
    )
    click_social.save()

    TOKEN = settings.TELEGRAM_BOT_AUTH_KEY

    bot = telebot.TeleBot(TOKEN, parse_mode=None)

    message_text = f"""У нас новый клик по сайту №{click_social.id}\nТип клика - {click_social.category_name}"""

    bot.send_message(settings.PRIVATE_GROUPID,message_text)

    return redirect('https://www.facebook.com/study.link.37')

def telegram_redirect(request):
    
    click_social = ClicksSocial.objects.create(
        category_name="telegram"
    )
    click_social.save()

    TOKEN = settings.TELEGRAM_BOT_AUTH_KEY

    bot = telebot.TeleBot(TOKEN, parse_mode=None)

    message_text = f"""У нас новый клик по сайту №{click_social.id}\nТип клика - {click_social.category_name}"""

    bot.send_message(settings.PRIVATE_GROUPID,message_text)

    return redirect('https://t.me/studylinksever')


        