CREATE DATABASE sculdb;

CREATE USER sculuser WITH PASSWORD 'Huawei@123';

ALTER ROLE sculuser SET client_encoding TO 'utf8';
ALTER ROLE sculuser SET default_transaction_isolation TO 'read committed';
ALTER ROLE sculuser SET timezone TO 'GMT+5';

GRANT ALL PRIVILEGES ON DATABASE sculdb TO sculuser;