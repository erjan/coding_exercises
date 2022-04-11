'''
Write an SQL query to report the statistics of the league. The statistics should be built using the played matches where the winning team gets three points and the losing team gets no points. If a match ends with a draw, both teams get one point.

Each row of the result table should contain:

team_name - The name of the team in the Teams table.
matches_played - The number of matches played as either a home or away team.
points - The total points the team has so far.
goal_for - The total number of goals scored by the team across all matches.
goal_against - The total number of goals scored by opponent teams against this team across all matches.
goal_diff - The result of goal_for - goal_against.
Return the result table ordered by points in descending order. If two or more teams have the same points, order them by goal_diff in descending order. If there is still a tie, order them by team_name in lexicographical order.

The query result format is in the following example.

'''


select team_name,
sum(case when home_team_id = team_id or away_team_id = team_id then 1 else 0 end) as matches_played,
sum(case when team_id = home_team_id and home_team_goals > away_team_goals then 3 when team_id = away_team_id and home_team_goals < away_team_goals then 3 when home_team_goals = away_team_goals then 1 else 0 end) as points,
sum(case when home_team_id = team_id then home_team_goals else away_team_goals end) as goal_for,
sum(case when home_team_id = team_id then away_team_goals else home_team_goals end) as goal_against,
sum(case when home_team_id = team_id then home_team_goals-away_team_goals else away_team_goals-home_team_goals end) as goal_diff
from matches m 
join teams t on m.home_team_id = t.team_id or m.away_team_id = t.team_id
group by team_name
order by points desc, goal_diff desc, team_name

------------------------------------------------------------

WITH CTE AS (
SELECT B.TEAM_NAME, A.GOAL_FOR, A.GOAL_AGAINST, A.POINTS FROM (
    SELECT
        home_team_id AS TEAM_ID,
        home_team_goals AS GOAL_FOR,
        away_team_goals AS GOAL_AGAINST,
        CASE WHEN home_team_goals > away_team_goals THEN 3
             WHEN home_team_goals < away_team_goals THEN 0
        ELSE 1 END AS POINTS 
    FROM Matches 
    UNION ALL
    SELECT
        away_team_id AS TEAM_ID,
        away_team_goals AS GOAL_FOR,
        home_team_goals AS GOAL_AGAINST,
        CASE WHEN home_team_goals < away_team_goals THEN 3
             WHEN home_team_goals > away_team_goals THEN 0
        ELSE 1 END AS POINTS 
    FROM Matches) A
LEFT JOIN Teams B
ON A.TEAM_ID=B.TEAM_ID )

SELECT TEAM_NAME, 
    COUNT(*) AS matches_played, 
    SUM(POINTS) AS POINTS,
    SUM(GOAL_FOR) AS GOAL_FOR,
    SUM(GOAL_AGAINST) AS GOAL_AGAINST,
    (SUM(GOAL_FOR)-SUM(GOAL_AGAINST)) AS GOAL_DIFF
FROM CTE 
GROUP BY TEAM_NAME
ORDER BY POINTS DESC, GOAL_DIFF DESC, TEAM_NAME ASC;
