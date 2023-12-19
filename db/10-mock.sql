-- Insert mock data into the users table
INSERT INTO users (uuid, github_id, username, email, avatar_url, profile_url, oauth_token)
VALUES
    ('f47f1b5c-d2d4-4e7d-9b59-8a0d7c9a1e85', 'id1', 'max.hello', 'max@muster', 'https://picsum.photos/200', 'https://github.com/max.hello', 'token_123'),
    ('7f21344d-246a-4a76-8f25-950b23a0d1d4', 'id2', 'john.doe', 'john@example.com', 'https://picsum.photos/200', 'https://github.com/john.doe', 'token_456'),
    ('ac9d3d2a-839b-4a9c-a6ab-893f9b27efcc', 'id3', 'jane.smith', 'jane@example.com', 'https://picsum.photos/200', 'https://github.com/jane.smith', 'token_789'),
    ('15ebcd4d-8b18-45d2-9903-88146ad8109a', 'id4', 'alice', 'alice@example.com', 'https://picsum.photos/200', 'https://github.com/alice', 'token_abc'),
    ('c5a1c93e-16e0-4f6a-8e84-38a84f3c670c', 'id5', 'bob', 'bob@example.com', 'https://picsum.photos/200', 'https://github.com/bob', 'token_def'),
    ('e66a2672-29b4-4a57-b95e-21d6bae1fe94', 'id6', 'charlie', 'charlie@example.com', 'https://picsum.photos/200', 'https://github.com/charlie', 'token_ghi'),
    ('d06db89f-0f07-4db1-9bda-4260e4c54d1c', 'id7', 'david', 'david@example.com', 'https://picsum.photos/200', 'https://github.com/david', 'token_jkl'),
    ('1cf3d15f-7677-4a8a-9af1-dc54e4975581', 'id8', 'emma', 'emma@example.com', 'https://picsum.photos/200', 'https://github.com/emma', 'token_mno'),
    ('372a24fe-1698-49ce-9903-aa34ed63591b', 'id9', 'frank', 'frank@example.com', 'https://picsum.photos/200', 'https://github.com/frank', 'token_pqr'),
    ('ff4959f4-4e6a-4a82-8e87-eb16f5378a04', 'id10', 'grace', 'grace@example.com', 'https://picsum.photos/200', 'https://github.com/grace', 'token_stu');

-- Insert mock data into the challenges table
INSERT INTO challenges (uuid, title, tags, open_at, created_by)
VALUES
    ('cb9dcd1f-d2c4-40ed-a255-c240178ce789', 'Day 1', ARRAY['math'], '2024-12-01 07:00:00', 'david'),
    ('3d73c233-2c0e-44f1-861f-d1b3c5a2b9f1', 'Day 2', ARRAY['statistics', 'math'], '2024-12-02 07:00:00', 'frank'),
    ('34dd7273-166d-403c-8ac5-747234e51a1a', 'Day 3', ARRAY['viz'], '2024-12-03 07:00:00', 'grace'),
    ('4cc6368d-004f-4fbf-88e7-1e5d0314c1d6', 'Day 4', ARRAY['python'], '2024-12-04 07:00:00', 'frank'),
    ('f2055f10-92c8-4c93-a064-c133ce450b24', 'Day 5', ARRAY['math'], '2024-12-05 07:00:00', 'bob'),
    ('e1423bb7-4dbb-4e54-a3e8-448731d4e5b5', 'Day 6', ARRAY['math'], '2024-12-06 07:00:00', 'frank'),
    ('a8e2e1d3-642a-4ab4-8e32-0b8b7a7765c1', 'Day 7', ARRAY['R', 'python'], '2024-12-07 07:00:00', 'grace'),
    ('6edec036-ee9a-4db7-8f08-2e53420a3d6a', 'Day 8', ARRAY['excel'], '2024-12-08 07:00:00', 'frank'),
    ('f453a4f3-cdea-4f6a-9e2d-2c6cc188a7d5', 'Day 9', ARRAY['python'], '2024-12-09 07:00:00', 'grace'),
    ('d99e24e8-d41c-4bd2-8320-d489b9005f07', 'Day 10', ARRAY['sql'], '2024-12-10 07:00:00', 'frank'),
    ('8a3f62bf-02c9-4e34-8f23-bf1d03f8a77d', 'Day 11', ARRAY['math'], '2024-12-11 07:00:00', 'grace'),
    ('7543f8cc-88fb-4f23-9469-e5016873d79a', 'Day 12', ARRAY['python'], '2024-12-12 07:00:00', 'frank'),
    ('3d2d9d19-e0a8-40cf-b87d-d647b95a7819', 'Day 13', ARRAY['math'], '2024-12-13 07:00:00', 'grace'),
    ('2e4a7b39-072c-428a-813c-ee7173f0c4d3', 'Day 14', ARRAY['ethics'], '2024-12-14 07:00:00', 'frank'),
    ('3a4bfbc8-e747-431f-b2c6-70df05b5c6c5', 'Day 15', ARRAY['excel'], '2024-12-15 07:00:00', 'grace'),
    ('394cf17e-b0b2-4e0f-a376-ea0f8472ff45', 'Day 16', ARRAY['R'], '2024-12-16 07:00:00', 'charlie'),
    ('8a66350a-1159-493a-a72e-1c0c3f1e8a2d', 'Day 17', ARRAY['python', 'R', 'statistics'], '2024-12-17 07:00:00', 'grace'),
    ('7f3f7db4-d43c-429d-9bb1-dc88be55c7f7', 'Day 18', ARRAY['sql'], '2024-12-18 07:00:00', 'frank'),
    ('c85d7d2b-4f7c-42e1-9f5f-01cb94da2d04', 'Day 19', ARRAY['statistics', 'math'], '2024-12-19 07:00:00', 'grace'),
    ('9ccf5ba9-98b6-4e64-944f-b38efc38b425', 'Day 20', ARRAY['math'], '2024-12-20 07:00:00', 'frank'),
    ('9d58b007-565b-43c6-bb9c-7d4f2faa63a4', 'Day 21', ARRAY['python'], '2024-12-21 07:00:00', 'bob'),
    ('03d2a36b-11ef-4d32-9df4-ffde6a9e63fb', 'Day 22', ARRAY['python', 'R'], '2024-12-22 07:00:00', 'frank'),
    ('d54d18d8-b6af-447d-9af4-4c4bf0ec2073', 'Day 23', ARRAY['python', 'math'], '2024-12-23 07:00:00', 'jane.smith'),
    ('c2b54d1a-8e5d-47ef-97f8-731d31e09a4c', 'Day 24', ARRAY['X-mas Special!'], '2024-12-24 07:00:00', 'frank');

-- Insert mock data into the submissions table
INSERT INTO submissions (uuid, user_uuid, challenge_uuid, opened_at, closed_at, task_1, task_2)
VALUES
    -- Challenge 1
    ('a1b2c3d4-e5f6-4a7b-8c9d-0e1f2a3b4c5d', 'f47f1b5c-d2d4-4e7d-9b59-8a0d7c9a1e85', 'cb9dcd1f-d2c4-40ed-a255-c240178ce789', '2024-12-01 07:00:00', '2024-12-01 10:00:00', TRUE, TRUE),
    ('b1b2c3d4-e5f6-4a7b-8c9d-0e1f2a3b4c5d', '7f21344d-246a-4a76-8f25-950b23a0d1d4', 'cb9dcd1f-d2c4-40ed-a255-c240178ce789', '2024-12-01 07:00:00', NULL, TRUE, FALSE),
    ('c1b2c3d4-e5f6-4a7b-8c9d-0e1f2a3b4c5d', 'ac9d3d2a-839b-4a9c-a6ab-893f9b27efcc', 'cb9dcd1f-d2c4-40ed-a255-c240178ce789', '2024-12-01 07:00:00', NULL, FALSE, TRUE),
    ('d1b2c3d4-e5f6-4a7b-8c9d-0e1f2a3b4c5d', '15ebcd4d-8b18-45d2-9903-88146ad8109a', 'cb9dcd1f-d2c4-40ed-a255-c240178ce789', '2024-12-01 07:00:00', '2024-12-01 11:30:00', TRUE, TRUE),
    ('e1b2c3d4-e5f6-4a7b-8c9d-0e1f2a3b4c5d', 'c5a1c93e-16e0-4f6a-8e84-38a84f3c670c', 'cb9dcd1f-d2c4-40ed-a255-c240178ce789', '2024-12-01 07:00:00', '2024-12-01 09:45:00', TRUE, TRUE),

    -- Challenge 2
    ('f1b2c3d4-e5f6-4a7b-8c9d-0e1f2a3b4c5d', 'f47f1b5c-d2d4-4e7d-9b59-8a0d7c9a1e85', '3d73c233-2c0e-44f1-861f-d1b3c5a2b9f1', '2024-12-02 07:00:00', '2024-12-02 10:30:00', TRUE, TRUE),
    ('f2b2c3d4-e5f6-4a7b-8c9d-0e1f2a3b4c5d', '7f21344d-246a-4a76-8f25-950b23a0d1d4', '3d73c233-2c0e-44f1-861f-d1b3c5a2b9f1', '2024-12-02 07:00:00', NULL, TRUE, FALSE),
    ('f3b2c3d4-e5f6-4a7b-8c9d-0e1f2a3b4c5d', 'ac9d3d2a-839b-4a9c-a6ab-893f9b27efcc', '3d73c233-2c0e-44f1-861f-d1b3c5a2b9f1', '2024-12-02 07:00:00', NULL, FALSE, TRUE),
    ('f4b2c3d4-e5f6-4a7b-8c9d-0e1f2a3b4c5d', '15ebcd4d-8b18-45d2-9903-88146ad8109a', '3d73c233-2c0e-44f1-861f-d1b3c5a2b9f1', '2024-12-02 07:00:00', '2024-12-02 11:15:00', TRUE, TRUE),
    ('f5b2c3d4-e5f6-4a7b-8c9d-0e1f2a3b4c5d', 'c5a1c93e-16e0-4f6a-8e84-38a84f3c670c', '3d73c233-2c0e-44f1-861f-d1b3c5a2b9f1', '2024-12-02 07:00:00', NULL, FALSE, TRUE),

    -- Challenge 3
    ('a1b2c3d4-e5f6-4a7b-7c9d-0e1f2a3b4c5d', 'f47f1b5c-d2d4-4e7d-9b59-8a0d7c9a1e85', '34dd7273-166d-403c-8ac5-747234e51a1a', '2024-12-02 07:00:00', '2024-12-02 10:30:00', TRUE, TRUE),
    ('b2b2c3d4-e5f6-4a7b-7c9d-0e1f2a3b4c5d', '7f21344d-246a-4a76-8f25-950b23a0d1d4', '34dd7273-166d-403c-8ac5-747234e51a1a', '2024-12-02 07:00:00', NULL, TRUE, FALSE),
    ('c3b2c3d4-e5f6-4a7b-7c9d-0e1f2a3b4c5d', 'ac9d3d2a-839b-4a9c-a6ab-893f9b27efcc', '34dd7273-166d-403c-8ac5-747234e51a1a', '2024-12-02 07:00:00', NULL, FALSE, TRUE),
    ('550e8400-e29b-41d4-a716-446655440000', '15ebcd4d-8b18-45d2-9903-88146ad8109a', '34dd7273-166d-403c-8ac5-747234e51a1a', '2024-12-02 07:00:00', '2024-12-02 11:15:00', TRUE, TRUE);