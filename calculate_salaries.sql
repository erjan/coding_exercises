'''

Write an SQL query to find the salaries of the employees after applying taxes. Round the salary to the nearest integer.

The tax rate is calculated for each company based on the following criteria:

0% If the max salary of any employee in the company is less than $1000.
24% If the max salary of any employee in the company is in the range [1000, 10000] inclusive.
49% If the max salary of any employee in the company is greater than $10000.
Return the result table in any order.

The query result format is in the following example.
'''

with h as(

select 

company_id, employee_id,employee_name, salary,

max(salary) over(partition by company_id) as part

from salaries)


select 


company_id,
employee_id, employee_name,

case 
when part < 1000 then salary
when part >=1000 and part <=10000 then round(salary - 0.24*salary)
when part > 10000 then round(salary - 0.49*salary) end as salary

from h


#another----------------------

SELECT company_id, employee_id, employee_name
,ROUND(CASE
    WHEN MAX(salary) over(PARTITION BY company_id) < 1000 THEN salary
    WHEN MAX(salary) over(PARTITION BY company_id) BETWEEN 1000 AND 10000 THEN salary-(salary*.24) 
    ELSE salary-(salary*.49)
END,0) salary
FROM salaries
