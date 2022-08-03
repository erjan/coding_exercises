'''
Вывести все заказы, которые содержат анализы, предполагающие режим хранения 22. Ответ должен содержать ID заказа, ID анализа, название анализа и режим хранения.
'''

select 
ord_id, ord_an, an_name, gr_temp

from groups g inner join analysis a on a.an_group = g.gr_id
inner join orders o on o.ord_an = a.an_id
where gr_temp = 22
