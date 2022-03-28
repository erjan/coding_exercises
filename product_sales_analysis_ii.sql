'''
Write an SQL query that reports the total quantity sold for every product id.

Return the resulting table in any order.

The query result format is in the following example.

'''




select product.product_id,

sum(quantity) as total_quantity

from product inner join sales on product.product_id = sales.product_id

group by product.product_id
