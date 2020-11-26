FROM python:3.8-alpine

ARG BRANCH="master"
ARG COMMIT="head"
ARG DATE="unknown"

ENV DJANGO_SETTINGS_MODULE=bcp.settings
ENV PYTHONPATH=/app
ENV COMMIT_SHA=${COMMIT}
ENV COMMIT_BRANCH=${BRANCH}
ENV BUILD_DATE=${DATE}

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
