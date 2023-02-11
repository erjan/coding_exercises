'''
Write an SQL query to report the sum of prices paid by the customers of each salesperson. If a salesperson does 
not have any customers, the total value should be 0.

Return the result table in any order.

The query result format is shown in the following example.
'''


select s.salesperson_id, s.name, ifnull(sum(price),0) as total


 from salesperson s left join customer c on s.salesperson_id = c.salesperson_id
left join sales s2 on s2.customer_id = c.customer_id

group by s.salesperson_id



