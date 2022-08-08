'''
Необходимо вывести количество людей из Тулы, которые покупали телефоны с разбивкой по месяцам.
'''

with help as (
select
*,
rtrim(to_char(created_at, 'month')) AS "month"

from customer c  
join purchases p on p.user_id = c.id_customer

join skus s on s.id = p.sku_id
where town = 'Tula' and s.category = 2)

select month, count(distinct user_id) as people
from help 
group by month 
order by people desc
