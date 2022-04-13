'''
Buses and passengers arrive at the LeetCode station. If a bus arrives at the station at 
a time tbus and a passenger arrived at a time tpassenger where tpassenger <= tbus and the 
passenger did not catch any bus, the passenger will use that bus. In addition, each bus has a capacity. If at the moment 
the bus arrives at the station there are more passengers waiting than its capacity capacity, only capacity passengers will use the bus.

Write an SQL query to report the number of users that used each bus.

Return the result table ordered by bus_id in ascending order.

The query result format is in the following example.
'''



WITH RECURSIVE A AS(
    SELECT bus_id,
    LAG(arrival_time, 1, -1) OVER( ORDER BY arrival_time) AS last_arrival_time,
    arrival_time,  capacity FROM Buses 
),
B AS(
    SELECT A.bus_id, A.arrival_time,  A.capacity, COUNT(P.passenger_id) AS passager_count FROM A LEFT JOIN Passengers P 
    ON A.last_arrival_time < P.arrival_time AND P.arrival_time<= A.arrival_time GROUP BY 1
),
C AS(
    SELECT bus_id, 
    capacity,
    passager_count AS total_passenger,
    ROW_NUMBER() OVER(ORDER BY arrival_time) AS id
    FROM B
),
D AS(
    SELECT bus_id,capacity , total_passenger,id,
    IF(capacity>total_passenger, total_passenger, capacity) AS passager_taken,
    IF(capacity<total_passenger, total_passenger - capacity, 0) AS passager_overleft
    FROM C WHERE id = 1
    UNION
    SELECT C.bus_id,C.capacity , C.total_passenger, C.id,
    IF(C.capacity>C.total_passenger+D.passager_overleft, C.total_passenger+D.passager_overleft, C.capacity) AS passager_taken,
    IF(C.capacity<C.total_passenger+D.passager_overleft, C.total_passenger+D.passager_overleft - C.capacity, 0) AS passager_overleft
    FROM C 
    INNER JOIN D ON D.id+1 = C.id
)
SELECT bus_id, passager_taken AS passengers_cnt FROM D ORDER BY 1

---------------------------------------------
WITH TEMP AS (
SELECT bus_id, b.arrival_time, capacity, count(passenger_id) AS num
FROM Buses b  LEFT JOIN Passengers p  ON p.arrival_time <= b.arrival_time
WHERE bus_id is not NULL
GROUP BY bus_id
ORDER BY arrival_time
)

SELECT bus_id, passengers_cnt from (
SELECT bus_id, capacity, num,
      @passengers_cnt:=LEAST(capacity,num-@accum) as passengers_cnt, 
      @accum:=@accum+@passengers_cnt
FROM TEMP, (SELECT @accum:= 0, @passengers_cnt:=0) INIT) temp
ORDER BY bus_id

------------------------------------

I split the solution into 3 steps.

First 2 steps are same as Problem 2142. The Number of Passengers in Each Bus I, which is using LAG to get the previous bus arrival time, and find the number of passengers with arrival_time > previous bus arrival time and <= current bus arrival time.

Find previous bus arrival time
Find how many people current bus needs take, not considering the remaining passengers from the previous buses.
Using Recursive CTE to find accumative passenger left from the previous buses, and report how many people current bus can take.
/* Write your T-SQL query statement below */
with c1 as -- Find the previous bus arrival time 
(
    select
		rn = row_number() over (order by  arrival_time)  -- create a row number for the sequence of the bus.
		,bus_id
		,arrival_time
		,prev_time = lag(arrival_time, 1 , -999) over(order by arrival_time)  
		,capacity
    from Buses
)
, c2 as -- Find how many people current bus needs to take, without thinking of the remaining passengers from the previous buses
(
	select 
		c1.rn
		, c1.bus_id
		, c1.capacity
		, curr_passenger_cnt = count(p.passenger_id) 
	from c1 left outer join Passengers p on p.arrival_time <= c1.arrival_time and p.arrival_time > c1.prev_time
	group by c1.rn, c1.bus_id, c1.capacity
)
, r_cte as  
			-- find how many people previous bus left, and how many current bus can take.
			-- current bus pick = prev_remaining + current_Passenger
			-- current bus remaining = max(0, prev_remaining + current_Passenger - capacity)
(
	select 
		rn
		, bus_id
		, capacity
		, curr_passenger_cnt
		, accumulated_remaining = case when curr_passenger_cnt - capacity <= 0 then 0 else curr_passenger_cnt - capacity end  
	from c2 where rn = 1 --starting from the first arrival bus

	union all 
		
	select    
		 c2.rn 
		,c2.bus_id
		,c2.capacity
		,curr_passenger_cnt = c2.curr_passenger_cnt + c.accumulated_remaining
		,accumulated_remaining = case when c2.curr_passenger_cnt + c.accumulated_remaining - c2.capacity <= 0 then 0 else c2.curr_passenger_cnt + c.accumulated_remaining - c2.capacity end
	from r_cte c inner join c2 on c2.rn = c.rn + 1
)
select 
bus_id
, passengers_cnt = case when accumulated_remaining > 0 then capacity else curr_passenger_cnt end  
from r_cte
order by bus_id
