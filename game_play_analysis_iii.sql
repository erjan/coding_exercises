'''

Write an SQL query to report for each player and date, how many games played so far by the player. That is, the total number of games played by the player until that date. Check the example for clarity.

Return the result table in any order.

The query result format is in the following example.
'''

select 

player_id, event_date,

sum(games_played) over(partition by player_id order by event_date) as games_played_so_far 


from activity


