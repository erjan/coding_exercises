'''
Write an SQL query to find the most recent order(s) of each product.

Return the result table ordered by product_name in ascending order and in case of a tie by the product_id in ascending order. If there still a tie, order them by order_id in ascending order.

The query result format is in the following example.
'''

WITH rank AS(
    SELECT order_id, product_id, order_date, 
    RANK() OVER (PARTITION BY product_id ORDER BY order_date desc) as rank
FROM Orders as o)

SELECT p.product_name, r.product_id,  r.order_id, r.order_date
FROM rank as r
JOIN products as p
    ON p.product_id = r.product_id AND r.rank = 1
ORDER BY product_name, r.product_id, r.order_id

------------------

SELECT p.product_name,p.product_id,o.order_id,o.order_date FROM Products p
JOIN Orders o ON p.product_id = o.product_id
JOIN (
      SELECT product_id, MAX(order_date) AS first_order_date FROM Orders
      GROUP BY product_id
     ) t
ON t.product_id = p.product_id AND t.first_order_date = o.order_date
ORDER BY p.product_name,p.product_id,o.order_id;

----------------------------

select po.product_name, po.product_id, po.order_id, po.order_date
from (
select p.product_name, o.product_id, o.order_id, o.order_date,
RANK() over (partition by o.product_id order by
o.order_date desc) AS rank
from orders o inner join products p on p.product_id = o.product_id
) AS po
where po.rank = 1
order by po.product_name, po.product_id, po.order_id
