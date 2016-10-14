from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
import configparser
import logging
from slashgif_site.settings import CONFIG_FILE
import requests
import json

config = configparser.ConfigParser()
config.read(CONFIG_FILE)

log_file = config.get('Logging', 'file')
log_level = config.get('Logging', 'level')

logging_level = logging.getLevelName(log_level)
logging.basicConfig(filename=log_file, level=logging_level)

DISCORD_INSTALL_SUCCESS = ':white_check_mark: Successful Install'
DISCORD_INSTALL_ERROR = ':no_entry: **WARNING**: Installation Attempt Failure...'
DISCORD_HOOK_URI = config.get('Discord', 'hook_uri')

OAUTH_URL = config.get('Slack', 'oauth_url')
CLIENT_ID = config.get('Slack', 'client_id')
OAUTH_SCOPES = config.get('Slack', 'oauth_scopes')
CLIENT_SECRET = config.get('Slack', 'client_secret')
REDIRECT_URI = config.get('Slack', 'redirect_uri')


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
	oauth_uri = '%s?client_id=%s&scope=%s' % (OAUTH_URL, CLIENT_ID, OAUTH_SCOPES)
	return HttpResponseRedirect(oauth_uri)


def callback(request):
	"""
	Responds to oauth requests
	"""
	try:
		if request.GET['error'] == 'access_denied':
			return HttpResponseRedirect(reverse('cancel'))
	except Exception:
		pass

	try:
		oauth_code = request.GET['code']
		oauth_request = send_oauth(oauth_code)
		logging.info(oauth_request.text)
		oauth_response = json.loads(oauth_request.text)
	except Exception as error:
		logging.info(error)
		return HttpResponseRedirect(reverse('error'))

	if oauth_response['ok']:
		try:
			team_id = oauth_response['team_id']
			install_success_message = '%s (ID: %s)' % (DISCORD_INSTALL_SUCCESS, team_id)
			send_discord(install_success_message)
			return HttpResponseRedirect(reverse('success'))

		except Exception as error:
			logging.error(error)
			send_discord(DISCORD_INSTALL_ERROR)
			return HttpResponseRedirect(reverse('error'))

	else:
		logging.error(oauth_response)
		return HttpResponseRedirect(reverse('error'))


def send_oauth(oauth_code):
	"""
	Send Oauth Code
	"""
	oauth_uri = 'https://slack.com/api/oauth.access'
	payload = {"client_id": CLIENT_ID, "client_secret": CLIENT_SECRET, "code": oauth_code, 'redirect_uri': REDIRECT_URI}
	oauth_req = requests.post(oauth_uri, data=payload)
	return oauth_req


def send_discord(message):
	"""
	Send Discord Message
	"""
	try:
		headers = {'Content-Type': 'application/json'}
		body = {'content': message}
		requests.post(DISCORD_HOOK_URI, data=json.dumps(body), headers=headers, timeout=3)
		return
	except Exception as error:
		logging.info(error)
		return
