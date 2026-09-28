/* Write your PL/SQL query statement below */
select 
      contest_id,
      round(count(user_id)*100/(select count(*)from users),2) as percentage

from register r
group by contest_id
order by percentage DESC , contest_id ASC;