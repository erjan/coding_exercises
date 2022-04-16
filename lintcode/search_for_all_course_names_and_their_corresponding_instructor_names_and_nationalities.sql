'''
Write an SQL statement to full outer 
join the courses table courses and the teachers table teachers,then
query all course names and their corresponding teacher's names and nationalities, with the result columns named course name course_name, teacher name teacher_name and teacher nationality teacher_country respectively.
'''



SELECT

c.name as course_name,
t.name as teacher_name,

t.country as teacher_country

from  courses c left join teachers t  on c.teacher_id = t.id and  c.teacher_id is not null

union 

SELECT

c.name as course_name,
t.name as teacher_name,
t.country as teacher_country

from  courses c right join teachers t  on c.teacher_id = t.id and  t.id is  not null

---------------------------------
SELECT c.name AS `course_name`,t.name AS `teacher_name`,t.country AS `teacher_country`
FROM `courses` AS c 
    LEFT JOIN teachers AS t ON c.teacher_id = t.id
UNION 
SELECT c.name AS `course_name`,t.name AS `teacher_name`,t.country AS `teacher_country`
FROM `courses` AS c
    Right JOIN teachers AS t ON c.teacher_id = t.id;
