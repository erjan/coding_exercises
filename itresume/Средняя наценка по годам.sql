'''
Вывести из таблицы Заказов информацию по средней наценке с разбивкой по годам.

Примечание: Наценка рассчитывается по формуле Наценка = (Розница - Себестоимость)/Себестоимость
'''

select

extract(year from ord_datetime) as year,

 avg(100.0*(an_price - an_cost)/an_cost)/100.0 as mean_markup

from analysis a inner join orders o on a.an_id = o.ord_an
group by year
order by year asc
