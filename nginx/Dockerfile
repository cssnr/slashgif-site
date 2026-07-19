FROM nginx:alpine-slim

LABEL org.opencontainers.image.source="https://github.com/cssnr/slashgif-site"
LABEL org.opencontainers.image.description="SlashGIF Website Nginx"
LABEL org.opencontainers.image.authors="smashedr"

ENV TZ=UTC

COPY nginx.conf /etc/nginx/nginx.conf
