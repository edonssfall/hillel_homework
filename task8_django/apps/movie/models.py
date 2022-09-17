from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.postgres.fields import ArrayField


class Movie(models.Model):
    class TitleType(models.TextChoices):
        short = 'short', _("Short")
        movie = 'movie', _("Movie")

    imdb_id = models.CharField(_("IMDB Id"), max_length=255, null=True)
    title_type = models.CharField(_("Title Type"), max_length=255, choices=TitleType.choices, null=True)
    name = models.CharField(_("Name"), max_length=255, null=True)
    is_adult = models.BooleanField(_("Is Adult"), default=False)
    year = models.DateField(_("Year"), auto_now=False, auto_now_add=False, blank=True)
    genres = ArrayField(models.CharField(max_length=255), verbose_name=_("Genre"), null=True)

    def __str__(self):
        return f"M: {self.name}"


class Person(models.Model):
    imdb_id = models.CharField(_("IMDB Id"), max_length=255, null=True)
    name = models.CharField(_("Name"), max_length=255, null=True)
    birth_year = models.DateField(_("Birth Year"), null=True)
    death_year = models.DateField(_("Death Year"), null=True)

    def __str__(self):
        return f"P: {self.name}"


class PersonMovie(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.PROTECT)
    person = models.ForeignKey(Person, on_delete=models.PROTECT)
    order = models.IntegerField(_("Order"), null=True)
    category = models.CharField(_("Category"), max_length=255, null=True)
    job = models.CharField(_("Job"), max_length=255, null=True)
    characters = ArrayField(models.CharField(max_length=255, null=True), verbose_name=_("Characters"), blank=True, null=True)
