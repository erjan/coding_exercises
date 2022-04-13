'''
A bank wants to draw a chart of the number of transactions bank visitors did in one visit to the bank and the corresponding number of visitors who have done this number of transaction in one visit.

Write an SQL query to find how many users visited the bank and didn't do any transactions, how many visited the bank and did one transaction and so on.

The result table will contain two columns:

transactions_count which is the number of transactions done in one visit.
visits_count which is the corresponding number of users who did transactions_count in one visit to the bank.
transactions_count should take all values from 0 to max(transactions_count) done by one or more users.

Return the result table ordered by transactions_count.

The query result format is in the following example.
'''


WITH a AS
(
    SELECT v.user_id, v.visit_date, 
    SUM(CASE WHEN t.transaction_date is not null THEN 1 ELSE 0 END) as transactions_count
    FROM Visits v
    LEFT JOIN Transactions t
    ON v.user_id = t.user_id AND v.visit_date = t.transaction_date
    GROUP BY visit_date, v.user_id
),

b AS
(
    SELECT transactions_count, COUNT(transactions_count) as visits_count
    FROM a
    GROUP BY transactions_count
),

c as
(
    SELECT 0 as transactions_count, max(transactions_count) as temp
    FROM b
	UNION ALL
    SELECT transactions_count + 1 , temp FROM c
    WHERE transactions_count < temp
)

SELECT c.transactions_count, isnull(b.visits_count, 0) as visits_count
FROM c
LEFT JOIN b
ON c.transactions_count = b.transactions_count

------------------------------------------------------

# This t table calculates the number of transactions for each user, for each visit (including if the user had zero transactions for that visit)
WITH t AS (SELECT v.user_id as user_id, visit_date, IF(transaction_date is null, 0, count(*)) as transaction_count
            FROM Visits v LEFT JOIN Transactions t on v.visit_date = t.transaction_date and v.user_id=t.user_id
            GROUP BY 1, 2),
	# This simply generates a table with numbers from zero to [number of rows in Transactions table]
	# This will be necessary later to deal with edge cases for when there are zero of that number of transactions
	# but we still want to see that in the end result (eg there were zero cases of two-transactions but there were cases with three-transactions)
    row_nums AS (SELECT ROW_NUMBER() OVER () as rn 
                 FROM Transactions 
                 UNION 
                 SELECT 0) 
				 
# If transaction_count is null (due to the right join below), then insert a zero, otherwise simply count the times that number appears
SELECT rn as transactions_count, IF(transaction_count is null, 0, count(*)) as visits_count
# Right Join on row_nums (right join because we don't want to lose, for example, two-transactions being zero)
FROM t RIGHT JOIN row_nums ON transaction_count = rn
# We can remove excess transaction-numbers (eg if the max transaction-number is four, we don't need five+ in our end result)
WHERE rn <= (SELECT MAX(transaction_count) FROM t)
GROUP BY rn
ORDER BY 1

---------------------------------------------------------------------------------
Tricky part of problem
This problem involves a few translations between the number of visits--> number of transactions --> number of occurances and so it is really easy to aggregate the wrong column. Also, it is easy to confuse which aggregate function to use.

Do you aggregate visit_date or transaction_date
Do you SUM or COUNT?
Tip: Work backwards to figure out which tables you will ultimately need

In the final solution you need the following:
+-------------------+--------------+
| transactions_count | visits_count |
+-------------------+--------------+
But to get that you need a table like this:
+----------+---------------------------+
| visit_date | num_transactions_by_date |
+----------+---------------------------+
But to get num_transactions_by_date you need a table like this:
+------+----------+-------------------------------------+
| users | visit_date | num_transactions_by_users_by_date
+------+----------+-------------------------------------+

CTE Tables needed
num_transactions_by_users_by_date
image

num_transactions_by_date
image

num_transactions ( aka row_number)
image

final_table (still need to remove NULL rows but we will deal with that below)
image

STEP 1. Create CTEs
a. Tip: test each CTE to make sure they work before creating final table.
--> Use smaller test case to make it easier to see if expected results are corect
--> Comment out filter after successful run
--> I used where user_id in (1,2)
b. Tip: If expected results only returning on row but there should be multiple, likely mising a GROUP BY statement

STEP 2. Write out query that will return the max_num_transactions based off of CTE table num_transactions
--> We will use this to filter out NULL values in the final query
--> Test it out and make sure it only returns a single value
--> We are using this only as reference for step 3, so comment out so it does not affect the rest of the code.

STEP 3. Create final select query
a. Make sure to use COUNT and not SUM when calcuating visits_count column.
--> SUM will return a NULL value if no entry while COUNT will return 0
b. Remove rows where the value in the transactions column is is greater than max_num_transactions from step 2
--> Uncomment Select query from step 3
--> Highlight/copy entire SELECT query
--> Paste into final query (Make sure to paste inside of parentheses)

Pseudocode for CTE tables

WITH
	## This is to add 0s to dates when user visite but didn't complete a transaction
    num_transactions_by_users_by_date AS -- ntbubd
    (< insert query1 here>)
    
    , num_transactions_by_date as --ntbd 
     (< insert query2 here>)

	-- This is to list the give an ordered list starting from 0 up to the max_number_transactions
    ,num_transactions as --nt 
     (< insert query3 here>)
Final MySQL Query

WITH 
    # This is to add 0s to dates when user visite but didn't complete a transaction
    num_transactions_by_users_by_date AS #nvbubd
    (
        SELECT v.user_id
            , visit_date
            , count(transaction_date) AS num_transactions
        FROM visits v
        LEFT JOIN Transactions t        
        ON v.user_id = t.user_id
        AND v.visit_date = t.transaction_date
        -- where v.user_id in (1,2) -- for testing only
        GROUP BY 1, 2
        ORDER BY 1, 2
    )
    
    , num_transactions_by_date AS #ntbd
    (
        SELECT user_id  # not really necessary but leaving it in for testing small use case
            ,visit_date
            , sum(num_transactions) AS num_transactions
        FROM num_transactions_by_users_by_date
        -- where user_id in (1,2)  # for testing only
        GROUP BY 1,2
        ORDER BY 1,2
    )
    
    # This is to list the give an ordered list starting from 0 up to the max_number_transactions      
    ,num_transactions AS #nt
    (
        SELECT row_number() over () as num_transactions
        FROM transactions
        UNION select 0   
    )
    
# ******************************************   
# Test CTEs
# ******************************************   

# SELECT * FROM num_transactions_by_users_by_date
# SELECT * FROM num_transactions_by_date
# SELECT * FROM num_transactions


# ******************************************   
# Max number of calculations
# ****************************************** 

# SELECT MAX(num_transactions) FROM num_transactions_by_date

# ******************************************   
# Final Query
# ******************************************  

SELECT nt.num_transactions AS transactions_count
	, COUNT(ntbd.num_transactions) AS visits_count
FROM num_transactions AS nt
LEFT JOIN num_transactions_by_date AS ntbd
ON nt.num_transactions = ntbd.num_transactions
WHERE nt.num_transactions <= (SELECT MAX(num_transactions) FROM num_transactions_by_date)
# AND ntbd.user_id in (1,2) -- for testing only
GROUP BY 1
ORDER by 1
Take aways and learnings after many multiple failed attempts.
Mapping things out on whiteboard with expected results before writing the query was most helpful in keeping everything straight
