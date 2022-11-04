from django.shortcuts import render
from .models import BarberModel


def booking_view(request):
    barbers = BarberModel.objects.all()
    return render(request, 'main/booking.html', context={
        'barbers': barbers
    })
