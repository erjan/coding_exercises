'''
Write an SQL query to rearrange the Products table so that each row has (product_id, store, price). 
If a product is not available in a store, do not include a row with that product_id and store combination in the result table.

Return the result table in any order.

The query result format is in the following example.
'''



select product_id,'store1' as store, store1 as price from products where store1 is not null
union
select product_id,'store2' as store, store2 as price from products where store2 is not null
union
select product_id,'store3' as store, store3 as price from products where store3 is not null
