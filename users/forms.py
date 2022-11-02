from django import forms
from users.models import UserModel


class UserModelForm(forms.ModelForm):
    full_name = forms.CharField(widget=forms.TextInput(attrs={
         'placeholder': 'Full Name'
    }), label=False)
    phone = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Phone'
    }), label=False)

    class Meta:
        model = UserModel
        fields = ['full_name', 'phone']
