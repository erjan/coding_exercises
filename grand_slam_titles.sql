
'''

Write an SQL query to report the number of grand slam tournaments won by each player. Do not include the players who did not win any tournament.

Return the result table in any order.

The query result format is in the following example.

 
 
 '''


SELECT player_id,player_name,
SUM(player_id=Wimbledon)+SUM(player_id=Fr_open)+SUM(player_id=US_open)+SUM(player_id=Au_open)
as grand_slams_count
FROM Players
JOIN Championships
ON player_id=Wimbledon or player_id=Fr_open or player_id=US_open or player_id=Au_open
GROUP BY player_id;


---------------

SELECT * 
FROM (
  SELECT 
   player_id,
   player_name,
   SUM( CASE WHEN player_id = Wimbledon THEN 1 ELSE 0 END +
        CASE WHEN player_id = Fr_open THEN 1 ELSE 0 END +
        CASE WHEN player_id = US_open THEN 1 ELSE 0 END +
        CASE WHEN player_id = Au_open THEN 1 ELSE 0 END ) AS grand_slams_count
  FROM Players CROSS JOIN Championships GROUP BY player_id, player_name ) T
WHERE grand_slams_count > 0

------------------------------

WITH CTE AS 
   (
    SELECT Wimbledon AS id FROM Championships
    UNION ALL 
    SELECT Fr_open AS id FROM Championships
    UNION ALL 
    SELECT US_open AS id FROM Championships
    UNION ALL 
    SELECT Au_open AS id FROM Championships 
   )
   
SELECT player_id,player_name,COUNT(*) AS grand_slams_count
FROM Players INNER JOIN CTE ON Players.player_id = CTE.id
GROUP BY player_id,player_name
