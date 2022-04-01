'''

Write an SQL query to report the fraction of players that logged in again on the day after the day they first logged in, rounded to 2 decimal places. In other words, you need to count the number of players that logged in for at least two consecutive days starting from their first login date, then divide that number by the total number of players.

The query result format is in the following example.

'''


SELECT ROUND(COUNT(t2.player_id)/COUNT(t1.player_id),2) AS fraction
FROM
(SELECT player_id, MIN(event_date) AS first_login FROM Activity GROUP BY player_id) t1 LEFT JOIN Activity t2
ON t1.player_id = t2.player_id AND t1.first_login = t2.event_date - 1
