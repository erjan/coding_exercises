'''
The students table stores all student information, including student id and student name
The companies table stores all company information, including company id and company name
The recording table stores all resume delivery data, including student id (student_id) and company id (company_id)
Please write SQL statements to query the names of all students who have not submitted their resumes to Alibaba.
'''


select name from students where name not in

 (select students.name from students inner join recording on recording.student_id = students.id 
 
 inner join companies on companies.id = recording.company_id where companies.name = 'Alibaba'   )
