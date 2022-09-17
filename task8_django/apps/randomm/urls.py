from django.urls import path
from .views import randomm

app_name = 'apps.randomm'

urlpatterns =[
    path('', randomm),
    path('warning', randomm)
]