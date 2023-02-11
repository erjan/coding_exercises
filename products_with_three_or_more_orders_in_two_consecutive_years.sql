'''
Write an SQL query to report the IDs of all the products that were ordered three or more times in two consecutive years.

Return the result table in any order.

The query result format is shown in the following example.
'''


WITH VOL AS (
                SELECT      product_id,
                            YEAR(purchase_date) AS PURCHASE_YEAR                            
                FROM        Orders
                GROUP BY    product_id,PURCHASE_YEAR
                HAVING      COUNT(order_id) >= 3
            )

SELECT      DISTINCT V1.product_id 
FROM        VOL V1, VOL V2
WHERE       V1.product_id = V2.product_id AND V2.PURCHASE_YEAR = V1.PURCHASE_YEAR + 1 

--------------------------------------------------------------------------------------------
-- cte stores the data for count of purchase of a product_id for that year
with cte as 
(
 select product_id, YEAR(purchase_date) as year_of_purchase
 from orders
 group by product_id, year_of_purchase
 having count(*) >= 3
)

-- We are getting the data for 2 consecutive year having count greater than or equal to 3 in each year
select distinct c1.product_id
from cte c1
join cte c2
on c1.product_id = c2.product_id
and c1.year_of_purchase - c2.year_of_purchase = 1

# Do upvote if you like the solution
