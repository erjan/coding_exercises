'''
Write an SQL query to report the name and the mail of all interview candidates. A user is an interview candidate if at least one of these two conditions is true:

The user won any medal in three or more consecutive contests.
The user won the gold medal in three or more different contests (not necessarily consecutive).
Return the result table in any order.

The query result format is in the following example.
'''


with t0 as (
    select gold_medal as user, contest_id 
    from contests 
    union all 
    select silver_medal as user, contest_id 
    from contests 
    union all 
    select bronze_medal as user, contest_id 
    from contests 
)
, t1 as (
    select user, contest_id, row_number() over(partition by user order by contest_id) as rn 
    from t0 
)
, t2 as (
    select user as user_id -- consecutive medal winners
    from t1 
    group by user, contest_id - rn 
    having count(*) >= 3 -- replace 3 with any number to solve the N problem
    union all
    select gold_medal as user_id  -- gold medal winners
    from contests 
    group by gold_medal 
    having count(*) >= 3
)
select distinct u.name, u.mail 
from t2 
inner join users u
on t2.user_id = u.user_id


-----------------------------------
select a.name, a.mail
from ( select * , lag(contest_id, 2) over
(partition by user_id order by contest_id) as lag_two
FROM
Users u
JOIN
Contests c
on u.user_id in (c.gold_medal, c.silver_medal, c.bronze_medal)
) a
group by user_id
having sum(user_id = gold_medal) >= 3 or sum(contest_id - lag_two = 2) >= 1

---------------------------------------------


kyungminlee's avatar
kyungminlee
30
September 5, 2021 6:42 AM

339 VIEWS

SELECT DISTINCT name, mail
FROM Users
JOIN (
    SELECT
        gold_medal   as g0,
        silver_medal as s0,
        bronze_medal as b0,
        LAG(gold_medal,   1) OVER (ORDER BY contest_id) AS g1,
        LAG(silver_medal, 1) OVER (ORDER BY contest_id) AS s1,
        LAG(bronze_medal, 1) OVER (ORDER BY contest_id) AS b1,
        LAG(gold_medal,   2) OVER (ORDER BY contest_id) AS g2,
        LAG(silver_medal, 2) OVER (ORDER BY contest_id) AS s2,
        LAG(bronze_medal, 2) OVER (ORDER BY contest_id) AS b2
    FROM Contests
) AS C3 ON user_id IN (g0, s0, b0) AND user_id IN (g1, s1, b1) AND user_ID IN (g2, s2, b2)

UNION

SELECT name, mail
FROM Contests
LEFT JOIN Users ON gold_medal = user_id
GROUP BY gold_medal
HAVING COUNT(1) >= 3
;
