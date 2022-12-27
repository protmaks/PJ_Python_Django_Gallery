from django.contrib import admin
from .models import Image


@admin.register(Image)
class FisherAdmin(admin.ModelAdmin):
    list_display = ['title', 'date_posted', 'author']