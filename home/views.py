from django.shortcuts import render
import configparser
import logging
from slashgif_site.settings import CONFIG_FILE

config = configparser.ConfigParser()
config.read(CONFIG_FILE)

log_file = config.get('Logging', 'file')
log_level = config.get('Logging', 'level')

logging_level = logging.getLevelName(log_level)
logging.basicConfig(filename=log_file, level=logging_level)


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
