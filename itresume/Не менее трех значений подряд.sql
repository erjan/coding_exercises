'''
Найти все Num, которые встречаются не менее
трех раз подряд. Результат выведите в столбце ConsecutiveNums.

Числа выведите без повторов - чтобы одно число 
в столбце ConsecutiveNums встречалось только 1 раз.
'''



select distinct l1.num as ConsecutiveNums from logs l1, logs l2 , logs l3

where l1.id = l2.id-1 and l2.id = l3.id-1
and l1.num = l2.num and l1.num = l3.num
order by l1.num desc

