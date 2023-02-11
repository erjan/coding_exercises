'''
Write an SQL query that reports for each user the product id on which the user spent the most money. In case the same user spent the most money on two or more products, report all of them.

Return the resulting table in any order.

The query result format is in the following example.
'''


with h as(

select user_id,s.product_id, sum(price*quantity) as spending

 from sales s join product p on p.product_id = s.product_id

group by user_id, s.product_id),

h2 as(
select user_id, product_id, rank()over(partition by user_id order by spending desc) as rnk from h )

select user_id, product_id from h2 where rnk=1


------------------------------------------------------------------------------------------------------
SELECT
    user_id
    , product_id
FROM (
    SELECT
        user_id
        , product_id
        , RANK() OVER(PARTITION BY user_id ORDER BY SUM(quantity)*price DESC) AS rnk
    FROM Sales
    JOIN Product USING(product_id)
    GROUP BY user_id, product_id
) a
WHERE rnk = 1
