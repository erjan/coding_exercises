'''
Write an SQL query to report the IDs of the low-quality problems. A LeetCode problem is low-quality if the like percentage of the problem (number of likes divided by the total number of votes) is strictly less than 60%.

Return the result table ordered by problem_id in ascending order.

The query result format is in the following example.
'''

select problem_id from (

select  problem_id, likes/(likes + dislikes)*100 as ratio

from problems 
order by ratio asc)k

where k.ratio < 60
order by problem_id 


#another

select problem_id 
from problems 
where likes/(likes+dislikes) < 0.6
order by problem_id
