FROM python:3.8.2-alpine

RUN apk update \
  && apk add \
    build-base \
    libpq

RUN mkdir /usr/src/app
WORKDIR /usr/src/app

COPY ./requirements.txt .
RUN pip install -r requirements.txt

COPY . .