FROM python:3.7-alpine

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# development dependencies
RUN apk update && apk add python3-dev gcc musl-dev postgresql-dev netcat-openbsd

# update pip and install pipenv
RUN pip install -U pip
RUN pip install pipenv

# setup path for codebase
RUN mkdir -p /code
WORKDIR /code

# copy pipfile and install dependencies
COPY Pipfile Pipfile.lock /code/
RUN pipenv install --dev

# code is linked in /code via volume
