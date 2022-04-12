'''
If the customer's preferred delivery date is the same as the order date, then the order is called immediate; otherwise, it is called scheduled.

The first order of a customer is the order with the earliest order date that the customer made. It is guaranteed that a customer has precisely one first order.

Write an SQL query to find the percentage of immediate orders in the first orders of all customers, rounded to 2 decimal places.

The query result format is in the following example.

'''

select 
	round(avg(case when order_date = customer_pref_delivery_date then 1 else 0 end)*100, 2) 'immediate_percentage'
from 
	Delivery
where 
	(customer_id, order_date) in (select customer_id, min(order_date) from Delivery group by customer_id);
  
  
  
  ---------------
  select
round(sum(if(order_date=customer_pref_delivery_date,1,0))/count(*)*100,2) as immediate_percentage
from Delivery 
where (customer_id, order_date) in 
(select customer_id, min(order_date) from Delivery group by 1)


---------
SELECT ROUND(100 *
SUM(CASE WHEN order_date = customer_pref_delivery_date THEN 1 ELSE 0 END) / COUNT(customer_id), 2) AS immediate_percentage
FROM Delivery
WHERE (customer_id, order_date) IN (
SELECT customer_id, MIN(order_date)
FROM Delivery
GROUP BY customer_id
) 
