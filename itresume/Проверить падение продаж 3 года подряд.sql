'''
Помесячно проверить: если суммарное количество продаж в течение трех месяцев подряд падают, то вывести в столбец Result 1, иначе 0.
'''


WITH sales AS (
  SELECT
    TO_CHAR(ord_datetime, 'YYYY-MM') AS year_month,
    TO_CHAR(ord_datetime, 'YYYY') AS year,
    TO_CHAR(ord_datetime, 'MM') AS month,
    LAG(COUNT(*), 2) OVER (ORDER BY TO_CHAR(ord_datetime, 'YYYY-MM')) AS prev2_cnt,
    LAG(COUNT(*), 1) OVER (ORDER BY TO_CHAR(ord_datetime, 'YYYY-MM')) AS prev_cnt,
    COUNT(*) AS cur_cnt
  FROM Orders
  GROUP BY year_month, year, month
)
SELECT year, month, prev2_cnt, prev_cnt, cur_cnt,
  CASE
    WHEN (prev_cnt - cur_cnt) > 0 AND (prev2_cnt - prev_cnt) > 0 THEN 1
    ELSE 0
  END AS result
FROM sales
ORDER BY year, month
