from django.contrib import admin

# Register your models here.
from dataviewer.models import Data, Comment

admin.site.register(Data)
admin.site.register(Comment)