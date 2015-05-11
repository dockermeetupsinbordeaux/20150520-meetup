#!/bin/bash
set -e

if [ "$1" = 'redis-server' ]; then
	chown -R redis .
	chown -R redis /var/log/containers
	exec gosu redis "$@"
fi

exec "$@
