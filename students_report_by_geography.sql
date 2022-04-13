

'''

A school has students from Asia, Europe, and America.

Write an SQL query to pivot the continent column in the Student table so that each name is sorted alphabetically and displayed underneath its corresponding continent. The output headers should be America, Asia, and Europe, respectively.

The test cases are generated so that the student number from America is not less than either Asia or Europe.

The query result format is in the following example.

 
 
 '''


select min(America) as America, min(Asia) as Asia, min(Europe) as Europe from
(select
case when continent= "America" then name else null end as "America",
case when continent = "Asia" then name else null end as "Asia",
case when continent = "Europe" then name end as "Europe",
row_number() over (partition by continent order by name) as rnk
from student
) t1
group by rnk
