'''

Write an SQL query to report the fraction of players that logged in again on the day after the day they first logged in, rounded to 2 decimal places. In other words, you need to count the number of players that logged in for at least two consecutive days starting from their first login date, then divide that number by the total number of players.

The query result format is in the following example.

'''


SELECT ROUND(COUNT(t2.player_id)/COUNT(t1.player_id),2) AS fraction
FROM
(SELECT player_id, MIN(event_date) AS first_login FROM Activity GROUP BY player_id) t1 LEFT JOIN Activity t2
ON t1.player_id = t2.player_id AND t1.first_login = t2.event_date - 1




#another using window function

select
    round(count(player_id) /  (select count(distinct player_id) from activity), 2) as fraction
from (
    select
        player_id,
        event_date,
        row_number() over (partition by player_id order by event_date asc) as login_rank,
        lead(event_date) over (partition by player_id order by event_date asc) as next_login
    from
        activity
) login_table
where 
 login_table.login_rank = 1 and
 login_table.next_login is not null and
 datediff(login_table.next_login, login_table.event_date) = 1
 
 
 
 ---------
 
 select round((sum(if(datediff(event_date,first_login)=1,1,0))/count(distinct player_id)),2) fraction
from (select *, min(event_date) over(partition by player_id) first_login
      from activity) t
