

'''
Write an SQL statement to obtain 
the number of students in each course taught by the teacher 
Western Venom, then query the courses with student count more than all of Western 
Venom taught and return the information of these courses.
'''


select c.* from courses c left join teachers t on t.id = c.teacher_id

where c.student_count > all(

select student_count from courses c left join teachers t on t.id = c.teacher_id where t.name= 'Western Venom')





------------------------------------------
select * from courses where student_count >
all (select student_count from courses 
where teacher_id in (select id from teachers where name ='Western Venom'));

-----------------------------------------------

SELECT * FROM courses
WHERE student_count > ALL(
	SELECT student_count FROM courses 
	WHERE teacher_id = (
		SELECT id FROM teachers WHERE name = 'Western Venom'
	)
)
