'''
Задача состоит в том, чтобы вернуть интервалы подряд идущих чисел.Результатом будет таблица из 2 столбцов start и end:
'''

-- Введите свое решение ниже. 
-- Вы работаете с PostgreSQL.

with help as (
select 
a, row_number()over() as r

from numbers),

help2 as(
select a,r, (a-r) as diff
from help
group by a,r
order by r)

select 
min(a) as start, max(a) as end
from help2
group by diff
order by min(a)

