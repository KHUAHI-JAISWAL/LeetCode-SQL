/* Write your PL/SQL query statement below */

select product_id,year as first_year , quantity , price
from(
    select product_id ,  year , quantity, price,
    rank() over(partition by product_id order by year) as rnk
    from sales

)where rnk = 1;
