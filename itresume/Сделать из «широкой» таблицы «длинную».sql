'''
Как из таблицы WideTable получить LongTable?


'''


select
name, 'FIO' as key, FIO as value from widetable
union 
select name, 'Phone' as key, Phone as value
from widetable
union 
select name, 'Email' as key, Email as value
from widetable
order by name,key,value
