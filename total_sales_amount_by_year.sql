'''
Write an SQL query to report the total sales amount of each item for each year, with corresponding product_name, product_id, product_name, and report_year.

Return the result table ordered by product_id and report_year.

The query result format is in the following example.
'''


SELECT a.product_id, b.product_name, a.report_year, a.total_amount
FROM (
    SELECT product_id, '2018' AS report_year,
        average_daily_sales * (DATEDIFF(LEAST(period_end, '2018-12-31'), GREATEST(period_start, '2018-01-01'))+1) AS total_amount
    FROM Sales
    WHERE YEAR(period_start)=2018 OR YEAR(period_end)=2018

    UNION ALL

    SELECT product_id, '2019' AS report_year,
        average_daily_sales * (DATEDIFF(LEAST(period_end, '2019-12-31'), GREATEST(period_start, '2019-01-01'))+1) AS total_amount
    FROM Sales
    WHERE YEAR(period_start)<=2019 AND YEAR(period_end)>=2019

    UNION ALL

    SELECT product_id, '2020' AS report_year,
        average_daily_sales * (DATEDIFF(LEAST(period_end, '2020-12-31'), GREATEST(period_start, '2020-01-01'))+1) AS total_amount
    FROM Sales
    WHERE YEAR(period_start)=2020 OR YEAR(period_end)=2020
) a
LEFT JOIN Product b
ON a.product_id = b.product_id
ORDER BY a.product_id, a.report_year

-----------------
WITH RECURSIVE CTE AS
    (SELECT MIN(period_start) as date
     FROM Sales 
     UNION ALL
     SELECT DATE_ADD(date, INTERVAL 1 day)
     FROM CTE
     WHERE date <= ALL (SELECT MAX(period_end) FROM Sales))

 
SELECT 
        s.product_id, p.product_name, LEFT(e.date,4) as report_year, SUM(s.average_daily_sales) as total_amount
FROM Sales s
JOIN Product p ON p.product_id = s.product_id
JOIN CTE e ON s.period_start<=e.date AND s.period_end>=e.date
GROUP BY 1,2,3 
ORDER BY 1,3

-------------------------
ith recursive cte as(
    select product_id, average_daily_sales, period_start, period_end from Sales
	
    UNION ALL
    
	select 
		product_id, 
		average_daily_sales, 
		date_add(period_start, interval 1 day) period_start, 
		period_end
    from cte
    where period_start < period_end
)

select 
    c.product_id,
    p.product_name,
    date_format(c.period_start, "%Y") report_year,
    count(c.period_start)*c.average_daily_sales total_amount
from cte c 
join Product p on p.product_id = c.product_id
group by 1,2,3
order by 1,3
