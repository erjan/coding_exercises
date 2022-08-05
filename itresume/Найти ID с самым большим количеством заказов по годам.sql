
'''
Выберите ID товара с самым большим количеством заказов с разбивкой по годам.
'''

with help as(
select 

an_id,count( ord_id) as cnt, to_char(ord_datetime, 'YYYY') as year
from analysis a inner join orders o on o.ord_an = a.an_id
group by year,an_id),

help2 as(
select 
  year,
an_id,cnt,
rank()over(partition by year order by cnt desc) as rnk
from help)


select year,an_id, cnt from help2 where rnk=1
order by  year,an_id
