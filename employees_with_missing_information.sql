'''
Write an SQL query to report the IDs of all the employees with missing information. The information of an employee is missing if:

The employee's name is missing, or
The employee's salary is missing.
Return the result table ordered by employee_id in ascending order.

The query result format is in the following example.
'''


# Write your MySQL query statement below


select salaries.employee_id from salaries where salaries.employee_id not in (select employee_id from employees)

union

select employees.employee_id from employees where  employees.employee_id not in (select salaries.employee_id from salaries)

order by 1 asc
