# Write your MySQL query statement below

select p.product_id ,
        round(coalesce(sum(p.price*u.units)/NullIF(sum(u.units),0),0),
        2
        ) as average_price
from prices p
left join UnitsSold U
on p.product_id = u.product_id 
and u.purchase_date between p.start_date and p.end_date
group by  product_id ;
