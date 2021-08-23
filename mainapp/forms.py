from django.forms import ModelForm
from .models import Leeds

class LeedForm(ModelForm):
    class Meta:
        model = Leeds
        fields = ['numberPhone', 'fullName','description','teacher']
        