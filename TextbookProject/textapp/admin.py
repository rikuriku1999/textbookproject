from django.contrib import admin
from .models import Textbookmodel ,Commentmodel ,Usermodel

# Register your models here.

admin.site.register(Commentmodel)

admin.site.register(Textbookmodel)

admin.site.register(Usermodel)


