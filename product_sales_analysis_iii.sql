
'''

Write an SQL query that selects the product id, year, quantity, and price for the first year of every product sold.

Return the resulting table in any order.

The query result format is in the following example.

'''


SELECT product_id, year AS first_year, quantity, price
FROM Sales
WHERE (product_id, year) IN (
SELECT product_id, MIN(year) as year
FROM Sales
GROUP BY product_id) ;


select product_id, year as first_year, quantity, price
from(
select *,
rank() over(partition by product_id order by year) as year_rnk
from sales) as tbl
where year_rnk = 1
