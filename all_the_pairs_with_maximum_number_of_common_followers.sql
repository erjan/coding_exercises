'''

Write an SQL query to find all the pairs of users with the maximum number of common followers. In other words, if the
maximum number of common followers between any two users is maxCommon, then you have to return all pairs of users 
that have maxCommon common followers.

The result table should contain the pairs user1_id and user2_id where user1_id < user2_id.

Return the result table in any order.

The query result format is in the following example.

'''


with new as (select r1.user_id user1_id, r2.user_id user2_id, count(distinct r1.follower_id) as common
from relations r1
join relations r2
on r1.user_id <r2.user_id  and r1.follower_id = r2.follower_id
group by r1.user_id, r2.user_id)

select user1_id, user2_id
from new
where common in (select max(common) from new)


--------------------------

select user1_id, user2_id
from
(select r1.user_id as user1_id, r2.user_id as user2_id, dense_rank()over(order by count(r1.follower_id) desc) as rk
from Relations r1, Relations r2
where r1.user_id < r2.user_id and r1.follower_id = r2.follower_id 
group by r1.user_id, r2.user_id) temp
where rk = 1
