'''
Write an SQL query to find the daily active user count for a period of 30 days ending 2019-07-27 inclusively. A user was active on someday if they made at least one activity on that day.

Return the result table in any order.

The query result format is in the following example.
'''


SELECT 
    activity_date AS day,
    COUNT(DISTINCT user_id) AS active_users
FROM Activity
GROUP BY 1
HAVING DATEDIFF('2019-07-27', day) < 30
    AND active_users >= 1;
