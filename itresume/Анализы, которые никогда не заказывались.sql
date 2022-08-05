'''
Выведите ID и названия всех анализов, которые никогда не заказывались.
'''


SELECT  an_id, an_name
FROM    analysis a
WHERE   a.an_id NOT IN (SELECT  ord_an FROM    orders o)
