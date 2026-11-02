# Write your MySQL query statement below
select e.name 
from employee e
join employee a
on e.id = a.managerId 
group by e.id, 
        e.name
having count(e.id) >=5;