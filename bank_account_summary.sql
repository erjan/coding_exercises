'''

Leetcode Bank (LCB) helps its coders in making virtual payments. Our bank records all transactions in the table Transaction, we want to find out the current balance of all users and check whether they have breached their credit limit (If their current credit is less than 0).

Write an SQL query to report.

user_id,
user_name,
credit, current balance after performing transactions, and
credit_limit_breached, check credit_limit ("Yes" or "No")
Return the result table in any order.

The query result format is in the following example.

'''

with h as(

select user_id, credit from users 
union all

select paid_by as user_id, -1*amount as amount from transactions
union all

select paid_to as user_id , amount as amount from transactions)




select u.user_id, user_name,sum(h.credit) as credit,

case when sum(h.credit) >=0 then "No" else "Yes" end as credit_limit_breached

from h join users u using(user_id)

group by u.user_id


-------------------------
SELECT user_id,user_name,
IFNULL(SUM(CASE WHEN a.user_id=b.paid_by THEN -amount ELSE amount END),0)+a.credit as credit,
CASE WHEN IFNULL(SUM(CASE WHEN a.user_id=b.paid_by THEN -amount ELSE amount END),0)>=-a.credit THEN "No" ELSE "Yes" END as credit_limit_breached
FROM Users as a
LEFT JOIN Transactions as b
ON a.user_id=b.paid_by OR a.user_id=b.paid_to
GROUP BY a.user_id;
