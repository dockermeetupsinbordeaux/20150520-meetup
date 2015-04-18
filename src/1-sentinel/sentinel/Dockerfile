FROM redis
MAINTAINER Cogniteev <tech@cogniteev.com>

ADD sentinel-start /bin/sentinel-start

ENV CLUSTER_NAME=meetup

ENTRYPOINT ["/bin/sentinel-start"]
