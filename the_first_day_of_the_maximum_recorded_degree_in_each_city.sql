'''
Write an SQL query to report the day that has the maximum recorded degree in each city. If the maximum degree 
was recorded for the same city multiple times, return the earliest day among them.

Return the result table ordered by city_id in ascending order.

The query result format is shown in the following example.
'''


select city_id, day, degree from(

select city_id, day, degree,
rank()over(partition by city_id order by degree desc,day asc) as rnk
 from  weather)k
 where rnk = 1
 order by city_id 
