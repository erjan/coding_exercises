'''
The median is the value separating the higher half from the lower half of a data sample.

Write an SQL query to report the median of all the numbers in the database after decompressing the Numbers table. Round the median to one decimal point.

The query result format is in the following example.
'''


Get the middle two numbers' indexes by floor((sum(frequency) + 1) / 2), floor((sum(frequency) + 2) / 2). E.g.,

if sum(frequency) == 12, then the middle indexes are 6, 7, and if
sum(frequency) == 13, then the middle indexes are 7, 7, i.e., the same number.
Then get average of numbers from these two indexes.

WITH cte AS (SELECT floor((sum(frequency) + 1) / 2) AS m1
    , FLOOR((SUM(frequency) + 2) / 2) AS m2
FROM numbers )
    , cte2 AS (select number
    , SUM(frequency) OVER (ORDER BY number ROWS UNBOUNDED PRECEDING) AS presum
FROM numbers )
    , n1 AS ( SELECT number 
FROM cte2 WHERE presum >= (SELECT m1 FROM cte) LIMIT 1)
    , n2 AS ( SELECT number 
FROM cte2 WHERE presum >= (SELECT m2 FROM cte) LIMIT 1)

SELECT AVG(number) AS median 
FROM (select * FROM n1 UNION SELECT * FROM n2) t

----------------------

WITH tmp AS (SELECT Number, Frequency,
             SUM(Frequency) OVER (ORDER BY Number ASC) rk1,
             SUM(Frequency) OVER (ORDER BY Number DESC) rk2
             FROM Numbers)
  
SELECT AVG(Number*1.0) AS median
FROM tmp
WHERE ABS(rk1-rk2)<=Frequency
---------------------------------

With cte_1 as
(Select  
    *,
    sum(Frequency) over() as total_freq,
    sum(Frequency) over(order by Number) as end_freq
    from Numbers
),
cte2 as(
Select  
    *,
    case when total_freq%2=0 then total_freq/2 end as mid_1,
    case when total_freq%2=0 then (total_freq/2)+1 end as mid_2,
    case when total_freq%2=1 then round((total_freq/2)+0.5) end as mid_3,
    lag(end_freq,1,0) over (order by Number) as start_freq
    from cte_1
)
Select avg(number) as median from cte2
where (mid_1 > start_freq and mid_1<=end_freq)
or  (mid_2 > start_freq and mid_2<=end_freq)
or (mid_3 > start_freq and mid_3<=end_freq)
