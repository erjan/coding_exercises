'''
Write an SQL query to report all the duplicate emails.

Return the result table in any order.

The query result format is in the following example.
'''

/* Write your T-SQL query statement below */


select distinct p1.email as Email 

from person p1 , person p2 where p1.email = p2.email and p1.id != p2.id
