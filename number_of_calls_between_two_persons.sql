'''

Write an SQL query to report the number of calls and the total call duration between each pair of distinct persons (person1, person2) where person1 < person2.

Return the result table in any order.

The query result format is in the following example.


'''



select IF(from_id < to_id, from_id,to_id) as person1,IF(from_id < to_id, to_id,from_id) as person2
, COUNT(*) as call_count,
 SUM(duration) as total_duration
FROM Calls
 GROUP BY person1,person2;
 
 -----------
 
 
 SELECT LEAST(from_id,to_id) as person1,
GREATEST(from_id,to_id) as person2,
COUNT(*) as call_count,
SUM(duration) as total_duration
FROM Calls
GROUP BY person1,person2;
