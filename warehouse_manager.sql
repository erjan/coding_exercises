'''
Write an SQL query to report the number of cubic feet of volume the inventory occupies in each warehouse.

Return the result table in any order.

The query result format is in the following example.
'''

SELECT name warehouse_name,
       SUM(units * Width * Length * Height) volume
FROM Warehouse W
LEFT JOIN Products P 
ON W.product_id = P.product_id
GROUP BY name
