/* Write your PL/SQL query statement below */
select department, 
       employee,
       salary

from( 
    select d.name as department,
           e.name as employee,
           e.salary,
           rank() over(
                partition by e.departmentID
                order by e.salary DESC
           ) as salary_rank

    from employee e
    join department d
     on e.departmentId = d.id
           
        

           
)
where salary_rank = 1;