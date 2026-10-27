# Write your MySQL query statement below
select w1.id as id 
from weather w1
inner join weather w2
on DateDIFF(w1.recordDate ,w2.recorddate) =1
where w1.temperature >w2.temperature;


