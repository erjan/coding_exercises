
'''
Write an SQL query to report the latest login for all users in the year 2020. Do not include the users who did not login in 2020.

Return the result table in any order.

The query result format is in the following example.
'''


with h1 as(

SELECT user_id, time_stamp FROM logins WHERE YEAR(time_stamp) = 2020 )


SELECT tt.user_id, time_stamp as last_stamp 
FROM h1 tt
INNER JOIN
    (SELECT user_id, MAX(time_stamp) AS MaxDateTime
    FROM h1
    GROUP BY user_id) groupedtt 
ON tt.user_id = groupedtt.user_id 
AND tt.time_stamp = groupedtt.MaxDateTime





SELECT
    user_id,
    MAX(time_stamp) AS last_stamp #obtaining latest login for all users
FROM Logins
WHERE YEAR(time_stamp) = 2020 #filtering for login dates with year 2020 in timestamp
GROUP BY user_id;
