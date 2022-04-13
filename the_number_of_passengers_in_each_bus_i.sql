'''
Buses and passengers arrive at the LeetCode station. If a bus arrives at 
the station at time tbus and a passenger arrived at time tpassenger where tpassenger <= tbus and the 
passenger did not catch any bus, the passenger will use that bus.

Write an SQL query to report the number of users that used each bus.

Return the result table ordered by bus_id in ascending order.

The query result format is in the following example.

 
 '''


WITH t AS
(
    SELECT passenger_id, MIN(b.arrival_time) AS arrival_time
    FROM Passengers p
    INNER JOIN Buses b
    ON p.arrival_time <= b.arrival_time
    GROUP BY passenger_id
)

# Boarding time and bus id have 1 to 1 correspondence
SELECT bus_id, COUNT(t.arrival_time) AS passengers_cnt
FROM Buses b
LEFT JOIN t
ON b.arrival_time = t.arrival_time
GROUP BY bus_id
ORDER BY bus_id

----------------------
WITH cte AS (
SELECT bus_id, arrival_time,
LAG(arrival_time,1,0) OVER (ORDER BY arrival_time) min_time
FROM buses
)

SELECT cte.bus_id, COUNT(passenger_id) AS passengers_cnt
FROM cte
LEFT JOIN passengers p
ON p.arrival_time > cte.min_time AND p.arrival_time <= cte.arrival_time
GROUP BY 1
ORDER BY 1;

-----------------------

select bus_id, count(used_bus.m) as passengers_cnt
from 
buses left join 
		(select passenger_id, min(b.arrival_time) as m
			from passengers p join buses b 
			on p.arrival_time <= b.arrival_time
			group by passenger_id) as used_bus 
on (used_bus.m = buses.arrival_time)
group by bus_id
order by bus_id

The inner select choose the bus's arrival time that has the 
smallest postive difference with the passenger's arrival time. The outer select match the minimal bus arrival time to the bus id since no 
two buses will arrive at the same time and for buses that nobody catches on, count(used_bus.m) will automatically return 0.
