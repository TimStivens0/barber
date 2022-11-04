from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from barber.models import BarberModel


class CBarberModelForm(UserCreationForm):

    class Meta:
        model = BarberModel
        fields = ('time1', 'time2', 'time3', 'time4', 'time5', 'time6', 'time7', 'time8', 'time9', 'time10', 'time11', 'time12')


class ChBarberModelForm(UserChangeForm):

    class Meta:
        model = BarberModel
        fields = ('time1', 'time2', 'time3', 'time4', 'time5', 'time6', 'time7', 'time8', 'time9', 'time10', 'time11', 'time12')
