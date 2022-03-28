'''
Write an SQL query to report the customers with postive revenue in the year 2021.

Return the result table in any order.

The query result format is in the following example.
'''

select customer_id from customers where year = 2021 and revenue > 0
