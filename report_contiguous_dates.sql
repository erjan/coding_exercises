'''
A system is running one task every day. Every task is independent of the previous tasks. The tasks can fail or succeed.

Write an SQL query to generate a report of period_state for each continuous interval of days in the period from 2019-01-01 to 2019-12-31.

period_state is 'failed' if tasks in this interval failed or 'succeeded' if tasks in this interval succeeded. Interval of days are retrieved as start_date and end_date.

Return the result table ordered by start_date.

The query result format is in the following example.

 
 '''



The idea here is to use row_number to get a unique grouping label for each continous sequence.
We can then easily find the min/max dates in each group

with a  as (
(select fail_date as date,
       'failed' as period_state
       from failed)
union all
 
 (select success_date as date,
         'succeeded' as period_state
         from succeeded)
    ),
    
  b as (    
select date,
       period_state,
       row_number() over (order by period_state, date asc) as seq
   from a where date between '2019-01-01' and '2019-12-31'
         ),

 c as (
select date, period_state,seq, dateadd(d, -seq, date) as seqStart from b
)

select period_state, min(date) as start_date, max(date) as end_date from c
group by seqStart,period_state
order by start_date asc

-----------------------------

SELECT stats AS period_state, MIN(day) AS start_date, MAX(day) AS end_date
FROM (
    SELECT 
        day, 
        RANK() OVER (ORDER BY day) AS overall_ranking, 
        stats, 
        rk, 
        (RANK() OVER (ORDER BY day) - rk) AS inv
    FROM (
        SELECT fail_date AS day, 'failed' AS stats, RANK() OVER (ORDER BY fail_date) AS rk
        FROM Failed
        WHERE fail_date BETWEEN '2019-01-01' AND '2019-12-31'
        UNION 
        SELECT success_date AS day, 'succeeded' AS stats, RANK() OVER (ORDER BY success_date) AS rk
        FROM Succeeded
        WHERE success_date BETWEEN '2019-01-01' AND '2019-12-31') t
    ) c
GROUP BY inv, stats
ORDER BY start_date

--------------------------------------------
with main as (
select 'failed' as flag,fail_date as date1 from failed where fail_date between '2019-01-01' and '2019-12-31'
union all
select 'succeeded' as flag,success_date as date1 from succeeded where success_date between '2019-01-01' and '2019-12-31'),
mappings as(
select *, dense_rank() over (order by date1) - dense_rank() over (partition by flag order by date1) as mappings  from main)


select 
flag as period_state ,min(date1) as start_date,max(date1) as end_date
from 
mappings
group by flag,mappings
order by start_date
