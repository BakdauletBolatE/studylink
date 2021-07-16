from django.contrib import admin
from .models import PageCategory, Title, Block
# Register your models here.


admin.site.register(PageCategory)
admin.site.register(Block)
admin.site.register(Title)

