FROM redis
MAINTAINER Cogniteev <tech@cogniteev.com>

ADD sentinel-start /bin/sentinel-start

ENV CLUSTER_NAME=meetup
ENV SENTINEL_NAME=sentinel
EXPOSE 26379

ENTRYPOINT ["/bin/sentinel-start"]
