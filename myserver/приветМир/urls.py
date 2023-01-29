from django.urls import path

from приветМир.views import привет

app_name = 'привет'

urlpatterns = [
    path('', привет, name='index'),
]
