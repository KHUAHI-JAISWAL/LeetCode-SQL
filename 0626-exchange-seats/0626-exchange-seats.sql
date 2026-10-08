/* Write your PL/SQL query statement below */
 SELECT id,
       CASE
           WHEN MOD(id, 2) = 1 THEN
               LEAD(student, 1, student) OVER (ORDER BY id)
           ELSE
               LAG(student) OVER (ORDER BY id)
       END AS student
FROM Seat
ORDER BY id;