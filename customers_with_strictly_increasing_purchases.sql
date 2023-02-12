'''
Write an SQL query to report the IDs of the customers with the total purchases strictly increasing yearly.

The total purchases of a customer in one year is the sum of the prices of their orders in that year. If for some year the customer did not make any order, we consider the total purchases 0.
The first year to consider for each customer is the year of their first order.
The last year to consider for each customer is the year of their last order.
Return the result table in any order.

The query result format is in the following example.
'''


# Write your MySQL query statement below
with t as (
select customer_id, yr, total,yr-lag(yr,1) over(partition by customer_id order by yr asc) as yr_lag, total-lag(total,1) over(partition by customer_id order by yr asc) as total_lag
 from
 (
select customer_id, yr, sum(price) total from
(select order_id, customer_id, order_date, year(order_date) as yr, price from Orders
order by customer_id, yr asc) as temp
group by customer_id, yr) as t1
)
#select * from t
select distinct customer_id from t where
customer_id not in (
select customer_id from t where
yr_lag>1 or total_lag<=0) 

--------------------------------------------------------------------------------
with h as(
select customer_id, year(order_date) as yr, sum(price) total from orders

group by customer_id, yr),


h2 as(
select customer_id, total, yr-lag(yr,1)over(partition by customer_id order by yr asc) as yr_lag,
total - lag(total,1)over(partition by customer_id order by yr asc) as price_lag
from h)

select distinct customer_id from h2 where customer_id not in (select customer_id from h2 where
 yr_lag>1 or price_lag<=0)


