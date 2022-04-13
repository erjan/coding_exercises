'''
Write an SQL query to compute the average_ride_distance and average_ride_duration of every 3-month window starting from January - March 2020 to October - December 2020. Round average_ride_distance and average_ride_duration to the nearest two decimal places.

The average_ride_distance is calculated by summing up the total ride_distance values from the three months and dividing it by 3. The average_ride_duration is calculated in a similar way.

Return the result table ordered by month in ascending order, where month is the starting month's number (January is 1, February is 2, etc.).

The query result format is in the following example.
'''


option 1: easy to understand
Related Questions:

Find the Missing IDs ------ step1
general inner join question + GROUP BY, SUM + date MONTH, YEAR ------ step2
general left join question + IFNULL ------ step3
(you can combine step 2 and step 3 into one query if you are comfortable with them)
Consecutive Numbers + ROUND ------ step4
with recursive month as (
    select 1 as month
    union
    select month + 1 as month from month where month < 12
)

, month_rides as(
    select   
        MONTH(r.requested_at) as month,
        sum(a.ride_distance) as ride_distance,
        sum(a.ride_duration) as ride_duration
    from Rides r join AcceptedRides a on a.ride_id = r.ride_id
    where YEAR(r.requested_at) = '2020'
    group by month
    # order by month asc
)
, every_month_rides as(
    select 
        m.month, 
        ifnull(mr.ride_distance,0) as ride_distance, 
        ifnull(mr.ride_duration,0) as ride_duration
    from month m left join month_rides mr on mr.month = m.month
    # order by 1
)


# select * from month
# select * from month_rides
# select * from every_month_rides

select 
    t1.month as month,
    round((t1.ride_distance + t2.ride_distance + t3.ride_distance)/3,2) as average_ride_distance,
    round((t1.ride_duration + t2.ride_duration + t3.ride_duration)/3,2) as average_ride_duration
from every_month_rides t1
join every_month_rides t2
join every_month_rides t3 
on t1.month = t2.month -1 and t2.month = t3.month -1

Step by Setp solution:

First, use recursive funtion to generate a Numeric Sequences in Mysql

    select 1 as month
    union
    select month + 1 as month from month where month < 12
You will the following result:
{"headers": ["month"], "values": [[1], [2], [3], [4], [5], [6], [7], [8], [9], [10], [11], [12]]}

Second, get the total ride_distance and total ride_duration of every month from table Rides and table AcceptedRides.

select   
        MONTH(r.requested_at) as month,
        sum(a.ride_distance) as ride_distance,
        sum(a.ride_duration) as ride_duration
    from Rides r join AcceptedRides a on a.ride_id = r.ride_id
    where YEAR(r.requested_at) = '2020'
    group by month
    # order by month asc
after running this, you will get the following result:
{"headers":
["month", "ride_id", "ride_distance", "ride_duration"], "values": [

[3, 10, 63, 38],
[6, 13, 73, 96],
[7, 7, 100, 28],
[8, 17, 119, 68],
[11, 163, 193],
[12, 2, 6, 38]]}

Third, left join month table to get 12 month's result.

 select 
        m.month, 
        ifnull(mr.ride_distance,0) as ride_distance, 
        ifnull(mr.ride_duration,0) as ride_duration
    from month m left join month_rides mr on mr.month = m.month
    # order by 1
after runing this query, you will see the following result:
{"headers":
["month", "ride_distance", "ride_duration"], "values": [

[1, 0, 0],
[2, 0, 0],
[3, 63, 38],
[4, 0, 0],
[5, 0, 0],
[6, 73, 96],
[7, 100, 28],
[8, 119, 68],
[9, 0, 0],
[10, 0, 0],
[11, 163, 193],
[12, 6, 38]]}

Finally, self join 3 times of the above table and get the final result.

select 
    t1.month as month,
    round((t1.ride_distance + t2.ride_distance + t3.ride_distance)/3,2) as average_ride_distance,
    round((t1.ride_duration + t2.ride_duration + t3.ride_duration)/3,2) as average_ride_duration
from every_month_rides t1
join every_month_rides t2
join every_month_rides t3 
on t1.month = t2.month -1 and t2.month = t3.month -1
P.s. Before doing the average_ride_distance and average_ride_duration in your final query, it's better to see this helpful result:

select 
   *
from every_month_rides t1
join every_month_rides t2
join every_month_rides t3 
on t1.month = t2.month -1 and t2.month = t3.month -1
{"headers":

["month", "ride_distanc", "ride_duration", "month", "ride_distanc", "ride_duration", "month", "ride_distanc", "ride_duration"], "values": [

[1, 0, 0, 2, 0, 0, 3, 63, 38],
[2, 0, 0, 3, 63, 38, 4, 0, 0],
[3, 63, 38, 4, 0, 0, 5, 0, 0],
[4, 0, 0, 5, 0, 0, 6, 73, 96],
[5, 0, 0, 6, 73, 96, 7, 100, 28],
[6, 73, 96, 7, 100, 28, 8, 119, 68],
[7, 100, 28, 8, 119, 68, 9, 0, 0],
[8, 119, 68, 9, 0, 0, 10, 0, 0],
[9, 0, 0, 10, 0, 0, 11, 163, 193],
[10, 0, 0, 11, 163, 193, 12, 6, 38]]}

option 2: fast and concise
After you understand the above instruction, you may easily find an easier way to solve this question like this:

with recursive month as (
    select 1 as month
    union
    select month + 1 as month from month where month < 10
)

, month_rides as(
    select   
        MONTH(r.requested_at) as month,
        sum(a.ride_distance) as ride_distance,
        sum(a.ride_duration) as ride_duration
    from Rides r 
    join AcceptedRides a on a.ride_id = r.ride_id
    where YEAR(r.requested_at) = '2020'
    group by month
)

select 
    m.month,
    ifnull(round(sum(mr.ride_distance)/3,2),0) as average_ride_distance,
    ifnull(round(sum(mr.ride_duration)/3,2),0) as average_ride_duration
from month m
left join month_rides mr
on ((mr.month - m.month = 0) 
    or (mr.month - m.month = 1)
    or (mr.month - m.month = 2))
group by 1
order by 1

-----------------------------------------
WITH RECURSIVE Tab AS
(SELECT 1 as month UNION ALL SELECT month+1 FROM Tab WHERE month<=11),

TOT AS (
SELECT
        t.month, IFNULL(SUM(ride_distance),0) as dist, IFNULL(SUM(ride_duration),0) as dur
FROM
        Rides r
JOIN    AcceptedRides a
        ON a.ride_id = r.ride_id AND YEAR(requested_at)=2020
RIGHT JOIN Tab t
        ON MONTH(r.requested_at) = t.month
GROUP BY 1 ORDER BY 1)

SELECT a.month, ROUND((a.dist+b.dist+c.dist)/3,2) as average_ride_distance, ROUND((a.dur+b.dur+c.dur)/3,2) as average_ride_duration
FROM TOT a
JOIN TOT b ON a.month=b.month-1
JOIN TOT c ON a.month=c.month-2
GROUP BY 1 ORDER BY 1
