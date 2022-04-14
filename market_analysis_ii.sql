'''
Write an SQL query to find for each user whether the brand of the second item (by date) they sold is their favorite brand. If a user sold less than two items, report the answer for that user as no. It is guaranteed that no seller sold more than one item on a day.

Return the result table in any order.

The query result format is in the following example.
'''


select user_id as seller_id, 
        (case 
            when favorite_brand = (
                            select i.item_brand
                            from Orders o left join Items i
                            on o.item_id = i.item_id
                            where o.seller_id = u.user_id 
                            order by o.order_date
                            limit 1 offset 1
                                  ) then "yes" else "no" end
         ) as "2nd_item_fav_brand"   
from Users u 


-------------------------------------
With tmp AS (
SELECT seller_id,
RANK() OVER (PARTITION BY seller_id ORDER BY order_date) AS ranks,
b.item_brand
FROM Orders a
INNER JOIN Items b
ON a.item_id = b.item_id
),
tmp2 AS (
SELECT * FROM tmp
WHERE ranks = 2
)
SELECT user_id AS seller_id,
CASE WHEN a.favorite_brand = b.item_brand THEN 'yes' ELSE 'no'
END AS 2nd_item_fav_brand
FROM Users a
LEFT JOIN tmp2 b
ON a.user_id = b.seller_id


-------------------------------Explanation:

With CTE - Use rank to find the 2nd item - partition by seller_id, order by date

With CTE - Then filter by ranking = 2

Use left join - want to make sure every user_id appears, then simple case then else statement.

  WITH cte AS 
  (
  	SELECT seller_id, item_brand FROM
  	(
  		SELECT o.seller_id, i.item_brand, o.order_date,
  		RANK() OVER(PARTITION BY o.seller_id ORDER BY o.order_date) AS "ranking"
  		FROM Orders o LEFT JOIN Items i ON i.item_id = o.item_id
  		ORDER BY 1, 3
  	) t WHERE ranking = 2 
  )

  SELECT u.user_id AS "seller_id", 
  CASE WHEN u.favorite_brand = c.item_brand THEN "yes" ELSE "no" END AS "2nd_item_fav_brand"
  FROM Users u LEFT JOIN cte c ON u.user_id = c.seller_id ORDER BY 1
  
