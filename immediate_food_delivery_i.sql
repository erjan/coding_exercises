'''
If the customer's preferred delivery date is the same as the order date, then the order is called immediate; otherwise, it is called scheduled.

Write an SQL query to find the percentage of immediate orders in the table, rounded to 2 decimal places.

The query result format is in the following example.'''


with h as (
select delivery_id ,
(if( customer_pref_delivery_date  = order_date, 1,0)) as just
from delivery)

select round(100* sum(just)/ (select count(delivery_id)  from delivery) ,2)
as immediate_percentage from h



#another
select round(100 * sum(order_date = customer_pref_delivery_date) / count(*), 2) as immediate_percentage 
from Delivery;

#another
SELECT ROUND(100*AVG(order_date = customer_pref_delivery_date), 2) AS immediate_percentage 
FROM Delivery;
