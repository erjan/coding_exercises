'''

Write an SQL query to report the IDs of the transactions with the maximum amount on their respective day. If in one day there are multiple such transactions, return all of them.

Return the result table ordered by transaction_id in ascending order.

The query result format is in the following example.

'''
WITH temp AS(
    
SELECT date(day) d, max(amount) a

    FROM transactions
GROUP BY 1)


SELECT transaction_id
FROM transactions t1
JOIN temp t2
ON Date(t1.day)=t2.d
AND t1.amount=t2.a
ORDER BY 1
