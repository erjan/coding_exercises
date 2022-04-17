'''
There are some boxes marked with ID in one place, some of 
which are filled with things and some of which are free.
Please write SQL statements, find empty and consecutive boxes, and 
return them in ascending order of id.
'''

select distinct a.id
from  boxes a,
       boxes b
where abs(a.id-b.id)=1
and (a.is_empty=1 and b.is_empty=1)
order by a.id asc



-----------------------------------------

select id from boxes where id in (
    select b1.id from boxes b1,boxes b2
    where (b1.is_empty = 1 and b2.is_empty=1 and ( 
         b1.id + 1= b2.id or b2.id +1 = b1.id
      )
    ) 
) order by id
