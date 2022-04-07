'''

Write an SQL query to report the customer_id and customer_name of 
customers who bought products "A", "B" but did not buy the product "C" since we want to recommend them to purchase this product.

Return the result table ordered by customer_id.

The query result format is in the following example.

'''


SELECT DISTINCT b.customer_id, b.customer_name
  FROM Orders a
  JOIN Customers b
    ON a.customer_id = b.customer_id 
 WHERE a.customer_id NOT IN (select customer_id FROM Orders WHERE product_name = 'C')
   AND a.customer_id IN (SELECT customer_id FROM Orders WHERE product_name = 'A')
   AND a.customer_id IN (SELECT customer_id FROM Orders WHERE product_name = 'B')
ORDER BY 1


----------------
SELECT DISTINCT customer_id, customer_name
  FROM Customers
 WHERE customer_id in (
    SELECT customer_id
      FROM Orders
     GROUP BY customer_id
    HAVING SUM(product_name = 'A') > 0
       AND SUM(product_name = 'B') > 0 
       AND SUM(product_name = 'C') = 0
)

-------------------------------

WITH CTE AS (
	 SELECT customer_id, 
	                SUM(Product_name = 'A') OVER (partition by customer_id) AS 'Purchase_A',
                    SUM(Product_name = 'B') OVER (partition by customer_id) AS 'Purchase_B',
                    SUM(Product_name = 'C') OVER (partition by customer_id) AS 'Purchase_C')
SELECT DISTINCT  c.customer_id, Customers.customer_name
  FROM CTE
  JOIN  Customers ON Customers.customer_id = c.customer_id
 WHERE c.Purchase_A > 0
   AND c.Purchase_B > 0
   AND c.Purchase_C = 0
