'''
Write an SQL query that reports all the possible matches of the league. Note that 
every two teams play two matches with each other, with one team being the home_team once and the other time being the away_team.

Return the result table in any order.

The query result format is in the following example.
'''


select  t1.team_name as home_team, t2.team_name as away_team

 from teams t1 cross join teams t2

 where t1.team_name != t2.team_name
