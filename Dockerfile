FROM python:3.8-alpine

ENV DJANGO_SETTINGS_MODULE=bcp.settings
ENV PYTHONPATH=/app

WORKDIR /app
COPY . /app

RUN apk add libpq tiff libjpeg libpng

RUN apk add --no-cache --virtual .build-deps \
    gcc \
    python3-dev \
    musl-dev \
    postgresql-dev \
    jpeg-dev \
    zlib-dev \
    libjpeg \
    && pip install --no-cache-dir -r requirements.txt \
    && apk del --no-cache .build-deps

CMD ["/app/docker/backend/start.sh"]
