'''
There is a competition between New York University and California University. The competition is held between the same number of students from both universities. The university that has more excellent students wins the competition. If the two universities have the same number of excellent students, the competition ends in a draw.

An excellent student is a student that scored 90% or more in the exam.

Write an SQL query to report:

"New York University" if New York University wins the competition.
"California University" if California University wins the competition.
"No Winner" if the competition ends in a draw.
The query result format is in the following example.
'''

# Write your MySQL query statement below

with h1 as(
select  count(student_id) 

from newyork
where score >=90),

h2 as(
select  count(student_id) 

from california
where score >=90)



SELECT (CASE 
            WHEN (SELECT * from h1) > (SELECT * from h2) THEN 'New York University'
            WHEN (SELECT * from h1) < (SELECT * from h2) THEN 'California University'
            ELSE 'No Winner' END) AS WINNER
;


