'''

Write an SQL query to report the IDs of the users that made any two purchases at most 7 days apart.

Return the result table ordered by user_id.

The query result format is in the following example.

'''


select  distinct user_id
from
( select user_id, purchase_date,
lag(purchase_date) over (partition by user_id order by purchase_date) prev_purchase_date
from purchases) t
where datediff(purchase_date, prev_purchase_date) <=7



#self join

select distinct p1.user_id
from purchases p1
inner join
purchases p2
on p1.user_id=p2.user_id and p1.purchase_id<>p2.purchase_id
and abs(datediff(p1.purchase_date, p2.purchase_date))<=7
order by p1.user_id
