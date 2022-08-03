

'''
Напишите запрос, в котором для каждого анализа будет выведены название группы и нужный температурный режим.

Результат должен содержать столбцы:

ID анализа
Название анализа
Название группы
Температурный режим
'''


select 

distinct an_id, an_name,gr_name,
gr_temp 

from analysis a left join orders o on a.an_id = o.ord_an inner join groups g on g.gr_id = a.an_group

order by an_id
