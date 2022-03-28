'''
Write an SQL query to report the shortest distance between any two points from the Point table.

The query result format is in the following example.
'''

#my own solution

with helper as (

SELECT x, 
  LAG(x) OVER(ORDER BY x) as prev FROM point) 
  
  
  select min(x - prev) as shortest from helper
  
  
  
  #another
 SELECT MIN(a.x - b.x) AS shortest
FROM point a, point b
WHERE a.x > b.x;
