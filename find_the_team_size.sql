'''
Write an SQL query to find the team size of each of the employees.

Return result table in any order.

The query result format is in the following example.
'''

#my own solution

with helper as
(select  team_id, count(employee_id) as team_size from employee

group by  team_id)


select employee_id, team_size from helper join employee where
employee.team_id = helper.team_id




#another solution

select e.employee_id, (select count(team_id) from Employee where e.team_id = team_id) as team_size
from Employee e
