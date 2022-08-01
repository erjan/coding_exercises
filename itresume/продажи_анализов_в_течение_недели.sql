'''
Для всех анализов, которые продавались 5 февраля 2020 и всю следующую неделю, вывести:

an_name
an_cost
ord_datetime
Результат отсортируйте по возрастанию столбцов:

ord_datetime
an_cost

'''



select analysis.an_name, an_cost, ord_datetime from analysis inner join orders on orders.ord_an = analysis.an_id

where ord_datetime between '2020-02-05' and '2020-02-12'
order by ord_datetime, an_cost
