'''

A company wants to hire new employees. The budget of the company for the salaries is $70000. The company's criteria for hiring are:

Keep hiring the senior with the smallest salary until you cannot hire any more seniors.
Use the remaining budget to hire the junior with the smallest salary.
Keep hiring the junior with the smallest salary until you cannot hire any more juniors.
Write an SQL query to find the ids of seniors and juniors hired under the mentioned criteria.

Return the result table in any order.

The query result format is in the following example.


'''


WITH CTE AS (SELECT employee_id, experience, SUM(salary) OVER(PARTITION BY experience ORDER BY salary ASC) AS RN FROM Candidates)
      
SELECT employee_id FROM CTE WHERE experience = 'Senior' AND RN < 70000
UNION
SELECT employee_id FROM CTE WHERE experience = 'Junior' AND RN < (SELECT 70000 - IFNULL(MAX(RN),0) FROM CTE WHERE experience = 'Senior' AND RN < 70000)


-------------------------
with sal_cte
as
(
/* CTE to calculate running salary total*/
select employee_id, experience, salary,
sum(salary) over (partition by experience order by salary) as tot_sal
from Candidates
),
senior_cte
as
(
/* CTE to extract senior employees below 70000 running total*/
select employee_id, experience, salary, tot_sal
from sal_cte
where tot_sal <= 70000 and experience = 'Senior'
),
junior_cte
as
(
/* CTE to extract junior employees for remaning 70000*/
select employee_id, experience, salary
from sal_cte
where tot_sal < (select ifnull(70000-max(tot_sal),70000) from senior_cte)
and experience = 'Junior'
)
/* CTE to union results from senior and junior cte*/
select employee_id from senior_cte
union
select employee_id from junior_cte

---------------------------------------
      
      with cte as (
select *, sum(salary) over (partition by experience order by salary) as cum_sum
   from Candidates
),
cte_s as (
select employee_id, salary from cte 
    where experience='Senior' and cum_sum<=70000
)

select employee_id from cte_s
union
select employee_id from cte 
    where experience='Junior' and cum_sum<=70000-(select coalesce(sum(salary),0) from cte_s)
      
      ----------------------------------------------------------
      
      WITH seniors AS
(

SELECT
    employee_id,
    running_salary
FROM
(
    SELECT
        employee_id,
        SUM(salary) OVER (ORDER BY salary ASC) as running_salary
    FROM
        Candidates
    WHERE
        experience = 'Senior'
)t
WHERE running_salary <= 70000
),


remaining_budget AS
(
SELECT CASE WHEN (SELECT MAX(running_salary) FROM seniors) IS NOT NULL THEN 70000 - (SELECT MAX(running_salary) FROM seniors)
    ELSE 70000 END AS remaining_amount

),


juniors AS

(

SELECT
    employee_id
FROM
(
    SELECT
        employee_id,
        SUM(salary) OVER (ORDER BY salary ASC) as running_salary
    FROM
        Candidates
    WHERE
        experience = 'Junior'    
)T
WHERE running_salary <= (SELECT remaining_amount FROM remaining_budget)

)
SELECT employee_id FROM seniors UNION ALL SELECT * FROM juniors
