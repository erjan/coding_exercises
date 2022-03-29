'''
Write an SQL query that reports the best seller by total sales price, If there is a tie, report them all.

Return the result table in any order.

The query result format is in the following example.
'''





select seller_id

from sales 
group by seller_id

having sum(price) = (select sum(price) 
from sales group by seller_id order by 1 desc limit 1)

