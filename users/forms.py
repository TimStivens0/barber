from django import forms
from users.models import UserModel


class UserModelForm(forms.ModelForm):
    full_name = forms.CharField(widget=forms.TextInput())
    phone = forms.CharField(widget=forms.TextInput())

    class Meta:
        model = UserModel
        fields = ['full_name', 'phone']
