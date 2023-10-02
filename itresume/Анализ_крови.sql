'''
Найти все уникальные названия анализов, которые фигурировали в заказах и имеют в названии любую форму слова кровь.
'''


select distinct an_name from analysis a inner join orders o on o.ord_an = a.an_id

where  lower(an_name) like '%кровь%';

