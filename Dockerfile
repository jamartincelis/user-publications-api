FROM python:3.10.2-alpine3.15

ENV PYTHONUNBUFFERED 1

RUN apk update
RUN apk upgrade --available
RUN mkdir /code
WORKDIR /code
ADD . /code/

RUN pip install -r requirements.txt
