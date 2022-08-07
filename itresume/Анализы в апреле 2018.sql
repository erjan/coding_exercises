'''
Отобрать все анализы, которые были заказаны в апреле 2018 года. Необходимо вывести 
только один столбец - название анализа.
'''

select distinct an_name from analysis a inner join orders o on o.ord_an = a.an_id
where extract(year from ord_datetime) = 2018 and extract(month from ord_datetime) = 4
