'''
Important note: This problem targets those who have a good experience with SQL. If you are a beginner, we recommend that you skip it for now.

Implement the procedure UnpivotProducts to reorganize the Products table so that each row has the id of one product, the name of a store where it is sold, and its price in that store. If a product is not available in a store, do not include a row with that product_id and store combination in the result table. There should be three columns: product_id, store, and price.

The procedure should return the table after reorganizing it.

Return the result table in any order.

The query result format is in the following example.
'''



CREATE PROCEDURE UnpivotProducts()
BEGIN
	# Write your MySQL query statement below.
    set session group_concat_max_len = 1000000;
    
    set @macro = null;
    
	select group_concat(
        concat(
            'select product_id, "', `column_name`, '" as store, ', `column_name`,
            ' as price from products where ', `column_name`, ' is not null'
        ) separator ' union '
    )
        into @macro
        from `information_schema`.`columns`
        where `table_schema`='test' and `table_name`='products' and `column_name` != 'product_id';
    
    prepare sql_query from @macro;
    execute sql_query;
    deallocate prepare sql_query;
END
