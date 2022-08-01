'''
Найти количество продаж с разбивкой по датам в период дат с '2019-10-25' до '2019-11-02'. Оставить только те строки, где количество заказов больше 5.

Результат должен содержать столбец с датой и количеством cnt.
'''


with help as (

select orders.ord_datetime, count(orders.ord_id) as cnt from analysis inner join orders on analysis.an_id = orders.ord_an
group by orders.ord_datetime
having count(orders.ord_id) > 5)


select ord_datetime, cnt from help where ord_datetime between '2019-10-25'  and '2019-11-02' order by cnt asc
