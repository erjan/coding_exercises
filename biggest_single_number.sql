'''

A single number is a number that appeared only once in the MyNumbers table.

Write an SQL query to report the largest single number. If there is no single number, report null.

The query result format is in the following example.
'''

with h as(

select num as x

from mynumbers

group by num
having count(num) = 1
order by num desc limit 1)


select if ( (select x from h) = 0, null , (select x from h)) as num




#another

select if(count(*) =1, num, null) as num from number 
group by num order by count(*), num desc limit 1
