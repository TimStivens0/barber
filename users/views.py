from django.shortcuts import render, redirect
from .forms import UserModelForm
from .models import UserModel


def home_view(request):
    return render(request, 'main/home.html', context={})


def input_view(request):
    form = UserModelForm()
    if request.method == "POST":
        data = UserModelForm(data=request.POST)
        if data.is_valid():
            user = UserModel(
                full_name=data.cleaned_data['full_name'],
                phone=data.cleaned_data['phone']
            )
            user.save()
            return redirect('/')
    return render(request, 'main/input.html', context={
        'form': form
    })
