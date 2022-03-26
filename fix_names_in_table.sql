'''
Write an SQL query to fix the names so that only the first character is uppercase and the rest are lowercase.

Return the result table ordered by user_id.

The query result format is in the following example.
'''

select user_id, CONCAT(UPPER(SUBSTRING(name,1,1)),(SUBSTRING(name,2))) as name from (

select user_id, lower(name) as name from users)k

order by user_id
