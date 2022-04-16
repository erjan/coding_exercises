
'''
Write an SQL statement to find the height of a player in the players 
table that has at least three players with consecutive ids 
reaching this height, and return the results in any order.
'''

with help as(

select 

id, height, 
-- lead(id,1)over() as next_id,
lead(height,1)over() as next2,
lead(height,2)over() as next3

from players)


select height from(
select  
case when height = next3 and next2 = next3 then height end as height
from help)k where height is not null

------------------

select a.height
from players as a, players as b,players as c
where b.id= a.id +1
and c.id = b.id + 1
and (a.height = b.height and b.height= c.height)
--------------------------
select distinct height from (select height,id-rn as subs ,count(1) as num  from 
(select *,row_number() over(partition by height order by id) rn from players
)m 
 group by height,id-rn 
) n where num>=3


----------------------------------

select p2.height  
from players p1,players p2,players p3
where p1.height = p2.height and p1.height = p3.height
and p2.id > p1.id and p2.id-p1.id = 1
and p2.id < p3.id and p3.id-p2.id = 1
