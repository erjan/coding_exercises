'''
from leetcode!

Write an SQL query to swap all 'f' and 'm' values (i.e., change all 'f' values to 'm' and vice versa) with a single 
update statement and no intermediate temp table(s).

Note that you must write a single update 
statement, DO NOT write any select statement for this problem.
'''


update salary
set sex = case when sex = 'f' then 'm'
               when sex = 'm' then 'f'
               end 
               
