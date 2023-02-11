'''
In a company, each employee must work a certain number of hours every month. Employees work in sessions. The number of hours an employee worked can be calculated from the sum of the number of minutes the employee worked in all of their sessions. The number of minutes in each session is rounded up.

For example, if the employee worked for 51 minutes and 2 seconds in a session, we consider it 52 minutes.
Write an SQL query to report the IDs of the employees that will be deducted. In other words, report the IDs of the employees that did not work the needed hours.

Return the result table in any order.

The query result format is in the following example.
'''



select e.employee_id,e.needed_hours,

sum(ceil(ifnull(TIMESTAMPDIFF(SECOND, L.in_time, L.out_time),0))/60/60)  as diff

 from employees e left join logs l on e.employee_id = l.employee_id
group by e.employee_id

having sum(ceil(ifnull(TIMESTAMPDIFF(SECOND, L.in_time, L.out_time),0))/60/60) <e.needed_hours

-----------------------------------------------------------------------------------------------------------

select e.employee_id


 from employees e 
 left join logs l on e.employee_id = l.employee_id
group by e.employee_id,e.needed_hours

HAVING
  (SUM(CEIL(IFNULL(TIMESTAMPDIFF(SECOND, l.in_time, l.out_time),0) / 60)) / 60) < 
  e.needed_hours;
