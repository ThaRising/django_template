#!/bin/bash
set -eu

export NGINX_PORT=${NGINX_PORT:-8080}
export NGINX_HOST=${NGINX_HOST:-localhost}

# shellcheck disable=SC2016
envsubst '${NGINX_PORT} ${NGINX_HOST}' < /etc/nginx/conf.d/default.conf.template > /etc/nginx/conf.d/default.conf

uwsgi /uwsgi.ini &
exec "$@"
