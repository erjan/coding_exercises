# Write your MySQL query statement below


'''
Write an SQL query to report all the sessions that did not get shown any ads.

Return the result table in any order.

The query result format is in the following example.

'''


select   session_id

from  playback left join ads on playback.customer_id = ads.customer_id and ads.timestamp between start_time and end_time

where ads.customer_id is null



#another
SELECT DISTINCT session_id
FROM Playback
WHERE session_id NOT IN 
(SELECT DISTINCT p.session_id
FROM Playback p LEFT JOIN Ads a ON p.customer_id = a.customer_id
WHERE a.timestamp BETWEEN p.start_time AND p.end_time)
