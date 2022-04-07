
'''

Write an SQL query to report the balance of each user after each transaction. You may assume that the balance of each account before any transaction is 0 and that the balance will never be below 0 at any moment.

Return the result table in ascending order by account_id, then by day in case of a tie.

The query result format is in the following example.

'''


select  

account_id, day,

sum(case when type='Deposit' then amount else -amount end  ) over(partition by  account_id order by day )  as balance
   
from transactions


---------------------------------------------

select
t1.account_id,
t1.day,
sum(case when t2.type = 'Deposit' then t2.amount
   when t2.type = 'Withdraw' then -t2.amount
    else 0 end) as balance
    
from transactions t1, transactions t2
where t1.account_id = t2.account_id and t1.day >= t2.day
group by 1,2
order by 1,2
