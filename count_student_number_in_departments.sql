'''

Write an SQL query to report the respective department name and number of students majoring in each department for all departments in the Department table (even ones with no current students).

Return the result table ordered by student_number in descending order. In case of a tie, order them by dept_name alphabetically.

The query result format is in the following example.

'''

select 

dept_name,
count(student_id) as student_number

from student right join department using(dept_id)

group by dept_id

order by student_number desc
