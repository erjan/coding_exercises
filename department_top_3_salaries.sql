'''
A company's executives are interested in seeing who earns the most money in each of the company's departments. A high earner in a department is an employee who has a salary in the top three unique salaries for that department.

Write an SQL query to find the employees who are high earners in each of the departments.

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
    
    where rn <=3
