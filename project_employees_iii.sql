'''


Write an SQL query that reports the most experienced employees in each project. In case of a tie, report all 
employees with the maximum number of experience years.

Return the result table in any order.

The query result format is in the following example.

 
 
'''



with employee_experience as (
    select p.project_id, p.employee_id,
    rank() over(partition by p.project_id order by experience_years desc) as rank
    from Project p join Employee e
    on p.employee_id = e.employee_id)

select project_id, employee_id
from employee_experience
where rank = 1;
