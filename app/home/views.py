import json
import logging

import requests
from django.conf import settings
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

# from django_statsd.clients import statsd

logger = logging.getLogger("app")


def home_view(request):
    return render(request, "home.html")


def support_view(request):
    return render(request, "support.html")


def privacy_view(request):
    return render(request, "privacy.html")


def success_view(request):
    return render(request, "success.html")


def error_view(request):
    return render(request, "error.html")


def cancel_view(request):
    return render(request, "cancel.html")


def add_to_slack(request):
    uri = "%s?client_id=%s&scope=%s" % (
        settings.SLACK_OAUTH_URL,
        settings.SLACK_CLIENT_ID,
        settings.SLACK_OAUTH_SCOPES,
    )
    return HttpResponseRedirect(uri)


def callback(request):
    """
    Responds to oauth requests
    """
    try:
        if request.GET.get("error") == "access_denied":
            # statsd.incr('cancel')
            return HttpResponseRedirect(reverse("cancel"))

        r = send_oauth(request.GET["code"])
        logger.debug(r.content)
        oauth = r.json()
        if not oauth["ok"]:
            return HttpResponseRedirect(reverse("error"))

    except Exception as error:
        logger.exception(error)
        return HttpResponseRedirect(reverse("error"))

    try:
        # statsd.incr('success')
        send_discord(":white_check_mark: Successful Install (ID: {})".format(oauth["team"]["id"]))
        return HttpResponseRedirect(reverse("success"))

    except Exception as error:
        logger.exception(error)
        # statsd.incr('failure')
        send_discord(":no_entry: **WARNING**: Installation Failure.")
        return HttpResponseRedirect(reverse("error"))


def send_oauth(oauth_code):
    """
    Send Oauth Code
    """
    data = {
        "client_id": settings.SLACK_CLIENT_ID,
        "client_secret": settings.SLACK_CLIENT_SECRET,
        "code": oauth_code,
    }
    return requests.post(settings.SLACK_ACCESS_URL, data=data, timeout=30)


def send_discord(message):
    """
    Send Discord Message
    """
    try:
        return requests.post(
            settings.DISCORD_HOOK_URL,
            data=json.dumps({"content": message}),
            headers={"Content-Type": "application/json"},
            timeout=3,
        )
    except Exception as error:
        logger.exception(error)
        return None
