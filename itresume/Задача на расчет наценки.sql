'''
Рассчитать и вывести наценку для каждой
строки таблицы Заказов. Рассчитанную наценку округлите до 3 знака после 
запятой и выразите в % (то есть не 0.01, а 1).
'''

with help as(
select 

o.*,

round( 100.0* (an_price -an_cost)/an_cost,3)   as markup

from analysis a right join orders o on a.an_id = o.ord_an)

select ord_id, ord_datetime, ord_an, cast (markup as numeric) as markup from help
