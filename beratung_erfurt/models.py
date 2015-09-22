#coding=utf-8
from django.db import models
from django.shortcuts import get_object_or_404

class SeoData(models.Model):
  key = models.CharField(verbose_name = "Key", max_length = 255)
  description = models.TextField(verbose_name = "Beschreibung")
  keywords = models.TextField(verbose_name = "Keywords")

  class Meta:
    verbose_name = "Seo Data"
    verbose_name_plural = "Seo Data"

  @staticmethod
  def get_metadata(key):
    try:
      obj = SeoData.objects.get(key = key)
      return {
        "description": obj.description,
        "keywords": obj.keywords,
      }
    except SeoData.DoesNotExist:
      return {
        "description": "Create SeoData with key \"{}\"".format(key),
        "keywords": "Create SeoData with key \"{}\"".format(key),
      }

class Page(models.Model):
  title = models.CharField(verbose_name = "Titel", max_length = 255)
  path = models.CharField(verbose_name = "Pfad", max_length = 255)
  content = models.TextField(verbose_name = "Inhalt")
  active = models.BooleanField(verbose_name = "Aktiv")

  class Meta:
    verbose_name = "Seite"
    verbose_name_plural = "Seiten"


class Text(models.Model):
  key = models.CharField(verbose_name = "Key", max_length = 255)
  content = models.TextField(verbose_name = "Inhalt")

  class Meta:
    verbose_name = "Text"
    verbose_name_plural = "Texte"



class Image(models.Model):
  key = models.CharField(verbose_name = "Key", max_length = 255)
  image = models.ImageField(upload_to = "image_upload")

  class Meta:
    verbose_name = "Bild"
    verbose_name_plural = "Bilder"



class SubPage(models.Model):
  key = models.CharField(verbose_name = "Key", max_length = 255)
  title = models.CharField(verbose_name = "Titel", max_length = 255)
  info = models.TextField(verbose_name = "Info")
  cause = models.TextField(verbose_name = "Ursache")
  solution = models.TextField(verbose_name = "Lösung")

  class Meta:
    verbose_name = "Unterseite"
    verbose_name_plural = "Unterseiten"


