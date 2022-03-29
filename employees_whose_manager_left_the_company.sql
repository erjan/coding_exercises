'''
Write an SQL query to report the IDs of the employees whose salary is strictly less than $30000 and whose manager left the company. When a manager leaves the company, their information is deleted from the Employees table, but the reports still have their manager_id set to the manager that left.

Return the result table ordered by employee_id.

The query result format is in the following example.
'''



SELECT DISTINCT emp.employee_id
FROM   employees emp
       LEFT JOIN employees mng
              ON( emp.manager_id = mng.employee_id )
WHERE  emp.manager_id IS NOT NULL
       AND emp.salary < 30000
       AND mng.employee_id IS NULL
ORDER  BY emp.employee_id 
