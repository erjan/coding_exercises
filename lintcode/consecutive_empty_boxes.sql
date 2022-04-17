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
