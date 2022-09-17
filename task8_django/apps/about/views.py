from django.shortcuts import render
from apps.about.models import Whoami
import time


def home(request):
    return render(request, 'about/base.html')


def whoam_i(request):
    user_agent = request.user_agent.browser.family + " " + request.user_agent.browser.version_string
    ip = request.META.get('REMOTE_ADDR')
    now_time = time.strftime("%c")
    Whoami.objects.create(user_agent=user_agent, ip_adres=ip)
    return render(request, 'about/whoami.html', context={'user_agent': user_agent, 'ip': ip, 'now_time': now_time})
