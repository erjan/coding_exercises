
'''

A bank account is suspicious if the total income exceeds the max_income for this account 
for two or more consecutive months. The total income of an account in some month is the 
sum of all its deposits in that month (i.e., transactions of the type 'Creditor').

Write an SQL query to report the IDs of all suspicious bank accounts.

Return the result table ordered by transaction_id in ascending order.

The query result format is in the following example.

'''

WITH temp AS (
SELECT t.account_id, DATE_FORMAT(day,'%Y%m') AS date, SUM(amount) AS 'income', Accounts.max_income
FROM Transactions t
LEFT JOIN Accounts ON Accounts.account_id=t.account_id
WHERE t.type='Creditor'
GROUP BY t.account_id, DATE_FORMAT(day,'%Y%m')
HAVING SUM(amount)>Accounts.max_income
)

SELECT t1.account_id
FROM temp t1, temp t2
WHERE t1.account_id=t2.account_id AND PERIOD_DIFF(t1.date, t2.date)=1
GROUP BY t1.account_id
ORDER BY t1.account_id


---------------------------

with cte as
(
select month(day) mon, account_id, sum(amount) tot_income
from Transactions
where type = 'Creditor'
group by month(day), account_id
), cte2 as
(
select a.account_id, mon, tot_income, max_income, mon-row_number() over (partition by a.account_id order by mon) grp
from cte c
join Accounts a on c.account_id = a.account_id
where tot_income>max_income
)

select distinct account_id
from cte2
group by grp, account_id
having count(*)>1
