
CREATE FUNCTION getNthHighestSalary(N IN NUMBER) RETURN NUMBER IS
result NUMBER;
BEGIN  
    select max(Salary)
    into result
    from (
        select salary,
        dense_rank() over(order by salary DESC) 
        as rnk from employee
    )
    where rnk = N;
    return result; 
END;
