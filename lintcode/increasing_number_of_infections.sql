
'''
Write an SQL query to find the IDs of all dates with a higher number of new cases in the United States than the previous day's date.
'''


select distinct n1.id

from new_cases n1 join new_cases n2 on n1.id=n2.id+1
where n1.increased_count>n2.increased_count



select b.id from new_cases a join new_cases b 
on  datediff(b.date,a.date)=1 
where a.increased_count < b.increased_count;


select n1.id 
from new_cases n1 
join new_cases n2
on datediff(n1.date,n2.date) = 1
and n1.increased_count > n2.increased_count;

----------------------------

select t2.id from new_cases t1, new_cases t2
where t2.increased_count > t1.increased_count
    and t2.date = date_add(t1.date, interval 1 day)
