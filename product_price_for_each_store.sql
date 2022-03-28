'''
Write an SQL query to find the price of each product in each store.

Return the result table in any order.

The query result format is in the following example.
'''

SELECT *
FROM (
       SELECT product_id,store,price FROM Products
     )T1
PIVOT
(MAX(price) FOR store IN (
                           [store1],
                           [store2],
                           [store3]
                         ) 
)T2
Naive CASE WHEN

SELECT
  product_id,
  MAX(CASE WHEN store = 'store1' THEN price END) AS store1,
  MAX(CASE WHEN store = 'store2' THEN price END) AS store2,
  MAX(CASE WHEN store = 'store3' THEN price END) AS store3
FROM Products GROUP BY product_id
