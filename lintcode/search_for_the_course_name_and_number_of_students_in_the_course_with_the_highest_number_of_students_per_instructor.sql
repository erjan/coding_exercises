
'''
Write an SQL statement 
to query the course name name and the number of students student_count 
for the course with the most students taught by each teacher from the course table courses.
'''


select `name`, student_count from courses
where (teacher_id, student_count) in
(
    select teacher_id, max(student_count) from courses
    group by teacher_id
)
