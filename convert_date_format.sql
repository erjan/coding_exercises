'''
Write an SQL query to convert each date in Days into a string formatted as "day_name, month_name day, year".

Return the result table in any order.

The query result format is in the following example.
'''


SELECT concat(DAYNAME(day), 
              ', ', monthname(day), 
              ' ', DAYOFMONTH(day), 
              ', ' 
              , year(day) ) 
              as day


from days

#another solution

SELECT DATE_FORMAT(day, "%W, %M %e, %Y") AS day
FROM Days
