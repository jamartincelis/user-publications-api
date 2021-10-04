FROM python:3.8

ENV PYTHONUNBUFFERED 1

RUN apt update

RUN mkdir /code
WORKDIR /code
ADD . /code/
COPY ./init-user-db.sh /docker-entrypoint-initdb.d/init-user-db.sh

RUN pip install -r requirements-dev.txt
ADD ./docker-entrypoint.sh /docker-entrypoint.sh
RUN chmod +x /docker-entrypoint.sh
CMD ["/docker-entrypoint.sh"]
