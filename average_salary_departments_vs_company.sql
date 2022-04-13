'''
Write an SQL query to report the comparison result (higher/lower/same) of the average salary of employees in a department to the company's average salary.

Return the result table in any order.

The query result format is in the following example.
'''


SELECT DISTINCT pay_month, department_id, 
(CASE WHEN department_avg_salary > company_avg_salary THEN 'higher'
     WHEN department_avg_salary < company_avg_salary THEN 'lower'
     WHEN department_avg_salary = company_avg_salary THEN 'same' END) AS comparison
FROM (
SELECT A.employee_id, amount, pay_date,department_id, LEFT(pay_date,7) as pay_month, AVG(amount) OVER(PARTITION BY A.pay_date) AS company_avg_salary,
AVG(amount) OVER(PARTITION BY A.pay_date, B.department_id) AS department_avg_salary
FROM salary AS A
JOIN employee AS B
ON A.employee_id = B.employee_id) AS temp;

--------------------------------------------------

SELECT d1.pay_month, d1.department_id, 
CASE WHEN d1.department_avg > c1.company_avg THEN 'higher'
     WHEN d1.department_avg < c1.company_avg THEN 'lower'
     ELSE 'same'
END AS 'comparison'
FROM ((SELECT LEFT(s1.pay_date, 7) pay_month, e1.department_id, AVG(s1.amount) department_avg
FROM salary s1
JOIN employee e1 ON s1.employee_id = e1.employee_id
GROUP BY pay_month, e1.department_id) d1
LEFT JOIN (SELECT LEFT(pay_date, 7) pay_month, AVG(amount) company_avg
FROM salary
GROUP BY pay_month) c1 ON d1.pay_month = c1.pay_month)
ORDER BY pay_month DESC, department_id;

---------------------------------------------
select distinct date_format(pay_date, '%Y-%m') as pay_month, department_id,
       case when avg(amount) over(partition by department_id, pay_date) > avg(amount) over(partition by pay_date) then 'higher'
            when avg(amount) over(partition by department_id, pay_date) < avg(amount) over(partition by pay_date) then 'lower'
            else 'same' end as comparison
from salary as s left join employee as e 
on s.employee_id = e.employee_id
order by 1 desc, 2 asc
