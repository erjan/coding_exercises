
'''

Write an SQL query to report the device that is first logged in for each player.

Return the result table in any order.

The query result format is in the following example.

'''


select player_id, device_id


from activity

where (player_id, event_date) in 


(select player_id, min(event_date) from activity

group by player_id
order by event_date asc)



#another

SELECT a.player_id
        ,a.device_id
FROM 
    (SELECT player_id
            ,min(event_date) AS min_date
    FROM Activity
    GROUP BY player_id) dt
JOIN Activity a ON a.player_id = dt.player_id
AND a.event_date = dt.min_date



#another window function - first value()

SELECT  DISTINCT player_id,
        FIRST_VALUE(device_id) OVER(PARTITION BY player_id ORDER BY event_date ASC) AS device_id 
FROM Activity 


#another window function rank()

SELECT player_id
        ,device_id
FROM 
    (SELECT player_id
            ,device_id
            ,rank() OVER(PARTITION BY player_id ORDER BY event_date) AS rnk
    FROM Activity) rnk_table
WHERE rnk_table.rnk = 1


#another

 select player_id, device_id from (
    
    select player_id, device_id, 
     
     rank() over(partition by player_id order by event_date asc) as ranky
     from activity )k
where k.ranky = 1

