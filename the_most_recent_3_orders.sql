'''

Write an SQL query to find the most recent three orders of each user. If a user ordered less than three orders, return all of their orders.

Return the result table ordered by customer_name in ascending order and in case of a tie by the customer_id in ascending order. If there is still a tie, order them by order_date in descending order.

The query result format is in the following example.

'''


with s as(
select 

name as customer_name, c.customer_id, order_id, order_date,

row_number() over(partition by orders.customer_id order by order_date desc) as x

    from customers c inner join orders using(customer_id))
    
select customer_name, customer_id, order_id, order_date

from s where s.x <=3
order by customer_name, customer_id, order_date desc

---------------------------------------------------------------

select customer_name, customer_id, order_id, order_date
from
(select  name customer_name, c.customer_id, order_id, order_date,
rank() over(partition by c.customer_id order by order_date desc) rank
from customers c
inner join
orders o
on c.customer_id = o.customer_id) temp
where rank <=3
order by customer_name, customer_id, order_date desc
