'''
Write an SQL query to show the details of the invoice with the highest price. If two or more invoices have the same price, return the details of the one with the smallest invoice_id.

Return the result table in any order.

The query result format is shown in the following example.
'''

# Write your MySQL query statement below
with cte as (
    SELECT invoice_id, SUM(quantity*price) AS price2
    FROM Purchases a LEFT JOIN Products b ON a.product_id = b.product_id
    GROUP BY invoice_id
    ORDER BY price2 DESC, invoice_id ASC
    LIMIT 1 
)
SELECT a.product_id, quantity, quantity*b.price AS price
FROM Purchases a LEFT JOIN Products b ON a.product_id = b.product_id
WHERE invoice_id = (SELECT invoice_id FROM cte)
