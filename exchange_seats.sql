'''
Write an SQL query to swap the seat id of every two consecutive students. If the number of students is odd, the id of the last student is not swapped.

Return the result table ordered by id in ascending order.

The query result format is in the following example.
'''


select id,
case 
    when id%2 = 0 then (select student from seat where id = (i.id-1) )  
    when id%2 != 0 and id<(select count(student) from seat) then (select student from seat where id = (i.id+1) )  
    else student
end as student
from seat i 
