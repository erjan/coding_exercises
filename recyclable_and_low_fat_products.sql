'''
Write an SQL query to find the ids of products that are both low fat and recyclable.

Return the result table in any order.

The query result format is in the following example.
'''

select product_id from products
where low_fats = 'Y' and recyclable = 'Y'
