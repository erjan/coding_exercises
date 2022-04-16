'''
Please write a SQL statement to query the information 
of all teachers who are not Chinese and not older than 20 years old(excluding 20) in the table teachers .
'''



select * from teachers

where not ( country = 'CN'  and  age > 20)


select *
from teachers 
where age<=20 or country !='CN'

----------------------------------------------


#this is wrong!!!


select * from teachers

where  country != 'CN'  and  age <= 20
