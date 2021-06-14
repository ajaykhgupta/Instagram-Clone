from django.contrib import admin
from .models import Image
# Register your models here.
@admin.register(Image)

class Post_Admin(admin.ModelAdmin):
    list_display = ['id','photo','date']