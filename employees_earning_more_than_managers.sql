'''
Write an SQL query to find the employees who earn more than their managers.

Return the result table in any order.

The query result format is in the following example.
'''

select e.name as Employee from employee e inner join employee e2 on e.managerId = e2.id

where e.salary > e2.salary

#wrong solution

select e.name as Employee from employee e inner join employee e2 on e.id = e2.managerId

where e.salary > e2.salary
