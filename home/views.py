import json
import logging
import requests
import statsd
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from slashgif_site.settings import config

logger = logging.getLogger(__name__)

stats = statsd.StatsClient(
    config.get('Stats', 'metric_host'),
    config.getint('Stats', 'metric_port'),
)

DISCORD_INSTALL_SUCCESS = ':white_check_mark: Successful Install'
DISCORD_INSTALL_ERROR = ':no_entry: **WARNING**: Installation Failure.'


def home(request):
    return render(request, 'home.html')


def support(request):
    return render(request, 'support.html')


def privacy(request):
    return render(request, 'privacy.html')


def success(request):
    return render(request, 'success.html')


def error(request):
    return render(request, 'error.html')


def cancel(request):
    return render(request, 'cancel.html')


def addtoslack(request):
    oauth_uri = '%s?client_id=%s&scope=%s' % (
        config.get('Slack', 'oauth_url'),
        config.get('Slack', 'client_id'),
        config.get('Slack', 'oauth_scopes'),
    )
    return HttpResponseRedirect(oauth_uri)


def callback(request):
    """
    Responds to oauth requests
    """
    try:
        if request.GET['error'] == 'access_denied':
            add_stat('cancel')
            return HttpResponseRedirect(reverse('cancel'))
    except Exception:
        pass

    try:
        oauth_code = request.GET['code']
        oauth_request = send_oauth(oauth_code)
        logger.info(oauth_request.text)
        oauth_response = json.loads(oauth_request.text)
    except Exception as error:
        logger.info(error)
        return HttpResponseRedirect(reverse('error'))

    if oauth_response['ok']:
        try:
            team_id = oauth_response['team_id']
            add_stat('success')
            install_success_message = '%s (ID: %s)' % (
                DISCORD_INSTALL_SUCCESS, team_id
            )
            send_discord(install_success_message)
            return HttpResponseRedirect(reverse('success'))

        except Exception as error:
            logger.exception(error)
            add_stat('failure')
            send_discord(DISCORD_INSTALL_ERROR)
            return HttpResponseRedirect(reverse('error'))

    else:
        logger.error(oauth_response)
        return HttpResponseRedirect(reverse('error'))


def send_oauth(oauth_code):
    """
    Send Oauth Code
    """
    oauth_uri = 'https://slack.com/api/oauth.access'
    payload = {
        "client_id": config.get('Slack', 'client_id'),
        "client_secret": config.get('Slack', 'client_secret'),
        "code": oauth_code,
        'redirect_uri': config.get('Slack', 'redirect_uri'),
    }
    oauth_req = requests.post(oauth_uri, data=payload)
    return oauth_req


def send_discord(message):
    """
    Send Discord Message
    """
    try:
        headers = {'Content-Type': 'application/json'}
        body = {'content': message}
        requests.post(
            config.get('Discord', 'hook_uri'),
            data=json.dumps(body),
            headers=headers, timeout=3,
        )
        return
    except Exception as error:
        logger.info(error)
        return


def add_stat(metric_name):
    """
    Add Metric
    """
    metric = '{0}.{1}'.format(
        config.get('Stats', 'metric_prefix'),
        metric_name,
    )
    stats.incr(metric)
