
'''
Для каждого года в отдельности
проранжировать продажи по группам анализов. Если для каких-то групп 
в рамках одного года продажи сопадают, то им присваивать одинаковое место. Ранги 
должны идти без разрывов.
'''


with h as(
select 

an_group as id, ord_id,
to_char(ord_datetime, 'YYYY') as year

from analysis a inner join orders o on o.ord_an = a.an_id),

h2 as(
select 
id, year, count(distinct ord_id) as cnt
from h
group by year, id)

select id,  year, cnt , dense_rank()over(partition by year order by  cnt desc) as rnk from h2



