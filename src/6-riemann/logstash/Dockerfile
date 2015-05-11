FROM logstash

USER root

ENV LOGSTASH_CONTRIB_VERSION 1.4.2-1-efd53ef
RUN set -x \
	&& apt-get update \
	&& apt-get install -y --no-install-recommends \
	   logstash-contrib=$LOGSTASH_CONTRIB_VERSION \
	&& rm -rf /var/lib/apt/lists/*

ADD logstash.conf /config-dir/
ADD start-logstash /usr/bin/
CMD start-logstash
EXPOSE 514 9292
