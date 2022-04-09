'''

Write an SQL query to report the number of accounts that
bought a subscription in 2021 but did not have any stream session.

The query result format is in the following example.

'''


SELECT COUNT(account_id) AS accounts_count  # find counts
FROM Subscriptions
WHERE YEAR(start_date) <= 2021 AND YEAR(end_date) >= 2021 # has subscription in 2021
	AND account_id NOT IN (SELECT account_id FROM Streams WHERE YEAR(stream_date) = '2021') # has no streams in 2021
