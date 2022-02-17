FROM python:3.9

ENV PYTHONUNBUFFERED 1

RUN apt update -y
RUN apt upgrade -y

RUN mkdir /code
WORKDIR /code
ADD . /code/

RUN pip install -r requirements.txt
