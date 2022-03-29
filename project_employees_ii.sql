'''
Write an SQL query that reports all the projects that have the most employees.

Return the result table in any order.

The query result format is in the following example.
'''

select project_id
from project

group by project_id   
having count(employee_id) = ( 


select count(employee_id) as c

from project
group by project_id
order by c desc limit 1)


#another solution

select project_id
from project 
group by project_id
having count(employee_id) = 
     (select max(cnt) 
      from (select project_id, count(distinct employee_id) as cnt
            from project
            group by project_id) as t1)
