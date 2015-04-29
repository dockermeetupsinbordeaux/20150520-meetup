FROM logstash

USER root

ADD logstash.conf /config-dir/
ADD start-logstash /usr/bin/
CMD start-logstash
EXPOSE 514 9292
