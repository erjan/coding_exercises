
'''
Write a SQL statement to calculate the number of 
days difference from 26/3/2019 to the course creation time (created at) in the courses 
table, with the result column named date_diff.
'''


select timestampdiff(day, '2019-03-26',created_at) as date_diff

from courses
