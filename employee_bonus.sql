'''
Write an SQL query to report the name and bonus amount of each employee with a bonus less than 1000.

Return the result table in any order.

The query result format is in the following example.

'''


select name, bonus from employee 
left outer join bonus on employee.empId = bonus.empId

where bonus.bonus < 1000  or bonus is null
