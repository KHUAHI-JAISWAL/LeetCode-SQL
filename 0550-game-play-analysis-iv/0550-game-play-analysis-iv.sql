/* Write your PL/SQL query statement below */
SELECT ROUND(
       (
        SELECT COUNT(DISTINCT a.player_id)
        FROM Activity a
        JOIN (
            SELECT player_id,
                   MIN(event_date) AS first_login
            FROM Activity
            GROUP BY player_id
        ) b
        ON a.player_id = b.player_id
        AND a.event_date = b.first_login + 1
       )
       /
       (SELECT COUNT(DISTINCT player_id)
        FROM Activity),
       2
       ) AS fraction
FROM dual;