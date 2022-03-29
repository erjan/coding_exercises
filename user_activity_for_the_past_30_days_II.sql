'''
Write an SQL query to find the average number of sessions per user for a period of 30 days 
ending 2019-07-27 inclusively, rounded to 2 decimal places. The sessions 
we want to count for a user are those with at least one activity in that time period.

The query result format is in the following example.
'''

SELECT ifnull(ROUND(COUNT(DISTINCT session_id)/COUNT(DISTINCT user_id), 2),0.00) 
AS average_sessions_per_user
FROM Activity 
WHERE activity_date >= '2019-06-28' and activity_date <= '2019-07-27'; 
