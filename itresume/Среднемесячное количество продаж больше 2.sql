'''
Вывести ID анализов, у которых среднемесячное количество заказов больше 2 в 2020 году.
'''

SELECT a.an_id,  ROUND(COUNT(*)::NUMERIC / 12, 3) AS cnt
FROM Orders o
JOIN Analysis a
ON o.ord_an = a.an_id
WHERE EXTRACT(YEAR FROM o.ord_datetime) = 2020
GROUP BY a.an_id
HAVING COUNT(*)::NUMERIC / 12 > 2
ORDER BY cnt DESC, an_id
