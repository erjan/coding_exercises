
'''
Write an SQL statement to query the information of the oldest teacher who come from USA by using an inline view.
'''


SELECT * from teachers 
where age =(SELECT max(age) from teachers) and country = 'USA';
