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
      'private',
      'company',
    ]

  def location(self, item):
    try:
      return reverse(item)
    except Exception, e:
      return reverse("index")

sitemaps = {'views': ViewSitemap}

from django.http import HttpResponse

urlpatterns = patterns('',

    url(r'^$', 'beratung_erfurt.views.index', name = 'index'),
    url(r'^private/$', 'beratung_erfurt.views.private', name = 'private'),
    url(r'^company/$', 'beratung_erfurt.views.company', name = 'company'),

    url(r'^private/(?P<path>.+?)/$', 'beratung_erfurt.views.private_page', name = 'private_page'),
    url(r'^company/(?P<path>.+?)/$', 'beratung_erfurt.views.company_page', name = 'company_page'),


    url(r'^admin/', include(admin.site.urls)),

    (r'^sitemap\.xml$', 'django.contrib.sitemaps.views.sitemap', {'sitemaps': sitemaps}),
    url(r'^google795b8bd63344ce1e\.html$', lambda x: HttpResponse("google-site-verification: google795b8bd63344ce1e.html")),
    url(r'^mywotc1345dd94b7e668fb1a3\.html$', lambda x: HttpResponse("30520abbde1b740cf42043cdfc2bafd7")),
    url(r'^(?P<path>.+?)/$', 'beratung_erfurt.views.page', name = 'page'),
    url(r'^robots\.txt$', lambda x: HttpResponse("User-agent: *\nDisallow: /media/")),
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