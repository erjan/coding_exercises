'''
Active users are those who logged in to their accounts for five or more consecutive days.

Write an SQL query to find the id and the name of active users.

Return the result table ordered by id.

The query result format is in the following example.
'''

select distinct l1.id, ac.name from logins l1 join logins l2 on l1.id = l2.id
and DATEDIFF(l2.login_date, l1.login_date) BETWEEN 1 AND 4
join accounts ac on l1.id = ac.id
group by l1.id,l1.login_date
having COUNT(DISTINCT l2.login_date) = 4



select id, name from accounts where id in
(select distinct l1.id from logins l1 join logins l2 on l1.id = l2.id
and DATEDIFF(l2.login_date, l1.login_date) BETWEEN 1 AND 4
group by l1.id,l1.login_date
having COUNT(DISTINCT l2.login_date) = 4)
order by id


With cte as (select id,
case when count(id) over(partition by id order by login_date asc range interval 4 day preceding ) >=5 then 1 else 0 end as ll
fromLogins
group by id,login_date)

select id , name from accounts
where id in (select distinct id from cte where ll=1)
order by id;



select distinct a.id, b.name
from 
 (select id from 
             (select id, login_date as day0, lead(login_date, 1) over (partition by id order by login_date) as day1, 
                                             lead(login_date, 2) over (partition by id order by login_date) as day2,
                                             lead(login_date, 3) over (partition by id order by login_date) as day3, 
                                             lead(login_date, 4) over (partition by id order by login_date) as day4  
              from (select distinct id, login_date from logins)p )
			  where datediff(day1, day0)=1 and 
                    datediff(day2, day1)=1 and   
                    datediff(day3, day2)=1 and 
                    datediff(day4, day3)=1 ) a 
 left join accounts b 
 on a.id=b.id
