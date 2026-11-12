# Write your MySQL query statement below
select round
          (count(distinct b.player_id)/
          count(distinct a.player_id),
          2
          ) as fraction
from
(select
        player_id , 
        min(event_date) as first_login
        
from activity
group by player_id
) a
left join activity  b
on a.player_id = b.player_id
and b.event_date = date_add(a.first_login,interval 1 day)