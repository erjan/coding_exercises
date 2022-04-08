'''

You are running an e-commerce site that is looking for imbalanced orders. An imbalanced order is one whose maximum quantity is strictly greater than the average quantity of every order (including itself).

The average quantity of an order is calculated as (total quantity of all products in the order) / (number of different products in the order). The maximum quantity of an order is the highest quantity of any single product in the order.

Write an SQL query to find the order_id of all imbalanced orders.

Return the result table in any order.

The query result format is in the following example.

'''






with cte as (
    select order_id,
    max(avg(quantity)) over() as max_avg_qty,
    max(quantity) as max_qty
    from ordersdetails
    group by order_id
)


select order_id from cte where max_qty>max_avg_qty

------------------------

with cte as (
    select order_id,
    avg(quantity) as avg_qty,
    max(quantity) as max_qty
    from ordersdetails
    group by order_id
)
select order_id from cte where max_qty>(select max(avg_qty) from cte);
