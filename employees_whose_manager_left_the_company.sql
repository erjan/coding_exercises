'''
Write an SQL query to report the IDs of the employees whose salary is strictly less than $30000 and whose manager left the company. When a manager leaves the company, their information is deleted from the Employees table, but the reports still have their manager_id set to the manager that left.

Return the result table ordered by employee_id.

The query result format is in the following example.
'''



SELECT DISTINCT e1.employee_id

FROM employees e1

LEFT JOIN employees e2

ON e1.manager_id = e2.employee_id 
              
WHERE  e1.manager_id IS NOT NULL

       AND e1.salary < 30000
       
       AND e2.employee_id IS NULL
       
ORDER  BY e1.employee_id 
