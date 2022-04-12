'''
A friendship between a pair of friends x and y is strong if x and y have at least three common friends.

Write an SQL query to find all the strong friendships.

Note that the result table should not contain duplicates with user1_id < user2_id.

Return the result table in any order.

The query result format is in the following example.

 
 '''


with allfriends as (
    select user1_id as user, user2_id as friend
    from Friendship
    UNION ALL
    select user2_id as user, user1_id as friend
    from Friendship)
    
select a.user as user1_id, b.user as user2_id, count(*) as common_friend
from allfriends a
join allfriends b
where a.user < b.user AND a.friend = b.friend and (a.user, b.user) in (select user, friend from allfriends)
group by 1, 2
having common_friend >=3

---------------------------

with all_friends as (
    select 
        user1_id as user_id, 
        user2_id as friend 
    from friendship
        UNION
    select 
        user2_id as user_id, 
        user1_id as friend 
    from friendship
)

select * from 
(
    select 
        a.user_id as user1_id, 
        b.user_id as user2_id, 
        count(distinct a.friend) as common_friend
    from 
        all_friends a 
    join 
        all_friends b
    on 
        a.user_id != b.user_id 
        and a.friend = b.friend
    where 
        (a.user_id, b.user_id) in 
            (select user1_id, user2_id from friendship)
    group by 
        a.user_id, b.user_id 
    having 
        count(distinct a.friend) >= 3  
) tb1


---------------------
WITH Cte AS (
    SELECT user1_id, user2_id FROM Friendship 
    UNION
    SELECT user2_id AS user1_id, user1_id AS user2_id FROM Friendship
)
SELECT a.user1_id AS user1_id, b.user2_id AS user2_id, COUNT(*) AS common_friend
FROM 
    Cte a 
    JOIN Cte b ON a.user2_id = b.user1_id AND a.user1_id < b.user2_id
    JOIN Friendship c ON a.user1_id = c.user1_id AND b.user2_id = c.user2_id
GROUP BY 1, 2
HAVING COUNT(*) >= 3
