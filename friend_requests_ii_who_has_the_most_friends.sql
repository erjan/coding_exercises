'''

Write an SQL query to find the people who have the most friends and the most friends number.

The test cases are generated so that only one person has the most friends.

The query result format is in the following example.

'''



SELECT id, COUNT(DISTINCT id2) AS num FROM (
SELECT requester_id AS id,accepter_id AS id2 from RequestAccepted
UNION 
SELECT accepter_id AS id,requester_id AS id2 from RequestAccepted) A
GROUP BY id ORDER BY num DESC LIMIT 1;

----------------------

select id, count(*) as num from(
select requester_id id from request_accepted
union all 
    select accepter_id id from request_accepted) t
group by id
order by num desc limit 1 
---------------------------------

select id, sum(cnt) as num

from
(
(select requester_id as id, count(*) as cnt
from request_accepted
group by requester_id) 
union all
(
select accepter_id as id, count(*) as cnt
from request_accepted
group by accepter_id) 
    ) as base
    
group by id

order by num desc

limit 1
