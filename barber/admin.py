from django.contrib import admin
from .models import BarberModel


@admin.register(BarberModel)
class BarberModelAdmin(admin.ModelAdmin):
    pass
