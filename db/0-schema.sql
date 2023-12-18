CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

-- create users table which stores user information
CREATE TABLE IF NOT EXISTS users (
    uuid uuid DEFAULT uuid_generate_v4 () PRIMARY KEY,
    github_id VARCHAR(255) UNIQUE NOT NULL,
    username VARCHAR(255) NOT NULL,
    email VARCHAR(255),
    avatar_url VARCHAR(255),
    profile_url VARCHAR(255),
    oauth_token VARCHAR(255) NOT NULL,
    created_at TIMESTAMP NOT NULL DEFAULT NOW()
);

-- create challenge table which stores challenge completeness information
CREATE TABLE IF NOT EXISTS challenges (
    uuid uuid DEFAULT uuid_generate_v4 () PRIMARY KEY,
    user_uuid uuid NOT NULL REFERENCES users(uuid),
    challenge_id VARCHAR(255) NOT NULL,
    challenge_opened_at TIMESTAMP NOT NULL DEFAULT NOW(),
    challenge_completed_at TIMESTAMP,
    challenges_completed INTEGER DEFAULT 0,
    is_fastest_for_challenge BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP NOT NULL DEFAULT NOW()
);