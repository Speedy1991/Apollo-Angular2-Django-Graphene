FROM python:3.4
ENV PYTHONUNBUFFERED 1
RUN apt-get update
RUN apt-get install sqlite3
RUN mkdir /app
WORKDIR /app
ADD requirements.txt /app/
RUN pip3 install -r requirements.txt
ADD . /app/