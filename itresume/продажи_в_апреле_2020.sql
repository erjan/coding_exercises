'''
Вывести все номера заказов, которые были совершены в апреле 2020 года. Ответ должен содержать:

ID заказа
дату-время заказа
Результат отсортируйте по возрастанию даты и времени.
'''


select ord_id,ord_datetime

from Orders where extract(month from ord_datetime) = 4 and extract( year from ord_datetime) = 2020

order by ord_datetime asc
