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



select e1.id,e1.month month,sum(e2.salary) salary
from
employee e1 inner join employee e2 on e1.id=e2.id and (e1.Month - e2.Month) between 0 and 2
where (e1.id,e1.month) not in (select id,max(month) from employee group by id)
group by e1.id,e1.month
order by e1.id,e1.month desc


#best solution

SELECT id, month, Salary
FROM
(
SELECT  id, 
        month, 
		-- Every 3 months. ROWS 2 PRECEDING indicates the number of rows or values to precede the current row (1 + 2)
        SUM(salary) OVER(PARTITION BY id  ORDER BY month ROWS 2 PRECEDING) as Salary, 
        DENSE_RANK() OVER(PARTITION BY id ORDER by month DESC) month_no
FROM Employee
)  src
--  exclude the most recent month
where month_no > 1
ORDER BY id , month desc
