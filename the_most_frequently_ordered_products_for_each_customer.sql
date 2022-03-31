'''

Write an SQL query to find the most frequently ordered product(s) for each customer.

The result table should have the product_id and product_name for each customer_id who ordered at least one order.

Return the result table in any order.

The query result format is in the following example.

'''


# Write your MySQL query statement below



select t.customer_id, t.product_id,p.product_name
from(
select customer_id, product_id, rank() over(partition by customer_id order by count(product_id) desc) as rank_p
from orders
group by customer_id,product_id
order by customer_id) as t left join products p on t.product_id = p.product_id
where rank_p = 1
