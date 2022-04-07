
'''

Write an SQL query to find the start and end number of continuous ranges in the table Logs.

Return the result table ordered by start_id.

The query result format is in the following example.

'''

WITH temp1 AS(
    
    SELECT log_id
,log_id-ROW_NUMBER() OVER(ORDER BY log_id) AS difference
FROM Logs)




SELECT 
MIN(log_id) AS start_id ,MAX(log_id) AS end_id
FROM temp1
GROUP BY difference
ORDER BY start_id


----------------------
SELECT min(log_id) as start_id, max(log_id) as end_id
FROM
(SELECT log_id, ROW_NUMBER() OVER(ORDER BY log_id) as num
FROM Logs) a
GROUP BY log_id - num
