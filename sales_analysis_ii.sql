'''
Write an SQL query that reports the buyers who have bought S8 but not iPhone. Note that S8 and iPhone are products present in the Product table.

Return the result table in any order.

The query result format is in the following example.

'''

select distinct buyer_id
from sales join product using(product_id)
where product_name = 'S8' 
and buyer_id not in (select distinct buyer_id
                    from sales join product using(product_id)
                    where product_name = 'iPhone' )
