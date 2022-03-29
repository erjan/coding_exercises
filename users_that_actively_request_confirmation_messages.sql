'''
Write an SQL query to find the IDs of the users that requested a confirmation message twice within a 24-hour window. Two messages exactly 24 hours apart are considered to be within the window. The action does not affect the answer, only the request time.

Return the result table in any order.

The query result format is in the following example.
'''


SELECT DISTINCT c1.user_id FROM Confirmations c1, Confirmations c2
WHERE c1.user_id = c2.user_id AND
      c1.time_stamp < c2.time_stamp AND
      c1.time_stamp >= date_sub(c2.time_stamp, interval 24 hour)
