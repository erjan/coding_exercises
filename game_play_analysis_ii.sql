
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

