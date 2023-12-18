-- Insert mock data into the users table
INSERT INTO users (github_id, username, email, avatar_url, profile_url, oauth_token)
VALUES
    ('id1', 'max.hello', 'max@muster', 'https://picsum.photos/200', 'https://github.com/max.hello', 'token_123'),
    ('id2', 'john.doe', 'john@example.com', 'https://picsum.photos/200', 'https://github.com/john.doe', 'token_456'),
    ('id3', 'jane.smith', 'jane@example.com', 'https://picsum.photos/200', 'https://github.com/jane.smith', 'token_789'),
    ('id4', 'alice', 'alice@example.com', 'https://picsum.photos/200', 'https://github.com/alice', 'token_abc'),
    ('id5', 'bob', 'bob@example.com', 'https://picsum.photos/200', 'https://github.com/bob', 'token_def'),
    ('id6', 'charlie', 'charlie@example.com', 'https://picsum.photos/200', 'https://github.com/charlie', 'token_ghi'),
    ('id7', 'david', 'david@example.com', 'https://picsum.photos/200', 'https://github.com/david', 'token_jkl'),
    ('id8', 'emma', 'emma@example.com', 'https://picsum.photos/200', 'https://github.com/emma', 'token_mno'),
    ('id9', 'frank', 'frank@example.com', 'https://picsum.photos/200', 'https://github.com/frank', 'token_pqr'),
    ('id10', 'grace', 'grace@example.com', 'https://picsum.photos/200', 'https://github.com/grace', 'token_stu');