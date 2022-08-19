'''
The cancellation rate is computed by dividing the number of canceled (by client or driver) requests with unbanned users by the total number of requests with unbanned users on that day.

Write a SQL query to find the cancellation rate of requests with unbanned users (both client and driver must not be banned) each day between "2013-10-01" and "2013-10-03". Round Cancellation Rate to two decimal points.

Return the result table in any order.

The query result format is in the following example.
'''


SELECT  t.request_at AS "Day",
        ROUND(
            COUNT(CASE
                    WHEN t.status != 'completed' THEN 1     -- numerator is total cancelled trips
                    ELSE NULL
                 END) / COUNT(id)                           -- denominator is all trips for that day
        , 2) AS "Cancellation Rate"
FROM    trips AS t
JOIN    users AS client                                     -- users table role-playing as client
ON      t.client_id = client.users_id
AND     client.banned = 'No'                                -- unbanned client
JOIN    users AS driver                                     -- users table role-playing as driver
ON      driver.users_id = t.driver_id
AND     driver.banned = 'No'                                -- unbanned driver
AND     t.request_at BETWEEN '2013-10-01' 
                         AND '2013-10-03'
GROUP BY t.request_at;  
