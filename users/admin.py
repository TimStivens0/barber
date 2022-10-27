from django.contrib import admin
from .models import UserModel


@admin.register(UserModel)
class UserModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'full_name', 'phone']
    list_display_links = ['id', 'full_name', 'phone']
