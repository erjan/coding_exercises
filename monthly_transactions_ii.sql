'''

Write an SQL query to find for each month and country: the number of approved transactions and their total amount, the number of chargebacks, and their total amount.

Note: In your query, given the month and country, ignore rows with all zeros.

Return the result table in any order.

The query result format is in the following example.

 
 
 '''

select *  #wrapper to take-off rows with all zeros
from (
    select date_format(trans_date, '%Y-%m') month, country,
        sum( case when state='approved' then 1 else 0 end) approved_count,
        sum( case when state='approved' then amount else 0 end) approved_amount,
        sum( case when state='charge' then 1 else 0 end) chargeback_count,
        sum( case when state='charge' then amount else 0 end) chargeback_amount
    from (
        select * 
        from Transactions
        union all
            select c.trans_id id, t.country, 'charge' state, t.amount, c.trans_date
            from Chargebacks c
            left join Transactions t
            on t.id = c.trans_id
        ) t1
    group by date_format(trans_date, '%Y-%m'), country
    ) t2
where approved_count+chargeback_count!=0




SELECT
DATE_FORMAT(trans_date,'%Y-%m') AS month,
country,
SUM(CASE WHEN state='approved' THEN 1 ELSE 0 END) AS approved_count,
SUM(CASE WHEN state='approved' THEN amount ELSE 0 END) AS approved_amount,
SUM(CASE WHEN state='chargebacks' THEN 1 ELSE 0 END) AS chargeback_count,
SUM(CASE WHEN state='chargebacks' THEN amount ELSE 0 END) AS chargeback_amount
FROM
(SELECT *
FROM Transactions
UNION ALL
SELECT
trans_id AS id,
(SELECT country FROM Transactions WHERE id=trans_id) AS country,
'chargebacks' AS state,
(SELECT amount FROM Transactions WHERE id=trans_id) AS amount,
trans_date
FROM Chargebacks) AS t
GROUP BY country,DATE_FORMAT(trans_date,'%Y-%m')
HAVING
approved_count!=0 OR
approved_amount!=0 OR
chargeback_count!=0 OR
chargeback_amount!=0
