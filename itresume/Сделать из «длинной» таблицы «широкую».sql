
'''
Как из таблицы LongTable получить WideTable? Предполагается чтение таблицы один раз и отсутствие соединений.
'''


select 

name, 
max(case when key = 'FIO' then value end) as fio,
max(case when key = 'Phone' then value end) as Phone,
max(case when key = 'Email' then value end) as Email

from longtable
group by name
order by name
