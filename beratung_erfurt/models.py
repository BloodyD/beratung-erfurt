from django.db import models


class Page(models.Model):
  title = models.CharField(verbose_name="Titel", max_length = 255)
  path = models.CharField(verbose_name="Pfad", max_length = 255)
  content = models.TextField(verbose_name="Inhalt")
  active = models.BooleanField(verbose_name="Aktiv")


class Text(models.Model):
  key = models.CharField(verbose_name="Key", max_length = 255)
  content = models.TextField(verbose_name="Inhalt")
