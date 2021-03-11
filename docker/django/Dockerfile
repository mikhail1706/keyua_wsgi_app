FROM python:3.8
MAINTAINER Mikhail Gumen

ADD . /usr/src/app
WORKDIR /usr/src/app
COPY requirements.txt ./
COPY .env .env
RUN pip install --no-cache-dir -r requirements.txt
ENTRYPOINT ["/usr/src/app/docker/django/entrypoint_db.sh"]
ENTRYPOINT ["/usr/src/app/docker/django/entrypoint.sh"]
