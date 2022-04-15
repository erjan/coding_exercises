'''
Question Description: Write a SQL statement to query the 
creation time of courses in the course table which 
output in 'hour:minute:second' format, and the returned column named created_at.
'''


select

right(created_at, 8) as created_at
-- DATE_FORMAT(created_at, '%H:%i:%s') as created_at
-- time(created_at) as created_at

from courses
