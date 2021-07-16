from django.http.response import HttpResponse
from django.urls import path
from . import views
from amocrm.v2 import tokens, Contact
def testView(request):

    contact = Contact.objects.get(query="Тест")
    print(contact.first_name)
    print(contact.company.name)
    print(contact.created_at)

    contact.last_name = "Новое"
    contact.tags.append("new")
    contact.notes.objects.create(text="Примечание")

    contact.save()
    print(tokens)
    return HttpResponse('hello')


urlpatterns = [
    path('hello/',testView),
    path('', views.index)
]