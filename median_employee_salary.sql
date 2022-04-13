'''
Write an SQL query to find the median salary of each company.

Return the result table in any order.

The query result format is in the following example.
'''




with t as(

select

*,
row_number()over(partition by company order by salary asc) as ranking,

count(id)over(partition by company)as cnt

from employee)

select id, company ,salary from t

where ranking between cnt/2.0 and cnt/2.0+1
