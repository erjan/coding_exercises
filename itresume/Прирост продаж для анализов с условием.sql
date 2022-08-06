

'''
Помесячно вывести прирост количества 
продаж в процентах относительно предыдущего месяца для всех анализов в
2020 году, где в названии в любом 
месте располагается слово "кров" или "тестостерон" в любом регистре.
'''

with help as(
  
select 
to_char(ord_datetime, 'MM') as month,
an_name,
  lower(an_name) as lname,
ord_id, 
an_price, an_cost,
an_id

from analysis a inner join orders o on a.an_id = o.ord_an
where extract(year from ord_datetime) = 2020),

help2 as(
select 
month,
an_name as name,
ord_id, 
an_price, 
an_cost,
an_id

from help where lname like '%кров%' or lname like '%тестостерон%'),

help3 as(
select 
name, month, count(ord_id) as current_cnt
from help2
group by name, month
order by name, month),

help4 as(
select 

name, month, current_cnt, 
lag(current_cnt,1)over(partition by name order by name,month) as prev_cnt

from help3)

select name, month, current_cnt, prev_cnt,

coalesce( round( 100.0 * (current_cnt - prev_cnt) / prev_cnt,3), 0) as change


from help4


