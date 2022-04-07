'''


Write an SQL query to find the missing customer IDs. The missing IDs are ones that are not in the Customers table but are in the range between 1 and the maximum customer_id present in the table.

Notice that the maximum customer_id will not exceed 100.

Return the result table ordered by ids in ascending order.

The query result format is in the following example.

'''

WITH recursive numbers AS (
    select 1 as ids
   union all
   select ids + 1
   from numbers
   where ids < (select max(customer_id) from customers))


select ids from numbers where 

ids not in (select customer_id from customers)


---------------------------------------------------------------------


WITH RECURSIVE id_seq AS (
    SELECT 1 as continued_id
    UNION 
    SELECT continued_id + 1
    FROM id_seq
    WHERE continued_id < (SELECT MAX(customer_id) FROM Customers) 
)

SELECT continued_id AS ids
FROM id_seq
WHERE continued_id NOT IN (SELECT customer_id FROM Customers)  
