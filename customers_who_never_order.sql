'''
Write an SQL query to report all customers who never order anything.

Return the result table in any order.

The query result format is in the following example.
'''

select name as Customers from customers c where c.id not in (
select customerId from orders)
