# SlashGIF Website

- https://slashgif.com/
- https://slack.com/apps/A1LE4DYCQ-slashgif

## Frameworks

- Django (5.x) https://www.djangoproject.com/
- Bootstrap (5.3.x) http://getbootstrap.com/
- JQuery (3.7.x) https://jquery.com/

## TODO

Dead env vars in `docker-compose-swarm.yaml` not read by `settings.py`:

- `DJANGO_DATA_DIR` (added since master)
- `SLACK_SIGNING_SECRET` (added since master)
- `STATSD_PREFIX` (commented out in settings.py)
- `STATSD_PORT` (commented out in settings.py)
- `STATSD_HOST` (commented out in settings.py)
