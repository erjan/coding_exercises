'''
Вывести третий анализ по количеству продаж за весь период.

Результат должен содержать столбцы:

ID анализа
Название анализа
Количество продаж cnt
Ранг анализа в зависимости от продаж rn
'''

with helper as(

select 

analysis.an_id, count(ord_id) as cnt

from analysis inner join orders on analysis.an_id = orders.ord_an

group by analysis.an_id
order by cnt desc),

helper2 as(
select an_id, cnt, rank()over(order by cnt desc) as rn from helper)

select analysis.an_id, analysis.an_name, cnt, rn

from helper2 inner join analysis on analysis.an_id = helper2.an_id
where rn = 3
