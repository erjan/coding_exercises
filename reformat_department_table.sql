'''
Write an SQL query to reformat the table such that there is a department id column and a revenue column for each month.

Return the result table in any order.

The query result format is in the following example.
'''

SELECT
  id   
 ,"Jan" AS "Jan_Revenue"
 ,"Feb" AS "Feb_Revenue"
 ,"Mar" AS "Mar_Revenue"
 ,"Apr" AS "Apr_Revenue"
 ,"May" AS "May_Revenue"
 ,"Jun" AS "Jun_Revenue"  
 ,"Jul" AS "Jul_Revenue" 
 ,"Aug" AS "Aug_Revenue" 
 ,"Sep" AS "Sep_Revenue" 
 ,"Oct" AS "Oct_Revenue" 
 ,"Nov" AS "Nov_Revenue" 
 ,"Dec" AS "Dec_Revenue" 
FROM (SELECT
    id
   ,revenue
   ,month
  FROM Department) p
PIVOT
(
 sum(revenue) FOR month IN ("Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"  )
) AS t
ORDER BY t.id;
