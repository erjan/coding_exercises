'''
Write an SQL query to report the name and balance of users with a balance higher than 10000. The balance of an account is equal to the sum of the amounts of all transactions involving that account.

Return the result table in any order.

The query result format is in the following example.
'''

#my own solution

with helper as(

select account, sum(amount) as balance from transactions

group by account
having balance > 10000)


select name,helper.balance from users inner join helper on helper.account= users.account

#another solution

select
    a.name,
    sum(b.amount) balance
from
    Users a
join
    Transactions b
on
    a.account = b.account
group by
    a.account
having
    balance > 10000;
