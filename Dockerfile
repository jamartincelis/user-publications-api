# pull official base image
FROM python:3.10.3-alpine3.15

# upgrade alpine
RUN apk update
RUN apk upgrade --available

# set work directory
WORKDIR /code

# set environment variables
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# copy project
COPY . /code/
