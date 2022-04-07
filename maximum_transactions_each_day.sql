'''

Write an SQL query to report the IDs of the transactions with the maximum amount on their respective day. If in one day there are multiple such transactions, return all of them.

Return the result table ordered by transaction_id in ascending order.

The query result format is in the following example.

'''



with h as(

select date(day) d, max(amount) a
    
    from transactions group by d )
         
select 

transaction_id

from transactions t join h t2 on t2.d = date(t.day) and t2.a = t.amount

order by 1

----------------

SELECT  
	transaction_id
FROM
(
SELECT 
   transaction_id,
   day,
   amount,
   rank() OVER(PARTITION BY date(day) ORDER BY amount DESC) as rnk
FROM
    Transactions
) as t
WHERE rnk =1
ORDER BY 1
