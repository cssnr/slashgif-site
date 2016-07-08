from django.conf.urls import url
from django.views.generic.base import RedirectView
from django.contrib import admin
import configparser
from slashgif_site.settings import CONFIG_FILE
from slashgif_site.settings import STATIC_URL
import home.views as home

config = configparser.ConfigParser()
config.read(CONFIG_FILE)

slack_app_url = config.get('Slack', 'slack_url')

urlpatterns = [
	url(r'^$', home.home, name='home'),
	url(r'^robots\.txt$', RedirectView.as_view(url=STATIC_URL + 'robots.txt')),
	url(r'^favicon\.ico$', RedirectView.as_view(url=STATIC_URL + 'favicon.ico')),
	url(r'^sitemap\.xml', RedirectView.as_view(url=STATIC_URL + 'sitemap.xml')),
	url(r'^error/', home.error, name="error"),
	url(r'^success/', home.success, name="success"),
	url(r'^privacy/', home.privacy, name="privacy"),
	url(r'^support/', home.support, name="support"),
	url(r'^slack/', RedirectView.as_view(url=slack_app_url), name="slack"),
	url(r'^admin/', admin.site.urls, name="django_admin"),
]
