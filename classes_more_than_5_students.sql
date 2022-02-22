'''
Write an SQL query to report all the classes that have at least five students.

Return the result table in any order.

The query result format is in the following example.
'''


select class from courses 
group by class
having count(*) >=5
