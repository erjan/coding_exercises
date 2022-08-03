'''
Вывести:

ID анализа
его количество продаж в штуках в течение предыдущего года от 01.03.2019 до 01.03.2020 (включительно)
поле Группа (gr)
Правило формирования групп:

если количество чеков от 10 (не включительно) до 20 (включительно), то Группа = 1
если больше 20, то Группа = 2
если меньше 10 (включительно), то Группа = 0
'''


with help as(
select 

an_id,

count(ord_id) as c

from analysis a inner join orders o on a.an_id = o.ord_an 
where ord_datetime between '2019-03-01' and '2020-03-01'

group by  an_id
order by an_id asc)

select an_id,
c as amount,
case when c > 10 and c <=20 then 1
 when c > 20 then 2
 else 0 end as gr


from help


