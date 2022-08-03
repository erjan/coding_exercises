'''
Для каждого анализа вывести: ID анализа, кол-во продаж за 2019 год и кол-во продаж за 2020 год.
'''

select an_id as an, 

count( case when extract(year from ord_datetime) = 2019 then ord_id end) as year2019,      
count( case when extract(year from ord_datetime) = 2020 then ord_id end) as year2020   

from analysis a inner join orders o on o.ord_an = a.an_id

group by an_id
order by an_id
