/* Write your PL/SQL query statement below */
SELECT product_id, new_price AS price
FROM (
    SELECT product_id,
           new_price,
           ROW_NUMBER() OVER (
               PARTITION BY product_id
               ORDER BY change_date DESC
           ) AS rn
    FROM Products
    WHERE change_date <= DATE '2019-08-16'
)
WHERE rn = 1

UNION

SELECT product_id, 10 AS price
FROM Products
WHERE product_id NOT IN (
    SELECT product_id
    FROM Products
    WHERE change_date <= DATE '2019-08-16'
);