'''
Write an SQL query to report the customer_id and customer_name of customers who have spent at least $100 in each month of June and July 2020.

Return the result table in any order.

The query result format is in the following example.
'''



with june as (

select 

customers.customer_id,
customers.name

from customers join orders on orders.customer_id = customers.customer_id
join product on product.product_id = orders.product_id
where month(order_date) = 6 and year(order_date) = 2020

group by customers.customer_id
having sum(orders.quantity* price) >=100),

july as(

select 

customers.customer_id,
customers.name

from customers join orders on orders.customer_id = customers.customer_id
join product on product.product_id = orders.product_id
where month(order_date) = 7 and year(order_date) = 2020

group by customers.customer_id
having sum(orders.quantity* price) >=100)



select j.customer_id, name

from july  j
where j.customer_id in (select customer_id from june)



#another
SELECT customer_id, name
FROM Customers JOIN Orders USING(customer_id) 
    JOIN Product USING(product_id)
GROUP BY customer_id
HAVING SUM(IF(LEFT(order_date, 7) = '2020-06', quantity, 0) * price) >= 100
    AND SUM(IF(LEFT(order_date, 7) = '2020-07', quantity, 0) * price) >= 100



