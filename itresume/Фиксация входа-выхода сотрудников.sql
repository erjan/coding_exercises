'''
Необходимо вывести сотрудников и дни, когда они находились на рабочем месте менее 8 часов.
'''


WITH a AS 
(
SELECT employee,
       check_time::DATE AS check_date,
       COALESCE(
           CASE 
                WHEN is_entered = False 
                THEN check_time - LAG(check_time) OVER (
                    PARTITION BY employee, check_time::DATE
                    ORDER BY check_time) 
                END, 
           INTERVAL '0'
        ) AS diff
FROM gate
)
SELECT employee, check_date, SUM(diff)
FROM a
GROUP BY employee, check_date
HAVING SUM(diff) < INTERVAL '8 hours'
