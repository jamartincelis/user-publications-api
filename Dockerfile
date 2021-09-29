FROM python:3.8

ENV PYTHONUNBUFFERED 1

RUN apt update

RUN mkdir /code
WORKDIR /code
ADD . /code/
COPY ./init-user-db.sh /docker-entrypoint-initdb.d/init-user-db.sh

#RUN pip install pipenv
#RUN pipenv lock --requirements > requirements.txt
RUN pip install -r requirements.txt
#RUN python manage.py migrate --noinput
ADD ./docker-entrypoint.sh /docker-entrypoint.sh
RUN chmod +x /docker-entrypoint.sh
CMD ["/docker-entrypoint.sh"]