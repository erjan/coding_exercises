'''
Write an SQL query to report each person's name followed by the first letter of their profession enclosed in parentheses.

Return the result table ordered by person_id in descending order.

The query result format is shown in the following example.
'''


SELECT person_id, CONCAT(name, "(",substr(profession,1,1),")") as name FROM Person
Order by person_id desc


