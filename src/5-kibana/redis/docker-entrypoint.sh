#!/bin/bash
set -e

if [ "$1" = 'redis-server' ]; then
	chown -R redis .
	chown -R redis /logs
	exec gosu redis "$@"
fi

exec "$@
