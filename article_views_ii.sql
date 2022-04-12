
'''
Write an SQL query to find all the people who viewed more than one article on the same date.

Return the result table sorted by id in ascending order.

The query result format is in the following example.
'''

#wrong solution
select viewer_id from(
select
viewer_id,
view_date,
count(article_id)over(partition by view_date ) as x

from views

group by viewer_id)oo
where x > 1


#working solution



select distinct viewer_id as id
from views
group by viewer_id, view_date
having count(distinct article_id) > 1
order by 1
