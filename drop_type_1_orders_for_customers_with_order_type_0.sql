'''

Write an SQL query to report all the orders based on the following criteria:

If a customer has at least one order of type 0, do not report any order of type 1 from that customer.
Otherwise, report all the orders of the customer.
Return the result table in any order.

The query result format is in the following example.

'''



SELECT order_id, customer_id, order_type FROM Orders WHERE order_type = 0
OR (order_type = 1 AND customer_id NOT IN (SELECT customer_id FROM Orders WHERE order_type = 0))


---

SELECT order_id, customer_id, order_type
FROM Orders
WHERE 
	order_type = 0 or 
	(order_type = 1 and customer_id not in (
		SELECT customer_id
		FROM Orders
		WHERE order_type = 0)
	)
;
