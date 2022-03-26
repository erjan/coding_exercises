'''
Write an SQL query to find the customer_number for the customer who has placed the largest number of orders.

The test cases are generated so that exactly one customer will have placed more orders than any other customer.

The query result format is in the following example.
'''

# Write your MySQL query statement below



select customer_number from (

select customer_number, count(order_number) as total from orders

group by customer_number 

order by total desc ) k limit 1



#solution for the follow-up

select customer_number
from orders
group by customer_number
having count(order_number) = (select count(*) as count
                              from orders
                              group by customer_number
                              order by count desc limit 1);
