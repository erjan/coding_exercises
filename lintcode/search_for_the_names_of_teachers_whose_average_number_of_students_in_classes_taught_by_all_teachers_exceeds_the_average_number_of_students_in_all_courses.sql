
'''
Write an SQL statement that query 
the namename of teachers whose average number of students of all courses
they taught more than the average of all courses from the course table courses
'''


SELECT
t.name
from  courses c inner join teachers t on c.teacher_id = t.id
group by t.name
having avg(student_count)  > (select avg(student_count) from courses)


-----------------------------------
select name from teachers where id in(
    
    select c1.teacher_id from
    (select teacher_id ,avg(student_count) gtavg from courses group by teacher_id) c1,
    (select avg(student_count) gcavg from courses ) c2
    where c1.gtavg>c2.gcavg

)

-------------------------------------------------

select t.name from teachers t
inner join courses c 
on t.id=c.teacher_id
group by c.teacher_id
having avg(student_count)>(
    select avg(student_count) 
    from courses 
    
)
