	'''
  Employees can belong to multiple departments. When the employee joins other departments, they need to decide which department is their primary department. Note that when an employee belongs to only one department, their primary column is 'N'.

Write an SQL query to report all the employees with their primary department. For employees who belong to one department, report their only department.

Return the result table in any order.

The query result format is in the following example.
'''
  
  
  select
	distinct employee_id
	, first_value(department_id) over (partition by employee_id order by primary_flag) as department_id
	from
	Employee
  
  
  
  select 
employee_id,
department_id
from Employee o
where primary_flag = 'Y'
or employee_id in (select employee_id from Employee group by employee_id having count(employee_id)=1 )
