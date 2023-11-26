FROM mysql:latest

RUN chown -R mysql:root /var/lib/mysql/

WORKDIR /app
COPY . /app

ARG MYSQL_DATABASE
ARG MYSQL_USER
ARG MYSQL_PASSWORD
ARG MYSQL_ROOT_PASSWORD

ENV MYSQL_DATABASE=website
ENV MYSQL_PASSWORD=root
ENV MYSQL_ROOT_PASSWORD=root

RUN cp ./init.sql /docker-entrypoint-initdb.d

EXPOSE 3306