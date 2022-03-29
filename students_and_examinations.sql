'''
Write an SQL query to find the number of times each student attended each exam.

Return the result table ordered by student_id and subject_name.

The query result format is in the following example.
'''

select 
students.student_id,
students.student_name, 
subjects.subject_name,
count( examinations.subject_name) as attended_exams

from students 
join subjects 
left join examinations 
on students.student_id = examinations.student_id
and subjects.subject_name = examinations.subject_name
group by students.student_id, subjects.subject_name
order by students.student_id, subjects.subject_name
