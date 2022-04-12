'''
The global ranking of a national team is its rank after sorting all the teams by their points in descending order. If two teams have the same points, we break the tie by sorting them by their name in lexicographical order.

The points of each national team should be updated based on its corresponding points_change value.

Write an SQL query to calculate the change in the global rankings after updating each team's points.

Return the result table in any order.

The query result format is in the following example.
'''


SELECT a.team_id,a.name,
CAST(ROW_NUMBER() OVER(ORDER BY points DESC,name ASC) AS SIGNED)-
CAST(ROW_NUMBER() OVER(ORDER BY points+points_change DESC,name ASC) as SIGNED) as rank_diff
FROM TeamPoints as a
JOIN PointsChange as b
ON a.team_id=b.team_id



SELECT
    ini.team_id,
    ini.name,            
    CAST(RANK() OVER (ORDER BY ini.points DESC, ini.name) AS SIGNED) -
    CAST(RANK() OVER (ORDER BY ini.points + chg.points_change DESC, ini.name) AS SIGNED) AS rank_diff
FROM
    TeamPoints ini
    INNER JOIN PointsChange chg
    ON chg.team_id = ini.team_id
ORDER BY 3
