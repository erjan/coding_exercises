'''
Найти все пары различных
клиентов (поле FIRST_NAME) из города Moscow. Результатом запроса должны 
быть 2 столбца: customer1 и customer2.
'''

select


c1.first_name as customer1,

c2.first_name as customer2

from customer c1 cross join customer c2 

where c1.town = 'Moscow' and c2.town = 'Moscow' and c1.first_name != c2.first_name
