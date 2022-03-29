'''
Write an SQL query that reports the best seller by total sales price, If there is a tie, report them all.

Return the result table in any order.

The query result format is in the following example.
'''

SELECT seller_id 
FROM Sales
GROUP BY seller_id
HAVING SUM(price) = (
    SELECT sum(price)
    FROM Sales
    GROUP BY seller_id
    ORDER BY 1 DESC 
    LIMIT 1)
    
