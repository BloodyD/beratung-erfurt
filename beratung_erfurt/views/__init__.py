from django.shortcuts import get_object_or_404

from utils.decorators import render_to
from beratung_erfurt.models import Page, Text


@render_to("index.html")
def index(request):
  return {}

@render_to("page.html")
def page(request, path):
  page = get_object_or_404(Page, path = path, active = True)
  return {
    "page_title": page.title,
    "content": page.content,
  }

def info_text(key):
  try:
    return Text.objects.get(key = key).content
  except Text.DoesNotExist:
    return "create text for this key: {}".format(key)

@render_to("private.html")
def private(request):
  return {
    "page_title": info_text("private:title"),
    "info_text": info_text("private:info_text"),
    "honorar": info_text("private:honorar"),
    "context": info_text("private:context"),
    "contact": info_text("private:contact"),
  }


@render_to("company.html")
def company(request):
  return {
    "page_title": info_text("company:title"),
    "info_text": info_text("company:info_text"),
    "honorar": info_text("company:honorar"),
    "context": info_text("company:context"),
    "contact": info_text("company:contact"),
  }


from .errors import *