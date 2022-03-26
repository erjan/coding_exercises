# Write your MySQL query statement below

'''
Write an SQL query to calculate the bonus of each employee. The bonus of an 
employee is 100% of their salary if the ID of the employee is an odd number and the employee name does not 
start with the character 'M'. The bonus of an employee is 0 otherwise.

Return the result table ordered by employee_id.

The query result format is in the following example.
'''


select employee_id ,

case 
    when employee_id % 2 = 1 and name not like 'M%' then salary  
    else 0
    
    end
    
    as bonus

from employees
