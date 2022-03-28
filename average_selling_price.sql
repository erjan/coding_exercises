
'''
Write an SQL query to find the average selling price for each product. average_price should be rounded to 2 decimal places.

Return the result table in any order.

The query result format is in the following example.
'''

select

prices.product_id,

round(sum(price*units)/ sum(units),2) as average_price

from prices inner join unitssold using(product_id)
where purchase_date between start_date and end_date
group by prices.product_id
