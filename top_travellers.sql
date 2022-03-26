'''
Write an SQL query to report the distance traveled by each user.

Return the result table ordered by travelled_distance in descending order, if two or more users traveled the same distance, order them by their name in ascending order.

The query result format is in the following example.
'''


select 
	name,
	sum(if(distance is not null, distance, 0)) as travelled_distance
from users u 
left join rides r 
	on u.id = r.user_id 
group by name
order by 2 desc, 1 
