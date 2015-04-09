from django.conf.urls import patterns, include, url
from django.core.urlresolvers import reverse
from django.contrib.sitemaps import Sitemap
from django.contrib import admin
from beratung_erfurt import settings

admin.autodiscover()

class ViewSitemap(Sitemap):
  """Reverse static views for XML sitemap."""
  def items(self):
    return [
      'index',
      # add your views here
    ]

  def location(self, item):
    try:
      return reverse(item)
    except Exception, e:
      return reverse("index")

sitemaps = {'views': ViewSitemap}


urlpatterns = patterns('',

    url(r'^$', 'beratung_erfurt.views.index', name = 'index'),
    url(r'^private/$', 'beratung_erfurt.views.private', name = 'private'),
    url(r'^company/$', 'beratung_erfurt.views.company', name = 'company'),

    url(r'^private/(?P<path>.+?)/$', 'beratung_erfurt.views.private_page', name = 'private_page'),
    url(r'^company/(?P<path>.+?)/$', 'beratung_erfurt.views.company_page', name = 'company_page'),


    url(r'^admin/', include(admin.site.urls)),

    (r'^sitemap\.xml$', 'django.contrib.sitemaps.views.sitemap', {'sitemaps': sitemaps}),
    url(r'^(?P<path>.+?)/$', 'beratung_erfurt.views.page', name = 'page'),
)

if settings.DEBUG is True:
  urlpatterns += patterns('',
    url(r'^media/(?P<path>.*)$', 'django.contrib.staticfiles.views.serve'),
    url(r'^static/(?P<path>.*)$', 'django.contrib.staticfiles.views.serve'),
  )


handler400 = 'beratung_erfurt.views.handler400'
handler403 = 'beratung_erfurt.views.handler403'
handler404 = 'beratung_erfurt.views.handler404'
handler500 = 'beratung_erfurt.views.handler500'