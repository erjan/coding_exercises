'''
Write an SQL query that reports the products that were only sold in the spring of 2019. That is, between 2019-01-01 and 2019-03-31 inclusive.

Return the result table in any order.

The query result format is in the following example.
'''

SELECT DISTINCT product_id, product_name
FROM sales

JOIN product USING (product_id)

WHERE product_id NOT IN 
(SELECT product_id FROM sales WHERE sale_date NOT BETWEEN'2019-01-01' AND '2019-03-31') 

AND 

product_id IN 

(SELECT product_id FROM sales WHERE sale_date BETWEEN'2019-01-01' AND '2019-03-31')
