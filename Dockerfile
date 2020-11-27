ARG BRANCH="master"
ARG COMMIT="head"
ARG DATE="unknown"
ARG BCP_ENV="production"

FROM python:3.8-alpine AS base

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

FROM base AS build-production
RUN echo " -> Building production image"

FROM base AS build-development
RUN echo " -> Building development image"
RUN cat /app/docker/backend/dependencies/development/apk.txt | xargs apk add
RUN pip3 install --no-cache-dir -r \
    /app/docker/backend/dependencies/development/python.txt
ENV PS1="bcp-web> "

FROM build-${BCP_ENV} as final
CMD ["/app/docker/backend/start.sh"]
