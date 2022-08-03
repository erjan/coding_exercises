

'''
Необходимо вывести информацию о продажах за те даты, когда продажи были больше, чем за предыдущий день из таблицы sales
'''


with help as(
select 
date,
sum(value) as value
from sales
group by date
order by date),

help2 as(
select 

date, value, lag(value,1)over(order by date) as lg

from help
order by date),

help3 as(
select date, value, case when lg is null then 0 else lg end as lg
  from help2
)

select date, value,lg from help3
where value > lg
order by date
