# Write your MySQL query statement below
'''
Write an SQL query to report the first login date for each player.

Return the result table in any order.

The query result format is in the following example.
'''

select player_id, min(event_date) as first_login 

from activity 

group by player_id

order by first_login   
