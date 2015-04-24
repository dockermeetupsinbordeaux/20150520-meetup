FROM python:2.7
ADD . /code
WORKDIR /code
RUN apt-get update && apt-get install -y uwsgi uwsgi-plugin-python
RUN pip install -r requirements.txt
VOLUME /data
EXPOSE 5000
CMD uwsgi                   \
    --socket 0.0.0.0:5000   \
    -w app:app              \
    --logto /data/flask.log \
    --umask 644
