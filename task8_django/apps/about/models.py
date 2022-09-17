from django.db import models
from django.utils.translation import gettext_lazy as _


class Whoami(models.Model):
    user_agent = models.CharField(_("User Agent"), max_length=255)
    ip_adres = models.CharField(_("IP"), max_length=16, null=True)
    now_time = models.TimeField(_("Time"), auto_now=True)
