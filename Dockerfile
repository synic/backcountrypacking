ARG build_info="head@now"
ARG build_env="production"

FROM python:3.8-alpine AS base

ARG build_info
ARG build_env

ENV DJANGO_SETTINGS_MODULE=bcp.settings
ENV PYTHONPATH=/app
ENV BUILD_INFO=${build_info}

WORKDIR /app
COPY . /app

RUN apk add --no-cache libpq tiff libjpeg libpng

RUN apk add --no-cache --virtual .build-deps \
    gcc \
    python3-dev \
    musl-dev \
    postgresql-dev \
    jpeg-dev \
    zlib-dev \
    && pip install --no-cache-dir -r requirements.txt \
    && apk del --no-cache .build-deps

FROM base AS build-production
RUN echo " -> Building production image"

FROM base AS build-development
RUN echo " -> Building development image"
RUN cat /app/docker/backend/dependencies/development/apk.txt | xargs apk add --no-cache
RUN pip3 install --no-cache-dir -r \
    /app/docker/backend/dependencies/development/python.txt
ENV PS1="web> "
ENV PYTHONBREAKPOINT=ipdb.set_trace

FROM build-${build_env} AS final

CMD ["/app/docker/backend/start.sh"]
