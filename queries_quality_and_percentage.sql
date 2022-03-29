
'''
Write an SQL query to find each query_name, the quality and poor_query_percentage.

Both quality and poor_query_percentage should be rounded to 2 decimal places.

Return the result table in any order.

The query result format is in the following example.
'''

select 
query_name,
round(avg(rating/position),2) as quality,

ROUND(AVG(rating < 3) * 100, 2) AS poor_query_percentage 

from queries
group by query_name


