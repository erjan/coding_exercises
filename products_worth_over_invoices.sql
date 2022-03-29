'''
Write an SQL query that will, for all products, return each product name with the total amount due, paid, canceled, and refunded across all invoices.

Return the result table ordered by product_name.

The query result format is in the following example.
'''

SELECT 

p.name, 

IFNULL(SUM(rest),0) rest, 
IFNULL(SUM(paid),0) paid, 
IFNULL(SUM(canceled),0) canceled, 
IFNULL(SUM(refunded),0) refunded 

FROM invoice i 
right  JOIN product p USING(product_id)
GROUP BY p.name
ORDER BY p.name
