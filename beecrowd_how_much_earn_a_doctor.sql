 
select d.name,

sum( round( (150*A.hours + (150*A.hours * w.bonus/100) ),1) )  as salary

from doctors as d inner join attendances as a
on d.id = a.id_doctor inner join work_shifts as w
on w.id = a.id_work_shift
 group by d.name
order by salary desc
