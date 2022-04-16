'''
Please write a SQL statement to query the teachers table to filter for countries where the average age of teachers in that country is greater than the average age of teachers in all countries, and query for information about teachers in those countries.
'''


select * from teachers where country in (

select country
from teachers
group by country
having avg(age) > ( select avg(age) as total_avg from teachers))


-----------------------

select t1.* from teachers t1 
left join(
select country , avg(age) as avg_age from teachers
group by country ) t2 on t1.country = t2.country 
where avg_age > (select avg(age) from teachers)
