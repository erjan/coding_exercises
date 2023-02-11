
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
