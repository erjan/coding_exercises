'''
Write an SQL query to find all dates' Id with higher temperatures compared to its previous dates (yesterday).

Return the result table in any order.

The query result format is in the following example.
'''


SELECT distinct a.Id from weather a, weather b where a.temperature > b.temperature
and datediff(a.recordDate, b.recordDate) = 1
