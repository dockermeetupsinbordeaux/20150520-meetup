#!/bin/bash
set -e

if [ "$1" = 'redis-server' ]; then
	chown -R redis .
    if [ -d "/var/log/containers" ] ;then
    	chown -R redis /var/log/containers
    fi
	exec gosu redis "$@"
fi

exec "$@"
