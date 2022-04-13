'''
Write an SQL query to report the following statistics for each month of 2020:

The number of drivers currently with the Hopper company by the end of the month (active_drivers).
The number of accepted rides in that month (accepted_rides).
Return the result table ordered by month in ascending order, where month is the month's number (January is 1, February is 2, etc.).

The query result format is in the following example.
'''

generate month table
(select 1 as month)
union (select 2 as month)
union (select 3 as month)
union (select 4 as month)
union (select 5 as month)
union (select 6 as month)
union (select 7 as month)
union (select 8 as month)
union (select 9 as month)
union (select 10 as month)
union (select 11 as month)
union (select 12 as month)
generate driver table (columns: driver_id and month (2020))
select driver_id, 
(case when year(join_date)=2019 then '1' else month(join_date) end) `month`
from Drivers 
where year(join_date)<=2020
generate accepted ride table (columns: ride_id and month (2020))
select month(requested_at) as `month`, a.ride_id
from AcceptedRides a 
join Rides r
on r.ride_id = a.ride_id
where year(requested_at)=2020
combine them
select t.month, 
count(distinct driver_id) active_drivers,
count(distinct rides.ride_id) accepted_rides 
from
(
    (select 1 as month)
    union (select 2 as month)
    union (select 3 as month)
    union (select 4 as month)
    union (select 5 as month)
    union (select 6 as month)
    union (select 7 as month)
    union (select 8 as month)
    union (select 9 as month)
    union (select 10 as month)
    union (select 11 as month)
    union (select 12 as month)
) t
# join driver table
left join
(
	select driver_id, 
	(case when year(join_date)=2019 then '1' else month(join_date) end) `month`
	from Drivers 
	where year(join_date)<=2020
) d
on d.month <= t.month
# join accepted ride table
left join
(
    select month(requested_at) as `month`, a.ride_id
    from AcceptedRides a 
    join Rides r
    on r.ride_id = a.ride_id
    where year(requested_at)=2020
) rides
on t.month = rides.month
group by t.month 
order by t.month 


-----------------------------------------------------------

with recursive months(month) as
(
  select 1
  union all
  select month + 1
  from months
  where month < 12
),

t1 as
(
select month(join_date) as month, count(driver_id) over (order by join_date) as active_drivers
from drivers
where year(join_date) <= 2020
),

t2 as
(
select month(requested_at) as month, count(ride_id) as accepted_rides
from rides r
where ride_id in (select ride_id from AcceptedRides) and year(requested_at) = 2020
group by month
)

select distinct m.month, 
ifnull(max(t1.active_drivers) over (order by m.month),0) as active_drivers,
ifnull(t2.accepted_rides, 0) as accepted_rides
from months m left join t1 on m.month = t1.month
left join t2 on m.month = t2.month
-------------------------------------------

SELECT column_0 as month, ( 
	SELECT COUNT(*) FROM Drivers 
	WHERE join_date < '2021-01-01' AND (join_date < '2020-01-01' OR Month(join_date) <= column_0)
) as active_drivers, ( 
	SELECT COUNT(*) FROM AcceptedRides, Rides
	WHERE AcceptedRides.ride_id = Rides.ride_id
	AND requested_at < '2021-01-01' AND requested_at >= '2020-01-01' AND Month(requested_at) = column_0
) as accepted_rides
FROM (
    VALUES ROW(1), ROW(2), ROW(3), ROW(4), ROW(5), ROW(6), ROW(7), ROW(8), ROW(9), ROW(10), ROW(11), ROW(12)
) AS months
