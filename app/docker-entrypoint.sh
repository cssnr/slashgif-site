#!/usr/bin/env sh

set -ex

if echo "${*}" | grep -q "gun\|runserver";then
    if [ -n "${DJANGO_SUPERUSER_PASSWORD}" ] &&
    [ -n "${DJANGO_SUPERUSER_USERNAME}" ] &&
    [ -n "${DJANGO_SUPERUSER_EMAIL}" ];then
        uv run python manage.py createsuperuser --noinput || :
    fi
    #uv run python manage.py migrate --noinput
    uv run python manage.py collectstatic --noinput -v 0
fi

exec "$@"
