'''

You are the restaurant owner and you want to analyze a possible expansion (there will be at least one customer every day).

Write an SQL query to compute the moving average of how much the customer paid 
in a seven days window (i.e., current day + 6 days before). average_amount should be rounded to two decimal places.

Return result table ordered by visited_on in ascending order.

The query result format is in the following example.
'''



select distinct visited_on, amount, round(amount/7, 2) as average_amount
from (select visited_on, 
      sum(amount) over (order by visited_on range between interval 6 day preceding and current row) as amount,
      dense_rank() over (order by visited_on) as rk
      from Customer) as t
where rk >= 7



----------------------------

with sum_table as (
select distinct visited_on,
sum(amount) over (order by visited_on range between interval 6 day preceding and current row) as amount,
-- note that we use range to get the preceding 6 days
dense_rank() over (order by visited_on) as days
-- we need to remove the first 6 days from the output, note that dense_rank() is used to avoid gap in rank
from Customer
)

select visited_on, amount, round(amount/7,2) as average_amount
from sum_table
where days >= 7;
