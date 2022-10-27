from django.urls import path
from .views import home_view, input_view


urlpatterns = [
    path('', home_view, name='home'),
    path('input/', input_view, name='input'),
]
