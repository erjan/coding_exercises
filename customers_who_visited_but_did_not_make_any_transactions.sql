'''
Write an SQL query to find the IDs of the users who visited without making any transactions and the number of times they made these types of visits.

Return the result table sorted in any order.

The query result format is in the following example.
'''


select customer_id, count(visits.visit_id) as count_no_trans from visits

where visits.visit_id not in (select transactions.visit_id from transactions)

group by customer_id
