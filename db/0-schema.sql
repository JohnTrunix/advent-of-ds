CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

-- create users table which stores user information
CREATE TABLE IF NOT EXISTS users (
    uuid uuid DEFAULT uuid_generate_v4 () PRIMARY KEY,
    name VARCHAR(255) UNIQUE NOT NULL,
    score INT DEFAULT 0,
    coffees INT DEFAULT 0
);