'''
Write an SQL query to delete all the duplicate emails, keeping only one unique
email with the smallest id. Note that you are supposed to write a DELETE statement and not a SELECT one.

Return the result table in any order.

The query result format is in the following example.
'''


delete from person where id not in (

select t1.id from (
select min(id) as id from person group by email
    ) t1
)
