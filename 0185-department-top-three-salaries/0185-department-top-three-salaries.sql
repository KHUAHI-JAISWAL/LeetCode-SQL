/* Write your PL/SQL query statement below */

SELECT d.name AS department,
       e.name AS employee,
       e.salary AS salary
FROM (
    SELECT name,
           salary,
           departmentId,
           DENSE_RANK() OVER (
               PARTITION BY departmentId
               ORDER BY salary DESC
           ) AS rnk
    FROM Employee
) e
JOIN Department d
    ON e.departmentId = d.id
WHERE e.rnk <= 3
ORDER BY d.name, e.salary DESC;