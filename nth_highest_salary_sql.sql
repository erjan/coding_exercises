'''
Write an SQL query to report the nth highest salary from the Employee table. If there is no nth highest salary, the query should report null.

The query result format is in the following example.
'''

CREATE FUNCTION getNthHighestSalary(@N INT) RETURNS INT AS
BEGIN
    RETURN (
        
        select salary from (
        select distinct salary from Employee 
        order by salary desc
        offset @N-1 row
        fetch next 1 row only) k
        
    );
END
