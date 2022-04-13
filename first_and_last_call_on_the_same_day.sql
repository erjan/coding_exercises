
'''
Write an SQL query to report the IDs of the users whose first and last calls on any day were with the same person. Calls are counted regardless of being the caller or the recipient.

Return the result table in any order.

The query result format is in the following example.
'''

with all_Callers as (
select caller_id user_id, recipient_id as reciever_id  , call_time from Calls
union 
select recipient_id v, caller_id as  reciever_id ,call_time from Calls
)

,first_last_caller as ( 
select
distinct
user_id ,
first_value(reciever_id) over (partition by user_id,date(call_time) order by call_time) first_recipient_id,
first_value(reciever_id) over (partition by user_id,date(call_time) order by  call_time desc) last_recipient_id   
from all_Callers
)

select 
user_id
from
first_last_caller
where first_recipient_id = last_recipient_id
group by user_id
----------------------------

WITH CTE AS (
                SELECT caller_id AS user_id, call_time, recipient_id FROM Calls
                UNION 
                SELECT recipient_id AS user_id, call_time, caller_id AS recipient_id FROM Calls
            ),

CTE1 AS (
        SELECT 
        user_id,
        recipient_id,
        DATE(call_time) AS DAY,
        DENSE_RANK() OVER(PARTITION BY user_id, DATE(call_time) ORDER BY call_time ASC) AS RN,
        DENSE_RANK() OVER(PARTITION BY user_id, DATE(call_time) ORDER BY call_time DESC) AS RK
        FROM CTE
        )

SELECT DISTINCT user_id
FROM CTE1
WHERE RN = 1 OR RK = 1
GROUP BY user_id, DAY
HAVING COUNT(DISTINCT recipient_id) = 1
