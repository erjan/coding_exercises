
'''
Li Hua’s job is to determine whether three line segments can form a 
right triangle
Assuming that the table line_segments saves all groups consisting of three 
line segments with lengths a, b, c, please help Li Hua write a SQL statement to determine whether each group of line segments can form a right triangle
'''

select 

id,a,b,c,

case when power(a,2) + power(b,2) = power(c,2) then 'Yes'
when power(b,2) + power(c,2) = power(a,2) then 'Yes'
when power(a,2) + power(c,2) = power(b,2) then 'Yes'

else "No" end as right_triangle
    
from line_segments




select *,if(a*a+b*b=c*c or a*a+c*c=b*b or b*b+c*c=a*a,'Yes','No')  right_triangle from line_segments;
