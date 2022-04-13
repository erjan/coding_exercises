'''
Write an SQL query to report the percentage of working drivers (working_percentage) for each month of 2020 where:


Note that if the number of available drivers during a month is zero, we consider the working_percentage to be 0.

Return the result table ordered by month in ascending order, where month is the month's number (January is 1, February is 2, etc.). Round working_percentage to the nearest 2 decimal places.

The query result format is in the following example.
'''

with recursive months as (
select      1 as month
union all
select      month+1
from        months
where       month <12),

available_drivers as (
select      months.month, ifnull(max(t1.active_driver) over (order by month),0) as active_driver
from        months
left join   
(select     month(join_date) as month, count(driver_id) over (order by join_date rows unbounded preceding) as active_driver
from        drivers
where       year(join_date) <= 2020) t1
on          t1.month = months.month
),

working_drivers as (
select      month(requested_at) as month, count(distinct driver_id) as working_driver
from        Rides R
join        AcceptedRides A on R.ride_id = A.ride_id
where       year(requested_at) = 2020
group by    1)

select      months.month, ifnull(round(working_driver/active_driver*100,2),0) as working_percentage
from        months
left join   available_drivers on available_drivers.month = months.month
left join   working_drivers on working_drivers.month = months.month
group by    1

--------------------------------------

# Write your MySQL query statement below
# select number from 1 to 12
with recursive months as (select 1 as month union all select month+1 from months where month<12),

# select cumulative drivers at the end of each month in 2020
t1 as (select m.month,sum(t.cnt) over(order by m.month) as active_drivers
from 
months m
left join
(select case when year(join_date)=2019 then 1 else month(join_date) end as month,
    count(distinct(driver_id)) cnt from Drivers
where year(join_date)<=2020
group by 1)t
on m.month=t.month),

# select drivers accepting orders each month 
t2 as (select month(r.requested_at) month,ifnull(count(distinct(a.driver_id)),0) as accept_drivers 
from Rides r 
join AcceptedRides a 
on r.ride_id=a.ride_id
where year(r.requested_at) =2020
group by 1 )

# calculate the percentage
select t1.month,ifnull(round(t2.accept_drivers/t1.active_drivers*100,2),0.00) working_percentage
from t1
left join t2
on t1.month=t2.month
