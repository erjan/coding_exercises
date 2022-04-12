'''
Write an SQL query to report the customer ids from the Customer table that bought all the products in the Product table.

Return the result table in any order.

The query result format is in the following example.
'''


WITH c as (SELECT customer_id, 
GROUP_CONCAT(DISTINCT product_key 
                     order by product_key
                     separator ',') as products
FROM Customer
GROUP BY customer_id),
p as (
SELECT 
GROUP_CONCAT(DISTINCT product_key 
				order by product_key
                 separator ',') as uni_product
FROM Product)

SELECT customer_id 
FROM c, p
WHERE c.products = p.uni_product


--------------------
Select customer_id from (select distinct
customer_id,product_key from customer) g group by customer_id
having count(*) = (select count( product_key) from product)

1- Use the inner query to get rid of dups ( one customer purchasing same product more than once)
2- Then get the number of times each customerid appears in the customer table.
3- The records with the count equal to number of products should be in our answer.



----------------

select 
customer_id
from customer 
group by customer_id
having count(distinct product_key) = (select count(*) from product)
;
