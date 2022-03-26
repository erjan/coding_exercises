'''
Write an SQL query to report the names of all the salespersons who did not have any orders related to the company with the name "RED".

Return the result table in any order.

The query result format is in the following example.
'''

SELECT name from salesperson
where sales_id not in 
(
    select sales_id from orders where com_id in 
	(select com_id from company where name='RED')
)
