'''

Write an SQL query to find the total score for each gender on each day.

Return the result table ordered by gender and day in ascending order.

The query result format is in the following example.

'''


SELECT  

gender,
day, 

SUM(score_points) over (PARTITION by gender ORDER by day) as total
FROM scores
order by gender, day



---------------------------
SELECT s1.gender, s1.day, SUM(s2.score_points) AS total
FROM Scores AS s1,
     Scores AS s2
WHERE s1.gender = s2.gender AND s2.day <= s1.day
GROUP BY s1.gender, s1.day
ORDER BY s1.gender, s1.day
