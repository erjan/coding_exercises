'''
Write an SQL query to find employees who have the highest salary in each of the departments.

Return the result table in any order.

The query result format is in the following example.
'''

select Department, Employee, Salary from (

SELECT 
   d.name as Department, 
   e.name as Employee, 
   e.salary as Salary,
   dense_rank() OVER (PARTITION BY d.id ORDER BY salary DESC) AS rn
   
    FROM department d inner join employee e on e.departmentId = d.id)tmp
    
    where rn <=1
