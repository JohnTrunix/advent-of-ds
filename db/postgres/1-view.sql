CREATE OR REPLACE VIEW leaderboard AS
WITH ranked_submissions AS (
    SELECT
        user_uuid,
        username,
        profile_url,
        avatar_url,
        task_1,
        task_2,
        duration,
        challenge_uuid,
        ROW_NUMBER() OVER (PARTITION BY challenge_uuid ORDER BY duration) AS duration_rank
    FROM
        submissions
        LEFT JOIN users ON submissions.user_uuid = users.uuid
),
intermediate_sums AS (
    SELECT
        user_uuid,
        username,
        profile_url,
        avatar_url,
        SUM(CASE WHEN task_1 THEN 1 ELSE 0 END + CASE WHEN task_2 THEN 1 ELSE 0 END) AS score,
        SUM(CASE WHEN duration_rank = 1 THEN 1 ELSE 0 END) AS mate
    FROM
        ranked_submissions
    GROUP BY
        user_uuid, username, profile_url, avatar_url
)
SELECT
    user_uuid,
    username,
    profile_url,
    avatar_url,
    score,
    mate,
    score + mate AS total
FROM
    intermediate_sums
ORDER BY
    total DESC;
