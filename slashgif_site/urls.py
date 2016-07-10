from django.conf.urls import url
from django.views.generic.base import RedirectView
from django.contrib import admin
from slashgif_site.settings import STATIC_URL
import home.views as home


urlpatterns = [
	url(r'^$', home.home, name='home'),
	url(r'^robots\.txt$', RedirectView.as_view(url=STATIC_URL + 'robots.txt')),
	url(r'^favicon\.ico$', RedirectView.as_view(url=STATIC_URL + 'favicon.ico')),
	url(r'^sitemap\.xml', RedirectView.as_view(url=STATIC_URL + 'sitemap.xml')),
	url(r'^support/', home.support, name="support"),
	url(r'^privacy/', home.privacy, name="privacy"),
	url(r'^success/', home.success, name="success"),
	url(r'^error/', home.error, name="error"),
	url(r'^cancel/', home.cancel, name="cancel"),
	url(r'^addtoslack/', home.addtoslack, name="addtoslack"),
	url(r'^callback/', home.callback),
	url(r'^admin/', admin.site.urls, name="django_admin"),
]
