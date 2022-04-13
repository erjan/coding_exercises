'''
The install date of a player is the first login day of that player.

We define day one retention of some date x to be the number of players whose install date is x and they logged back in on the day right after x, divided by the number of players whose install date is x, rounded to 2 decimal places.

Write an SQL query to report for each install date, the number of players that installed the game on that day, and the day one retention.

Return the result table in any order.

The query result format is in the following example.
'''



SELECT install_dt, COUNT(player_id) AS installs,
ROUND(COUNT(next_day) / COUNT(player_id), 2) AS Day1_retention
FROM (
    SELECT a1.player_id, a1.install_dt, a2.event_date AS next_day
    FROM
    (
        SELECT player_id, MIN(event_date) AS install_dt 
        FROM Activity
        GROUP BY player_id
    ) AS a1 
    LEFT JOIN Activity AS a2
    ON a1.player_id = a2.player_id
    AND a2.event_date = a1.install_dt + 1
) AS t
GROUP BY install_dt;

------------------------------------------------
select A.event_date as install_dt, count(A.player_id) as installs, round(count(B.player_id)/count(A.player_id),2) as Day1_retention
from (select player_id, min(event_date) AS event_date from Activity group by player_id) AS A
left join Activity B
ON A.player_id = B.player_id
and A.event_date + 1 = B.event_Date
group by A.event_date

-----------------------------
select a.install_date as install_dt, 
			count(distinct a.player_id) as installs, 
			round(count(distinct b.player_id)*1.0/count(distinct a.player_id), 2) as Day1_retention
from (select player_id, min(event_date) as install_date
			from Activity
			group by 1) a
left join Activity b 
on a.player_id = b.player_id and a.install_date = b.event_date - 1
group by 1
