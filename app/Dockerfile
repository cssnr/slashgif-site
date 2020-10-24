FROM python:3.8-alpine
ENV TZ=America/Los_Angeles

WORKDIR /app
COPY requirements.txt /app

RUN python -m pip install --no-cache-dir --upgrade pip && \
    python -m pip install --no-cache-dir -r requirements.txt

COPY . /app

ENTRYPOINT ["sh", "docker-entrypoint.sh"]
