'''
For this problem, we will consider a manager an employee who has at least 1 other employee reporting to them.

Write an SQL query to report the ids and the names of all managers, the number of employees who report directly to them, and the average age of the reports rounded to the nearest integer.

Return the result table ordered by employee_id.

The query result format is in the following example.
'''

select  e1.employee_id as employee_id ,
e1.name as name,
count(*) as reports_count,
round(avg(e2.age)) as average_age

from employees e1 join employees e2 on

e1.employee_id = e2.reports_to
group by 1
order by 1
