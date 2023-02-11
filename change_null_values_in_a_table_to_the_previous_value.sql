
'''
Write an SQL query to replace the null values of drink with the name of the drink of the 
previous row that is not null. It is guaranteed that the drink of the first row of the table is not null.

Return the result table in the same order as the input.

The query result format is shown in the following example.
'''


Idea:

Create an identifer grp that identifies continuous blocks of rows that should all use the same drink, using a cumulative sum
Use first_value to get the drink from the first row in the group
Code:

WITH cte AS (
    SELECT
        *,
        SUM(IF(drink IS NOT NULL, 1, 0)) over win AS grp
    FROM
        CoffeeShop 
    WINDOW win AS (
        ROWS BETWEEN UNBOUNDED preceding
        AND CURRENT ROW
        )
)

SELECT
    id,
    first_value(drink) over(PARTITION by grp) AS drink
FROM
    cte;
    
---------------------------------------------------------------------------------------------
WITH RECURSIVE WithRowNum (row_num, id, drink) AS (
    SELECT
        ROW_NUMBER() OVER() AS row_num,
        id,
        drink
    FROM CoffeeShop
), Result (row_num, id, drink) AS (
    SELECT
        row_num,
        id,
        drink
    FROM WithRowNum
    WHERE row_num = 1
    UNION ALL
    SELECT
        WithRowNum.row_num,
        WithRowNum.id,
        IFNULL(WithRowNum.drink, Result.drink) AS drink
    FROM Result
    JOIN WithRowNum
    ON Result.row_num = WithRowNum.row_num - 1
)

SELECT id, drink
FROM Result;

--------------------
WITH cte AS (SELECT id, drink, ROW_NUMBER() OVER () AS nb FROM CoffeeShop), -- nb = initial row order
     cte2 AS (SELECT id, drink, nb, SUM(1-ISNULL(drink)) OVER (ORDER BY nb) AS group_id FROM cte) -- same group_id -> same drink
SELECT id, FIRST_VALUE(drink) OVER (PARTITION BY group_id) AS drink
FROM cte2
ORDER BY nb;
