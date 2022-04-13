'''
Write an SQL query to calculate the cumulative salary summary for every employee in a single unified table.

The cumulative salary summary for an employee can be calculated as follows:

For each month that the employee worked, sum up the salaries in that month and the previous two months. This is their 3-month sum for that month. If an employee did not work for the company in previous months, their effective salary for those months is 0.
Do not include the 3-month sum for the most recent month that the employee worked for in the summary.
Do not include the 3-month sum for any month the employee did not work.
Return the result table ordered by id in ascending order. In case of a tie, order it by month in descending order.

The query result format is in the following example.

'''


SELECT   A.Id, MAX(B.Month) as Month, SUM(B.Salary) as Salary
FROM     Employee A INNER JOIN Employee B
ON    A.Id = B.Id AND B.Month BETWEEN   (A.Month-2) AND (A.Month)
WHERE A.month != (select max(month) from employee where id = a.id)
GROUP BY A.Id, A.Month
ORDER BY Id, Month DESC

#best solution
------
SELECT id, month, salary+prev_month_salary+prev_2month_salary AS Salary
FROM
(
    SELECT id, month, salary,
    ROW_NUMBER() OVER(PARTITION BY id ORDER BY month DESC) AS month_rank,
    CASE WHEN LAG(month,1,0) OVER(PARTITION BY id ORDER BY month) = month - 1 THEN LAG(salary,1,0) OVER(PARTITION BY id ORDER BY month) ELSE 0 END AS prev_month_salary,
    CASE WHEN LAG(month,2,0) OVER(PARTITION BY id ORDER BY month) = month - 2 THEN LAG(salary,2,0) OVER(PARTITION BY id ORDER BY month) ELSE 0 END AS prev_2month_salary
    FROM Employee
) AS SUB_T
WHERE month_rank <> 1 AND salary <> 0
GROUP BY id, month
ORDER BY id, month DESC
