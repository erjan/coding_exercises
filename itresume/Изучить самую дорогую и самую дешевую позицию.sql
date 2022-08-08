'''
Для каждого дня найти самую дорогую и самую дешевую позицию в нем и посчитать среднюю стоимость самых дорогих и среднюю стоимость самых дешевых позиций.
'''

with help as(
select 
ord_datetime,
an_price,
row_number()over(partition by ord_datetime order by an_price desc) exp_rank,
row_number()over(partition by ord_datetime order by an_price asc) cheap_rank
from
analysis a join orders o on o.ord_an = a.an_id)


select

avg(case when cheap_rank = 1 then an_price end) as avg_cheap,
avg(case when exp_rank = 1 then an_price end) as avg_exp

from help





