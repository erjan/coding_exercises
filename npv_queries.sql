'''
Write an SQL query to find the npv of each query of the Queries table.

Return the result table in any order.

The query result format is in the following example.
'''


select q.id, q.year, coalesce(n.npv, 0) as npv
from 
npv n 
right join 
queries q
on n.id = q.id and n.year = q.year
