
'''

Write an SQL statement to delete teachers who have created courses before 2020 (excluding 2020) from the teachers table teachers.

'''

delete from teachers 


where id in (select k.id from ( select t.id from teachers t inner join courses c on c.teacher_id = t.id 
where created_at < '2020-01-01' )k );


