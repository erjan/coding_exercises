'''
В рамках каждого дня пронумеруйте строки, опираясь на дату 
и время заказа (по убыванию). Для каждого нового дня нумерация должна начинаться заново.
'''

select 

date(ord_datetime) as dt,
ord_datetime, ord_id, ord_an, 

row_number()over(partition by ord_datetime order by ord_datetime   ) as rn

from analysis a inner join orders o on o.ord_an = a.an_id

order by dt, ord_datetime
