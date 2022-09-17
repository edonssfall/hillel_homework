from django.db import models
from django.utils.translation import gettext_lazy as _

class Randomm(models.Model):
    length = models.CharField(_("Length"), max_length=100)
    digits = models.BooleanField(_("Digits is on"), default=False)
    specials = models.BooleanField(_("Specials is on"), default=False)
