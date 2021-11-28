FROM postgres:14.1

ENV POSTGRES_USER customer_manager_adm
ENV POSTGRES_PASSWORD customer_manager_adm
ENV POSTGRES_DB db_customer_manager

RUN mkdir -p /tablespace/data \
    && mkdir -p /tablespace/index \
    && mkdir -p /tablespace/tsdcustomer_manager01 \
    && mkdir -p /tablespace/tsicustomer_manager01 \
    && chown -R postgres:postgres /tablespace \
    && chmod 777 /tablespace/data \
    && chmod 777 /tablespace/index \
    && chmod 777 /tablespace/tsdcustomer_manager01 \
    && chmod 777 /tablespace/tsicustomer_manager01

COPY initial.sql /docker-entrypoint-initdb.d/
