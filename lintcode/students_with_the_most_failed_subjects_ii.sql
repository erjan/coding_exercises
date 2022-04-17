'''
The exams records of students are stored in the exam table
Please use SQL statement to find the student_id corresponding to the student with the largest number of failed subjects.
'''



select student_id
from exams 
where is_pass = 0
group by student_id
having count(*) = (
	select max(c.c) from 
	(select count(*) as c 
	from exams where is_pass = 0 
	group by 
	student_id ) c)
