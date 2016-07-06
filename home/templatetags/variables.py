from django import template
import configparser
from slashgif_site.settings import CONFIG_FILE

SITE_TITLE = 'SlashGIF'
SITE_AUTHOR = 'Shane Rice'
SITE_DESCRIPTION = 'Search For and Preview Random GIFs Before Posting to Slack.'
SITE_KEYWORDS = 'GIF search,random GIF,Slack GIF,GIF Preview,Slash GIF,SlashGIF,GIF,GIFS,Giphy,Slack'

config = configparser.RawConfigParser()
config.read(CONFIG_FILE)

SITE_URI = config.get('App', 'site_uri')

OAUTH_URI = config.get('Slack', 'oauth_uri')
CLIENT_ID = config.get('Slack', 'client_id')
OAUTH_SCOPES = config.get('Slack', 'oauth_scopes')
SLACK_APP_URL = config.get('Slack', 'slack_url')

register = template.Library()

@register.simple_tag
def site_vars():
	oauth_uri = '%s?client_id=%s&scope=%s' % (OAUTH_URI, CLIENT_ID,OAUTH_SCOPES)
	value = {
		'OAUTH_URI': oauth_uri,
		'SLACK_APP_URL': SLACK_APP_URL,
		'SITE_URI': SITE_URI,
		'SITE_TITLE': SITE_TITLE,
		'SITE_AUTHOR': SITE_AUTHOR,
		'SITE_DESCRIPTION': SITE_DESCRIPTION,
		'SITE_KEYWORDS': SITE_KEYWORDS,
	}
	return value
