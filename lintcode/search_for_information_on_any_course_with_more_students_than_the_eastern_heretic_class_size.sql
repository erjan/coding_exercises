'''
Write an SQL statement that queries
the information of courses with total students more than 
any courses taught by 'Eastern Heretic' from the courses table and the teachers table (greater than any one of these will suffice).
'''

select c.* from courses c inner join teachers t on t.id = c.teacher_id 

where c. student_count > ANY(select student_count from courses inner join teachers on teachers.id= courses.teacher_id 
where teachers.name = 'Eastern Heretic') and t.name != 'Eastern Heretic'



---------------------
SELECT * FROM courses
WHERE student_count > ANY(
	SELECT student_count FROM courses 
	WHERE teacher_id = (
		SELECT id FROM teachers 
		WHERE name = 'Eastern Heretic'
	)
)  AND teacher_id != (
	SELECT id FROM teachers 
	WHERE name = 'Eastern Heretic'
)
