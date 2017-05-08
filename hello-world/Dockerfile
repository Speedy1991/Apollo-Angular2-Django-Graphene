FROM node:7.10

RUN apt-get update
RUN apt-get install net-tools -y -q
RUN mkdir /app
WORKDIR /app
ADD . /app/
RUN yarn install
