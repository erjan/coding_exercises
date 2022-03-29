'''
Write an SQL query that reports the average experience years of all the employees for each project, rounded to 2 digits.

Return the result table in any order.

The query result format is in the following example.
'''

select project_id,

round(avg(experience_years),2) as average_years 


from project join employee using(employee_id)


group by project_id
