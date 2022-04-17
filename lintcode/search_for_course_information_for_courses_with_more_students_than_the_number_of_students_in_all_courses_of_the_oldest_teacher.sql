'''
Write an SQL statement
that queries the student count of courses taught by the oldest
teacher from the teacher table teachers and the course table courses, and 
finally returns the information of courses in which the number of students exceeds all those courses.
'''

select * from courses
where student_count > all (
select c.student_count
from teachers t join courses c
on t.id = c.teacher_id
where t.age = (
select max(age) from teachers
) )
