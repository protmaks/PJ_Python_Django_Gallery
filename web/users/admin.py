from django.contrib import admin
from .models import Profile, User

@admin.register(Profile)
class FisherAdmin(admin.ModelAdmin):
    list_display = ['user', 'image']
