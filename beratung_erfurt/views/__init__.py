from django.shortcuts import get_object_or_404

from utils.decorators import render_to
from beratung_erfurt.models import Page


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



from .errors import *