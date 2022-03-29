'''
Since table Sales was filled manually in the year 2000, product_name may contain leading and/or trailing white spaces, also they are case-insensitive.

Write an SQL query to report

product_name in lowercase without leading or trailing white spaces.
sale_date in the format ('YYYY-MM').
total the number of times the product was sold in this month.
Return the result table ordered by product_name in ascending order. In case of a tie, order it by sale_date in ascending order.

The query result format is in the following example.
'''


with h as(

select lower(trim(product_name)) as product_name, 

date_format(sale_date, "%Y-%m") as sale_date,
sale_id

from sales)


select product_name, sale_date, count(sale_id) as total


from h

group by product_name, sale_date
order by product_name, sale_date 


#another

SELECT LOWER(TRIM(product_name)) product_name, DATE_FORMAT(sale_date, "%Y-%m") sale_date, count(sale_id) total
FROM sales
GROUP BY 1, 2
ORDER BY 1, 2
