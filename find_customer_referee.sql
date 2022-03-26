'''
Write an SQL query to report the IDs of the customer that are not referred by the customer with id = 2.

Return the result table in any order.

The query result format is in the following example.
'''



select name from customer where referee_id is null or referee_id not in (

select referee_id from customer

where referee_id = 2)
