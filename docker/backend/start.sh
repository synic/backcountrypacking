#!/bin/sh

BIND="${BIND:-0.0.0.0:8001}"
GUNICORN_ACCESS_LOG_FORMAT_DEFAULT="%({x-forwarded-for}i)s %(h)s \\\"%(r)s\\\" %(s)s %(D)s %(b)s \\\"%(f)s\\\" \\\"%(a)s\\\""
GUNICORN_PID_FILE="${GUNICORN_PID_FILE:-/var/run/gunicorn.pid}"
GUNICORN_ACCESS_LOG_FORMAT="${GUNICORN_ACCESS_LOG_FORMAT:-${GUNICORN_ACCESS_LOG_FORMAT_DEFAULT}}"
DJANGO_SETTINGS_MODULE=bcp.settings
PYTHONPATH=$PYTHONPATH:/app

echo "Starting up ..."
django-admin migrate --noinput
django-admin collectstatic --noinput

while true; do
    APP_CMD="gunicorn -b ${BIND} --pid ${GUNICORN_PID_FILE} --access-logfile - --access-logformat \"${GUNICORN_ACCESS_LOG_FORMAT}\" bcp.wsgi:application"

    if [[ ! -z "$BCP_DEV" ]]; then
        echo -n " * Enabling reloading..."
        # Install inotify so --reload works
        python3 -mpip install inotify 2>&1 > /dev/null && echo " done"

        # Gunicorn only reloads on files it's aware of on startup. Things loaded
        # lazily will not be watch and gunicorn will not auto restart
        RELOAD_EXTRA_FILES=""
        for f in `find /app/ -name '__init__.py' -print`; do
            RELOAD_EXTRA_FILES="${RELOAD_EXTRA_FILES} --reload-extra-file=${f}"
        done

        APP_CMD="${APP_CMD} -t 600 --reload${RELOAD_EXTRA_FILES}"

        sleep 5
    fi

    echo "Running ${APP_CMD}"
    eval $APP_CMD
    echo "Process died. Sleeping 10s before restarting."
    sleep 10
done
