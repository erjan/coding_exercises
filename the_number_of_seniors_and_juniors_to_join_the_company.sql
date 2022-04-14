'''

A company wants to hire new employees. The budget of the company for the salaries is $70000. The company's criteria for hiring are:

Hiring the largest number of seniors.
After hiring the maximum number of seniors, use the remaining budget to hire the largest number of juniors.
Write an SQL query to find the number of seniors and juniors hired under the mentioned criteria.

Return the result table in any order.

The query result format is in the following example.

'''

WITH CTE AS (SELECT employee_id, experience, SUM(salary) OVER(PARTITION BY experience ORDER BY salary,employee_id ASC) AS RN FROM Candidates)
      
SELECT 'Senior' AS experience, COUNT(employee_id) AS accepted_candidates FROM CTE WHERE experience = 'Senior' AND RN < 70000
UNION
SELECT 'Junior' AS experience, COUNT(employee_id) AS accepted_candidates FROM CTE WHERE experience = 'Junior' AND RN < (SELECT 70000 - IFNULL(MAX(RN),0) FROM CTE WHERE experience = 'Senior' AND RN < 70000)

----------------------------

# sum by experience order by salary
with rank_table as (
    select  experience, 
            sum(salary) over (partition by experience order by salary) count_salary
    from Candidates c
)
,
# get money spent + num of seniors
senior_table as (
    select max(count_salary) count_salary, count(*) num_of_seniors 
    from rank_table
    where experience = 'Senior'
    and count_salary <= 70000
)
,
# calculate num of juniors by remain money
junior_table as(
    select count(*) num_of_juniors
    from rank_table
    where experience = 'Junior' 
    and count_salary <= (select 70000-ifnull(count_salary, 0) from senior_table)
)

# union together
select 'Senior' experience, num_of_seniors accepted_candidates
from senior_table
union all
select 'Junior' experience, num_of_juniors accepted_candidates
from junior_table


-----------------------------------------------------------------------

with seniors as (
select employee_id, salary, sum(salary) over (order by salary asc) as running_salary 
    from candidates 
    where experience = 'Senior'
), hired_seniors as (
    select count(distinct employee_id) as accepted_candidates
    from seniors 
    where running_salary <= 70000
)
, calc_salary as (select max(running_salary) as senior_salaries from
                 seniors where running_salary <= 70000)
, juniors as (
select employee_id, salary, sum(salary) over (order by salary asc) as running_salary 
    from candidates 
    where experience = 'Junior'
),
hired_juniors as (
    select count(distinct employee_id) as accepted_candidates
    from juniors 
    cross join calc_salary c
    where running_salary <= (70000 - isnull(c.senior_salaries,0))
)
select 'Senior' as experience, accepted_candidates from hired_seniors
union all
select 'Junior' as experience, accepted_candidates from hired_juniors
