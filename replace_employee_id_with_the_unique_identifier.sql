'''
Write an SQL query to show the unique ID of each user, If a user does not have a unique ID replace just show null.

Return the result table in any order.

The query result format is in the following example.
'''


select employeeuni.unique_id, name from employees 

left join employeeuni using(id)
