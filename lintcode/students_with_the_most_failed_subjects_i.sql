'''Please use SQL statement to find the student_id corresponding to the student with the largest number of failed subjects.
'''


select student_id from 
(
	select student_id, sum(if(is_pass=0,1,0)) as failed
	from exams	
	group by student_id
	having failed > 0
	order by failed desc	
	limit 1
) t1
