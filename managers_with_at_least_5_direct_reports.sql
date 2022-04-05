'''

Write an SQL query to report the managers with at least five direct reports.

Return the result table in any order.

The query result format is in the following example.

'''

select name from (

select e1.id, e1.name from employee e1 join employee e2
on e1.id = e2.managerId

group by e1.id, e1.name
having count(e1.id) >=5)k


#another

select name from employee 
where id in 
(select managerId from Employee
group by managerId
having count(managerId)>=5) 
