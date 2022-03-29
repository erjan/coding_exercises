'''
Write an SQL query to find the percentage of the users registered in each contest rounded to two decimals.

Return the result table ordered by percentage in descending order. In case of a tie, order it by contest_id in ascending order.

The query result format is in the following example.
'''

select 
contest_id,
round( COUNT(DISTINCT user_id) * 100 / (SELECT COUNT(*) FROM Users),2) as percentage
from  register
group by contest_id
order by percentage desc, contest_id asc
