FROM postgres:alpine3.19

ENV POSTGRES_USER=postgres
ENV POSTGRES_PASSWORD=postgres
ENV POSTGRES_DB=aods

COPY 0-schema.sql /docker-entrypoint-initdb.d/

# mock data only in dev
COPY 10-mock.sql /docker-entrypoint-initdb.d/

# VOLUME /var/lib/postgresql/data save volumen for backup purposes in prod

EXPOSE 5432