'''

Write an SQL query to report the names of all sellers who did not make any sales in 2020.

Return the result table ordered by seller_name in ascending order.

The query result format is in the following example.

 
 '''

with the2020 as (
select 

seller_id,seller_name

from seller left join orders using(seller_id)

where year(sale_date) = 2020)


select  seller.seller_name as SELLER_NAME 
from seller left join orders using(seller_id)

where seller.seller_id not in (select seller_id from the2020)
order by SELLER_NAME asc


#another

SELECT seller_name
FROM Seller 
WHERE  seller_id NOT IN (
    SELECT DISTINCT seller_id 
    FROM Orders
    WHERE LEFT(sale_date, 4) = '2020'
)
ORDER BY 1
