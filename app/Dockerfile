FROM ghcr.io/astral-sh/uv:python3.13-alpine

LABEL org.opencontainers.image.source="https://github.com/cssnr/slashgif-site"
LABEL org.opencontainers.image.description="SlashGIF Website"
LABEL org.opencontainers.image.authors="smashedr"

ENV TZ=UTC
ENV PYTHONDONTWRITEBYTECODE=1
ENV UV_PROJECT_ENVIRONMENT=/usr/local
ENV UV_LOCKED=1
ENV UV_NO_DEV=1
ENV UV_NO_CACHE=1
ENV UV_NO_PROGRESS=1

RUN addgroup -g 1000 app  &&\
    adduser -S -H -h /app -s /sbin/nologin -u 1000 -G app app  &&\
    mkdir -p /app /data /data/static  &&  chown -R app:app /app /data /data/static  &&\
    apk add --no-cache curl

WORKDIR /app
COPY --chown=app:app pyproject.toml uv.lock ./
RUN uv sync
COPY --chown=app:app app ./
USER app
ENTRYPOINT ["sh", "docker-entrypoint.sh"]
