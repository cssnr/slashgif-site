import os
from slashgif_site.settings import config

SITE_TITLE = 'SlashGIF'
SITE_AUTHOR = 'Shane Rice'
SITE_DESCRIPTION = ('Search For and Preview Random GIFs Before Posting '
                    'to Slack.')
SITE_KEYWORDS = ('GIF search,random GIF,Slack GIF,GIF Preview,Slash GIF,'
                 'SlashGIF,GIF,GIFS,Giphy,Slack')

GLOBAL_VARIABLES = {
    'SLACK_APP_URL': config.get('Slack', 'slack_app_url'),
    'SITE_URI': config.get('App', 'site_uri'),
    'SITE_TITLE': SITE_TITLE,
    'SITE_AUTHOR': SITE_AUTHOR,
    'SITE_DESCRIPTION': SITE_DESCRIPTION,
    'SITE_KEYWORDS': SITE_KEYWORDS,
}


def global_variables(request):
    return {
        'site_vars': GLOBAL_VARIABLES,
    }
