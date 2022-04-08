'''

Assume today's date is '2021-1-1'.

Write an SQL query that will, for each user_id, find out the largest window of days 
between each visit and the one right after it (or today if you are considering the last visit).

Return the result table ordered by user_id.

The query result format is in the following example.

'''

with s as(

select

user_id,
visit_date, 


ifnull(lead(visit_date)over(partition by user_id order by visit_date), '2021-1-1') as next
from uservisits
order by user_id),

s2 as (
select user_id,

datediff(next, visit_date) as biggest_window

from s)

select distinct user_id, biggest_window from (

select user_id, biggest_window,

rank()over(partition by user_id order by biggest_window desc) as r
from s2)k where k.r = 1
------------------------------------------------------------------------

WITH C1 AS (
SELECT user_id, visit_date,
LEAD(visit_date, 1, '2021-01-01') OVER(PARTITION BY user_id ORDER BY visit_date) AS next_visit
FROM UserVisits
)
SELECT user_id,
MAX(DATEDIFF(next_visit, visit_date)) AS biggest_window
FROM C1
GROUP BY user_id ;

--------------------------------------------------------------------------------------


with s as(
select
user_id,
visit_date, 
DATEDIFF(LEAD(visit_date, 1, '2021-01-01') OVER (PARTITION BY user_id ORDER BY visit_date), visit_date) as biggest_window 
    from uservisits
    order by user_id)

select  user_id, biggest_window from (
select 
user_id,biggest_window,
row_number() over(partition by user_id order by biggest_window desc) as r
from s)k where k.r = 1



-----------------------------------

WITH C1 AS (
SELECT user_id, visit_date,
LEAD(visit_date, 1, '2021-01-01') OVER(PARTITION BY user_id ORDER BY visit_date) AS next_visit
FROM UserVisits
)
SELECT user_id,
MAX(DATEDIFF(next_visit, visit_date)) AS biggest_window
FROM C1
GROUP BY user_id ;
