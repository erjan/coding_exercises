'''
Write an SQL query that reports the spending of each user.

Return the resulting table ordered by spending in descending order. In case of a tie, order them by user_id in ascending order.

The query result format is in the following example.
'''


with h as(
select s.user_id, s.product_id, price * sum(quantity) as spending from sales s inner join product p on s.product_id = p.product_id

group by s.user_id, s.product_id

order by spending desc, s.user_id)


select user_id, sum(spending) as spending from h

group by user_id 
order by spending desc, user_id



SELECT s.user_id,
  SUM(quantity * price) as spending
FROM Sales s INNER JOIN Product p USING(product_id)
GROUP BY s.user_id
ORDER BY 2 desc
