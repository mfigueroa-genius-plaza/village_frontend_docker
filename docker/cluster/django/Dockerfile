FROM python:3.7

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# update pip and install pipenv
RUN pip install -U pip
RUN pip install pipenv

# setup path for codebase
RUN mkdir -p /code
WORKDIR /code

# copy code into container
COPY application/. /code/

# copy the .env file into the container
COPY docker/cluster/django/.env /code/

# copy pipfile and install dependencies
COPY Pipfile Pipfile.lock /code/
RUN pipenv install
