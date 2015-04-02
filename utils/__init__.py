
def default_template_dict(request, output = {}, title = ""):
  from beratung_erfurt import settings
  output.update({
    "settings": settings,
    "request": request,
    "title": title,
    })
  return output
