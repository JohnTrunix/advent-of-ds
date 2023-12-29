FROM postgres:alpine3.19

ENV POSTGRES_USER=postgres
ENV POSTGRES_PASSWORD=postgres
ENV POSTGRES_DB=aods

COPY 0-schema.sql /docker-entrypoint-initdb.d/
COPY 1-view.sql /docker-entrypoint-initdb.d/
COPY 10-mock.sql /docker-entrypoint-initdb.d/

VOLUME /var/lib/postgresql/data

EXPOSE 5432