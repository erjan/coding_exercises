'''
Write an SQL query to report the difference between the number of apples and oranges sold each day.

Return the result table ordered by sale_date.

The query result format is in the following example.
'''


select 
s1.sale_date,
( s1.sold_num - s2.sold_num)  as diff

from sales s1 join sales s2

on s1.sale_date = s2.sale_date and s1.fruit = 'apples'
and s2.fruit = 'oranges'



#another

select sale_date, sum(case when fruit='apples' then sold_num else -sold_num end) as diff
from sales
group by sale_date


#ANOTher

SELECT
    sale_date,
    SUM(IF(fruit = 'apples', sold_num, -sold_num)) AS diff
FROM Sales
GROUP BY sale_date
