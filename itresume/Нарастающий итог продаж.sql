'''
Нарастающим итогом вывести увеличение общей суммы продаж с каждым новым заказом в порядке увеличения ID.

Итоговая таблица должна содержать столбцы:

dt - дату заказа
ord_id - ID заказа
cumsum - накопительный итог
Результат отсортируйте по id заказа.
'''


select 

date(ord_datetime) as dt,
ord_id, 
sum(an_price) over(order by ord_id) as cumsum

from analysis a inner join orders o on o.ord_an = a.an_id

order by ord_id



----------------------------------------------------------------

SELECT DATE(o.ord_datetime) AS dt,
       o.ord_id,
       SUM(a.an_price) OVER(ORDER BY o.ord_id) AS cumsum
FROM Orders o
JOIN Analysis a
ON o.ord_an = a.an_id
ORDER BY o.ord_id
