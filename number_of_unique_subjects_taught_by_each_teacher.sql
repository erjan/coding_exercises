'''
Write an SQL query to report the number of unique subjects each teacher teaches in the university.

Return the result table in any order.

The query result format is shown in the following example.
'''


select teacher_id, count(distinct subject_id) as cnt from teacher

group by teacher_id
