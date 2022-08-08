'''
Нарастающим итогом рассчитать, как увеличивалось количество проданных тестов каждый месяц каждого года с разбивкой по группе.
'''


WITH sales as
(
  SELECT TO_CHAR(o.ord_datetime, 'YYYY') AS year,
         TO_CHAR(o.ord_datetime, 'MM') AS month,
         a.an_group AS group,
         COUNT(o.ord_an)::SMALLINT AS cnt
  FROM Orders o
  JOIN Analysis a
  ON o.ord_an = a.an_id
  GROUP BY year, month, a.an_group
)
  SELECT s.year, s.month, s.group,
         SUM(s.cnt) OVER(PARTITION BY s.group, s.year ORDER BY s.year, s.month) AS sum
  FROM sales AS s
  ORDER BY s.group, s.year, s.month
