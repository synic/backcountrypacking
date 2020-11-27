#!/bin/sh

BIND="${BIND:-0.0.0.0:8001}"
GUNICORN_ACCESS_LOG_FORMAT_DEFAULT="%({x-forwarded-for}i)s %(h)s \\\"%(r)s\\\" %(s)s %(D)s %(b)s \\\"%(f)s\\\" \\\"%(a)s\\\""
GUNICORN_PID_FILE="${GUNICORN_PID_FILE:-/var/run/gunicorn.pid}"
GUNICORN_ACCESS_LOG_FORMAT="${GUNICORN_ACCESS_LOG_FORMAT:-${GUNICORN_ACCESS_LOG_FORMAT_DEFAULT}}"
APP_CMD="gunicorn -b ${BIND} --pid ${GUNICORN_PID_FILE} --access-logfile - --access-logformat \"${GUNICORN_ACCESS_LOG_FORMAT}\" bcp.wsgi:application"

echo "Starting up ..."

if [[ "$BCP_ENV" == "development" ]]; then
    APP_CMD="${APP_CMD} -t 600 --reload"

    ./docker/wait-for bcp-db:5432
fi

django-admin migrate --noinput
django-admin collectstatic --noinput

while true; do
    echo "Running ${APP_CMD}"
    eval $APP_CMD
    echo "Process died. Sleeping 10s before restarting."
    sleep 10
done
