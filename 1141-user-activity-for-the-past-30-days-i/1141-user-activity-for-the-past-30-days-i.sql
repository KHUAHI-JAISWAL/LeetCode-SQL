/* Write your PL/SQL query statement below */

SELECT TO_CHAR(activity_date, 'YYYY-MM-DD') AS day,
       COUNT(DISTINCT user_id) AS active_users
FROM Activity
WHERE activity_date >= DATE '2019-06-28'
  AND activity_date <= DATE '2019-07-27'
GROUP BY TO_CHAR(activity_date, 'YYYY-MM-DD');