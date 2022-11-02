from django.db import models
from users.models import UserModel


class BarberModel(models.Model):
    time1 = models.BooleanField('09:00 AM', default=False)
    time2 = models.BooleanField('10:00 AM', default=False)
    time3 = models.BooleanField('11:00 AM', default=False)
    time4 = models.BooleanField('12:00 AM', default=False)
    time5 = models.BooleanField('02:00 PM', default=False)
    time6 = models.BooleanField('03:00 PM', default=False)
    time7 = models.BooleanField('04:00 PM', default=False)
    time8 = models.BooleanField('05:00 PM', default=False)
    time9 = models.BooleanField('07:00 PM', default=False)
    time10 = models.BooleanField('08:00 PM', default=False)
    time11 = models.BooleanField('09:00 PM', default=False)
    time12 = models.BooleanField('10:00 PM', default=False)
    # user = models.OneToOneField(UserModel, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'barber'
        verbose_name_plural = 'barbers'
