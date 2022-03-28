'''
Write an SQL query that reports the product_name, year, and price for each sale_id in the Sales table.

Return the resulting table in any order.

The query result format is in the following example.
'''

select product.product_name,

year, price from sales inner join product using(product_id)
