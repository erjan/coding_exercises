'''
Необходимо рассчитать медианное значение суммы заказов в разрезе года и месяца. Медиана должна быть рассчитана в 2 вариантах:

интерполированная медиана: в качестве медианы берется сумма, которая делит все заказы ровно в 50% пропорции, даже если фактически такого заказа на было.

действительная медиана: в качестве медианы берется реальная сумма заказа. Если заказов четное число, то берется ближайшая сумма заказа, меньшая интерполированной медианы.
'''


with help as(
select 

  to_char(ord_datetime, 'YYYY-MM') as dt,
  ord_datetime as id,
  sum(an_price) as revenue

from analysis a join orders o on a.an_id = o.ord_an
group by dt,id)

select 
dt, 
percentile_cont(0.5) within group(order by revenue)::numeric as interpolated_median,
percentile_disc(0.5) within group(order by revenue)::numeric as real_median

from help 
group by dt
order by dt
