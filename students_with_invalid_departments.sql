'''
Write an SQL query to find the id and the name of all students who are enrolled in departments that no longer exist.

Return the result table in any order.

The query result format is in the following example.
'''


select students.id, students.name 
from students left join 
departments  on students.department_id = departments.id

where departments.id is null
