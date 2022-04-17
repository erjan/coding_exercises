
'''
The students table stores information about all students, including student id and student name name.
The companies table stores all company information, including company id, company name name and company address address.
The records table stores all CV submissions, including student id (student_id) and company id (company_id)
Write an SQL statement to query the name and address of the company that receives the most resumes.
'''



select name, address from
companies where companies.id in (
select company_id 
from records  
group by company_id
having count(*) = ( select count(*) as x from records group by company_id order by x desc limit 1))
