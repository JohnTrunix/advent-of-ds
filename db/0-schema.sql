CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

-- create users table which stores user information
CREATE TABLE IF NOT EXISTS users (
    uuid uuid DEFAULT uuid_generate_v4 () PRIMARY KEY NOT NULL,
    github_id VARCHAR(255) UNIQUE NOT NULL,
    username VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL,
    avatar_url VARCHAR(255),
    profile_url VARCHAR(255),
    oauth_token VARCHAR(255) NOT NULL,
    created_at TIMESTAMP NOT NULL DEFAULT NOW()
);

-- create challenges table which stores challenge information
CREATE TABLE IF NOT EXISTS challenges (
    uuid uuid DEFAULT uuid_generate_v4 () PRIMARY KEY,
    day_id INTEGER NOT NULL UNIQUE,
    title VARCHAR(255) NOT NULL,
    tags VARCHAR(64)[] NOT NULL,
    open_at TIMESTAMP NOT NULL,
    created_by VARCHAR(255)
);

-- create submissions table which stores challenge completeness information
CREATE TABLE IF NOT EXISTS submissions (
    uuid uuid DEFAULT uuid_generate_v4 () PRIMARY KEY,
    user_uuid uuid NOT NULL REFERENCES users(uuid),
    challenge_uuid uuid NOT NULL REFERENCES challenges(uuid),
    opened_at TIMESTAMP NOT NULL,
    closed_at TIMESTAMP DEFAULT NULL,
    duration INTERVAL GENERATED ALWAYS AS (closed_at - opened_at) STORED,
    task_1 BOOLEAN NOT NULL DEFAULT FALSE,
    task_2 BOOLEAN NOT NULL DEFAULT FALSE,

    CONSTRAINT valid_duration CHECK (closed_at >= opened_at),
    CONSTRAINT task_completion CHECK (closed_at IS NULL OR (task_1 AND task_2))
);