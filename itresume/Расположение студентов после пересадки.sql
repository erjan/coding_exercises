'''
Было принято решение поменять студентов, которые сидят рядом, местами. Напишите SELECT-запрос, который из исходной таблицы сформирует расположение студентов после пересадки.

Примечание: 1 меняется местом со 2, 3 с 4 и так далее. Если студентов нечетное количество, то последний студент не пересаживается, а остается на своем месте.
'''

select

(case when mod(seat,2)=1 and seat!= (select count(*) from students) then seat+1
when mod(seat,2)=0 then seat-1
else seat end),name

from students
order by 1
