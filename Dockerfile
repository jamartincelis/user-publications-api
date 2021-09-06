FROM python:3.8

ENV PYTHONUNBUFFERED 1

RUN apt update

RUN mkdir /code
WORKDIR /code
ADD . /code/

RUN pip install pipenv
RUN pipenv lock --requirements > requirements.txt
RUN pip install -r requirements.txt
