'''
Important note: This problem targets those who have a good experience with SQL. If you are a beginner, we recommend that you skip it for now.

Implement the procedure PivotProducts to reorganize the Products table so that each row has the id of one product and its price in each store. The price should be null if the product is not sold in a store. The columns of the table should contain each store and they should be sorted in lexicographical order.

The procedure should return the table after reorganizing it.

Return the result table in any order.

The query result format is in the following example.
'''


CREATE PROCEDURE PivotProducts()
BEGIN
	# Write your MySQL query statement below.
    SET group_concat_max_len = 1000000; #This is tricky. There's a length limit on GROUP_CONCAT.
    SET @sql = NULL;
    SELECT
    GROUP_CONCAT(DISTINCT CONCAT(
      'SUM(IF(store = "', store, '", price, null)) AS ', store) ORDER BY store ASC)
    INTO @sql
    FROM Products;

    SET @sql = CONCAT('SELECT product_id, ', @sql, ' FROM Products GROUP BY product_id');
    

    PREPARE stmt FROM @sql;
    EXECUTE stmt;
    DEALLOCATE PREPARE stmt;
END
