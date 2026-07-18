/* Write your PL/SQL query statement below */
Select (
    select max(num)
    from (
        select num
        from mynumbers
        group by num
        having count(*) = 1
    )
) as num
from dual;


    
