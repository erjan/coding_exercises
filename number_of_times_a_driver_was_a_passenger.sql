'''
Write an SQL query to report the ID of each driver and the number of times they were a passenger.

Return the result table in any order.

The query result format is in the following example.
'''


-------------------------------
select a.driver_id, ifnull(count(distinct b.ride_id), 0) as cnt
from Rides a left join Rides b on a.driver_id = b.passenger_id
group by a.driver_id
----------------------
SELECT
  D.driver_id,
  COUNT(R2.passenger_id) AS cnt
FROM
  (SELECT DISTINCT R1.driver_id FROM Rides R1) D
  LEFT JOIN Rides R2 ON D.driver_id = R2.passenger_id
GROUP BY
  D.driver_id;
