'''

Округлите наценку на каждую позицию из таблицы Заказов до ближайшего десятка. Выберите только те строки, где наценка больше 50%.
'''


with help as(
select 
o.*, 
round( 100.0*(an_price -an_cost)/an_cost, -1)  as markup
from orders o left join analysis a on o.ord_an = a.an_id
order by markup asc)


select * from help
where markup > 50
order by ord_id
