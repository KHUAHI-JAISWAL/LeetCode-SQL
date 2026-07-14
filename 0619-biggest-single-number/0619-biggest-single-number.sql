/* Write your PL/SQL query statement below */
SELECT (
    SELECT MAX(num)
    FROM (
        SELECT num
        FROM MyNumbers
        GROUP BY num
        HAVING COUNT(*) = 1
    )
) AS num
FROM dual;