'''

Write an SQL query to report the number of bank accounts of each salary category. The salary categories are:

"Low Salary": All the salaries strictly less than $20000.
"Average Salary": All the salaries in the inclusive range [$20000, $50000].
"High Salary": All the salaries strictly greater than $50000.
The result table must contain all three categories. If there are no accounts in a category, then report 0.

Return the result table in any order.

The query result format is in the following example.

'''

with low  as(

select
account_id,
income

from accounts

where income < 20000),
aver as(


select
account_id,
income

from accounts

where income between 20000 and 50000 ),

high as(

select
account_id,
income

from accounts

where income > 50000
)


select 

'Low Salary' as category ,
count(account_id) as accounts_count

from low

union

select 

'Average Salary' as category ,
count(account_id) as accounts_count

from aver

union

select 

'High Salary' as category ,
count(account_id) as accounts_count

from high

----------------------------

SELECT "Low Salary" AS Category,
SUM(income<20000) AS accounts_count
FROM Accounts
UNION
SELECT  "Average Salary" Category,
SUM(income BETWEEN 20000 AND 50000) AS accounts_count
FROM Accounts
UNION
SELECT "High Salary" category,
SUM(income>50000) AS accounts_count
FROM Accounts

------------------------------
select 'Low Salary' as category, count(case when income<20000 then 1 end) as accounts_count from Accounts
union
select 'Average Salary' as category, count(case when income>=20000 and income<= 50000 then 1 end) as accounts_count from Accounts
union
select 'High Salary' as category, count(case when income>50000 then 1 end) as accounts_count from Accounts

----------------------

select 'Low Salary' as category,
(select ifnull(count(account_id),0) from accounts where income < 20000) as accounts_count
union
select 'Average Salary' as category,
(select ifnull(count(account_id),0) from accounts where income >= 20000 and income <= 50000) as accounts_count
union
select 'High Salary' as category,
(select ifnull(count(account_id), 0) from accounts where income > 50000) as accounts_count
