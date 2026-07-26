
CREATE FUNCTION getNthHighestSalary(N IN NUMBER) RETURN NUMBER IS
result NUMBER;
BEGIN  
    SELECT MAX(salary)
    INTO result
    FROM (
        SELECT salary,
               DENSE_RANK() OVER (ORDER BY salary DESC) AS rnk
        FROM Employee
    )
    WHERE rnk = N;
    


    

    RETURN result;
END;

   