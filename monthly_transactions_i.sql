

'''
Write an SQL query to find for each month and country, the number of transactions and their total amount, the number of approved transactions and their total amount.

Return the result table in any order.

The query result format is in the following example.

'''

select

CONCAT(YEAR(t.trans_date),'-',LPAD(MONTH(t.trans_date),2,'00')) as month,
country,
count(id) as trans_count,

sum(case when state = 'approved' then 1 else 0 end) as approved_count,
sum( amount  ) as trans_total_amount ,
sum(case when state= 'approved' then amount else 0 end ) as approved_total_amount 

from transactions t
GROUP BY YEAR(t.trans_date), MONTH(t.trans_date), country



---------------------------

select
      DATE_FORMAT(trans_date,"%Y-%m") as month,
      country,
      count(id) as trans_count,
      sum(case when state = 'approved' then 1 else 0 end) approved_count,
      sum(amount) as trans_total_amount,
      sum(case when state = 'approved' then amount else 0 end) approved_total_amount
from Transactions
       group by country, month
