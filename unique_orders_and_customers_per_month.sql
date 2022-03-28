'''
Write an SQL query to find the number of unique orders and the number of unique customers with invoices > $20 for each different month.

Return the result table sorted in any order.

The query result format is in the following example.
'''


select 

DATE_FORMAT(order_date,'%Y-%m') as month,

count(distinct order_id) as order_count,
count(distinct customer_id) as customer_count

from orders
where invoice > 20

group by DATE_FORMAT(order_date,'%Y-%m')
