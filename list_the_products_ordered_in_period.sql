'''
Write an SQL query to get the names of products that have at least 100 units ordered in February 2020 and their amount.

Return result table in any order.

The query result format is in the following example.
'''

#my own
with helper as(
    
select 
product_id, unit, order_date

from orders 
where month(order_date) = 2 and year(order_date) = 2020)


select product_name, sum(unit) as unit from helper join products using(product_id)
group by product_name
having unit >=100
