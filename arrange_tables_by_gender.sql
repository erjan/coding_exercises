'''
Write an SQL query to rearrange the Genders table such that the rows alternate between 'female', 'other', and 'male' in order. The table should be rearranged such that the IDs of each gender are sorted in ascending order.

Return the result table in the mentioned order.

The query result format is shown in the following example.
'''

select user_id, gender
from (
select user_id, gender, row_number() over (partition by gender order by user_id asc) rnk,
case when gender = "female" then 1
when gender = "male" then 3
else 2 end ord
from genders) a
order by rnk, ord asc
