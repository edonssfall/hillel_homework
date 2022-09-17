from django.urls import path
from .views import whoam_i, home

app_name = 'apps.about'

urlpatterns = [
    path('about/    ', home),
    path('about/whoami/', whoam_i)
]