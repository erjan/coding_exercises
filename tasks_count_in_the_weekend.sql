'''
Write an SQL query to report:

the number of the tasks that were submitted during the weekend (Saturday, Sunday) as weekend_cnt, and
the number of the tasks that were submitted during the working days as working_cnt.
Return the result table in any order.

The query result format is shown in the following example.
'''

with cte as(

select count(*) as num, dayname(submit_date) as day from tasks

group by day),

cte2 as(
select 
case when day in ('Saturday', 'Sunday') then num else 0 end as weekend_cnt,
case when day not in ('Saturday', 'Sunday') then num else 0 end as working_cnt
from cte)

select sum(weekend_cnt) as weekend_cnt, sum(working_cnt) as working_cnt from cte2


-----------------------------------------
# Write your MySQL query statement below
SELECT SUM(WEEKDAY(submit_date)>=5) AS weekend_cnt,
SUM(WEEKDAY(submit_date)<5) AS working_cnt
FROM Tasks;
