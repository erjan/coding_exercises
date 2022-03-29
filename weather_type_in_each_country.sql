'''
Write an SQL query to find the type of weather in each country for November 2019.

The type of weather is:

Cold if the average weather_state is less than or equal 15,
Hot if the average weather_state is greater than or equal to 25, and
Warm otherwise.
Return result table in any order.

The query result format is in the following example.
'''

with h1 as(

select 

country_name, 
avg(weather_state) as weather_type, day

from
countries join weather using(country_id)
where month(day) = 11 and year(day) = 2019

group by country_name)

select country_name,

case when weather_type <=15 then 'Cold'
     when weather_type >=25 then 'Hot'
     else 'Warm' end as weather_type
     
     from h1
     
     
#another

select country_name,
weather_type = case when AVG(weather_state*1.0)<=15.0 then 'Cold'
					when AVG(weather_state*1.0)>=25.0 then 'Hot'
					else 'Warm'
			   end
from Countries c inner join Weather  w
on c.country_id  = w.country_id
where [day] between '2019-11-01' and '2019-11-30'
group by country_name
