from django.shortcuts import get_object_or_404

from utils.decorators import render_to
from beratung_erfurt.models import Page, Text, Image, SubPage, SeoData

@render_to("index.html")
def index(request):
  priv_key = "priv_pic"
  prof_key = "prof_pic"
  return {
    "priv_url": img_url(priv_key),
    "prof_url": img_url(prof_key),
    "priv_key": priv_key,
    "prof_key": prof_key,
    "meta_data": SeoData.get_metadata("index")
    }

@render_to("page.html")
def page(request, path):
  page = get_object_or_404(Page, path = path, active = True)
  return {
    "page_title": page.title,
    "content": page.content,
    "meta_data": SeoData.get_metadata(path)
  }

def info_text(key):
  try:
    return Text.objects.get(key = key).content
  except Text.DoesNotExist:
    return "create text for this key: <b>{}</b>".format(key)

def img_url(key):
  try:
    return Image.objects.get(key = key).image
  except Image.DoesNotExist:
    return None

@render_to("private.html")
def private(request):
  keys = [
    "stress",
    "self esteem",
    "desicion making",
    "everyday fears",
    "relationship",
    "consulting",]
  text_keys = map(lambda key: "private:" + key, keys)
  img_keys = map(lambda key: "private:img:" + key, keys)
  return {
    "page_title": info_text("private:title"),
    "info_text": info_text("private:info_text"),
    "honorar": info_text("private:honorar"),
    "context": info_text("private:context"),
    "contact": info_text("private:contact"),
    "texts": map(info_text, text_keys),
    "images": map(img_url, img_keys),
    "image_keys": img_keys,
    "urls": map(lambda key: key.replace(" ", "_"), keys),
    "meta_data": SeoData.get_metadata("private")
  }


@render_to("company.html")
def company(request):
  keys = [
    "employee satisfaction",
    "marketing",
    "customer satisfaction",
    "consulting",]
  text_keys = map(lambda key: "company:" + key, keys)
  img_keys = map(lambda key: "company:img:" + key, keys)
  return {
    "page_title": info_text("company:title"),
    "info_text": info_text("company:info_text"),
    "honorar": info_text("company:honorar"),
    "context": info_text("company:context"),
    "contact": info_text("company:contact"),
    "texts": map(info_text, text_keys),
    "images": map(img_url, img_keys),
    "image_keys": img_keys,
    "urls": map(lambda key: key.replace(" ", "_"), keys),
    "meta_data": SeoData.get_metadata("company")
  }


def sub_page(key):
  try:
    subpage = SubPage.objects.get(key = key)
    return {
      "page_title": subpage.title,
      "info_text": subpage.info,
      "cause_text": subpage.cause,
      "solution_text": subpage.solution,
      "meta_data": SeoData.get_metadata(key)
    }
  except SubPage.DoesNotExist:
    return {
      "page_title": "Create SubPage with key <b>{}</b>".format(key),
      "info_text": "Create SubPage with key <b>{}</b>".format(key),
      "cause_text": "Create SubPage with key <b>{}</b>".format(key),
      "solution_text": "Create SubPage with key <b>{}</b>".format(key),
      "meta_data": SeoData.get_metadata(key)
    }

@render_to("sub_page.html")
def company_page(request, path):
  return sub_page("company:" + path)


@render_to("sub_page.html")
def private_page(request, path):
  return sub_page("private:" + path)

from .errors import *
