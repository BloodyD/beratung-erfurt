from django.contrib import admin

def register(*models, **kwargs):
  """
  Copied from Django 1.7 source

  Registers the given model(s) classes and wrapped ModelAdmin class with
  admin site:

  @register(Author)
  class AuthorAdmin(admin.ModelAdmin):
      pass

  A kwarg of `site` can be passed as the admin site, otherwise the default
  admin site will be used.
  """
  from django.contrib.admin import ModelAdmin
  from django.contrib.admin.sites import AdminSite

  def _model_admin_wrapper(admin_class):
    local_admin_site = kwargs.pop('site', admin.site)

    if not isinstance(local_admin_site, AdminSite):
      raise ValueError('site must subclass AdminSite')

    if not issubclass(admin_class, ModelAdmin):
      raise ValueError('Wrapped class must subclass ModelAdmin.')

    local_admin_site.register(models, admin_class=admin_class)

    return admin_class
  return _model_admin_wrapper



from beratung_erfurt.models import Page, Text, Image, SubPage, SeoData

@register(SeoData)
class SeoDataAdmin(admin.ModelAdmin):
  list_display = (
    'key',
    'description',
    'keywords',
    )



@register(Page)
class PageAdmin(admin.ModelAdmin):
  list_display = (
    'title',
    'path',
    '_content',
    'active',
    )


  _content = lambda self, obj: obj.content
  _content.allow_tags = True
  _content.short_description = Page._meta.get_field_by_name("content")[0].verbose_name

  list_filter = ['active']


@register(Text)
class TextAdmin(admin.ModelAdmin):
  list_display = (
    'key',
    '_content',
    )

  _content = lambda self, obj: obj.content
  _content.allow_tags = True
  _content.short_description = Text._meta.get_field_by_name("content")[0].verbose_name

@register(Image)
class ImageAdmin(admin.ModelAdmin):
  list_display = (
    'key',
    'image',
    )

@register(SubPage)
class SubPageAdmin(admin.ModelAdmin):
  list_display = (
    'key',
    # 'title',
    '_info',
    '_cause',
    '_solution',
    )


  _info = lambda self, obj: obj.info
  _info.allow_tags = True
  _info.short_description = SubPage._meta.get_field_by_name("info")[0].verbose_name

  _cause = lambda self, obj: obj.cause
  _cause.allow_tags = True
  _cause.short_description = SubPage._meta.get_field_by_name("cause")[0].verbose_name

  _solution = lambda self, obj: obj.solution
  _solution.allow_tags = True
  _solution.short_description = SubPage._meta.get_field_by_name("solution")[0].verbose_name
