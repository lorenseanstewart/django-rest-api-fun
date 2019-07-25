FROM python:3.7-alpine

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /requirements.txt

# apk is the alpine package manager
# --no-cache means: don't store the registry index in our container. This keeps the container light
RUN apk add --update --no-cache postgresql-client

# below are temporary dependencies that will be removed below
RUN apk add --update --no-cache --virtual .tmp-build-deps \
    gcc libc-dev linux-headers postgresql-dev

RUN pip install -r /requirements.txt

# remove temporary dependencies
RUN apk del .tmp-build-deps

RUN mkdir /app
WORKDIR /app
COPY ./app /app

RUN adduser -D user
USER user
