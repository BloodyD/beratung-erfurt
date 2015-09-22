from django.template import Library

register = Library()

@register.inclusion_tag("seo_data.html")
def seo_data(metadata):
  return metadata

@register.inclusion_tag('box.html')
def box(img_url, img_key, text, url):
  return {
    "img_url": img_url,
    "img_key": img_key,
    "text": text,
    "allgemein": "allgemeine beratung" in text.lower(),
    "url": url,
  }