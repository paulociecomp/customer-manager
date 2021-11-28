CREATE SCHEMA IF NOT EXISTS customer_manager
  AUTHORIZATION customer_manager_adm;

CREATE EXTENSION IF NOT EXISTS HSTORE ;

CREATE EXTENSION pgcrypto;

CREATE TABLESPACE TSDCUSTOEMER_MANAGER01
  OWNER customer_manager_adm
  LOCATION '/tablespace/data';

CREATE TABLESPACE TSICUSTOEMER_MANAGER01
  OWNER customer_manager_adm
  LOCATION '/tablespace/index';

CREATE DATABASE db_customer_manager_test OWNER customer_manager_adm;
\connect db_customer_manager_test;

CREATE SCHEMA IF NOT EXISTS customer_manager
  AUTHORIZATION customer_manager_adm;

CREATE EXTENSION IF NOT EXISTS HSTORE ;

CREATE EXTENSION pgcrypto;

select pg_reload_conf();