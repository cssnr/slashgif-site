from slashgif_site.settings import config

GLOBAL_VARIABLES = {
    'SLACK_APP_URL': config.get('Slack', 'slack_app_url'),
    'SITE_URI': config.get('App', 'site_uri'),
    'SITE_TITLE': config.get('Text', 'meta_description'),
    'SITE_AUTHOR': config.get('Text', 'meta_description'),
    'SITE_DESCRIPTION': config.get('Text', 'meta_description'),
    'SITE_KEYWORDS': config.get('Text', 'meta_keywords'),
}


def global_variables(request):
    return {
        'site_vars': GLOBAL_VARIABLES,
    }
