'''
You are implementing a page recommendation system for a social media website. Your system will 
recommended a page to user_id if the page is liked by at least one friend of user_id and is not liked by user_id.

Write an SQL query to find all the possible page recommendations for every user. Each recommendation 
should appear as a row in the result table with these columns:

user_id: The ID of the user that your system is making the recommendation to.
page_id: The ID of the page that will be recommended to user_id.
friends_likes: The number of the friends of user_id that like page_id.
Return result table in any order.

The query result format is in the following example.
'''


# Write your MySQL query statement below
SELECT user1_id as user_id,page_id,COUNT(user_id) as friends_likes
FROM
(
    SELECT a.user1_id,b.user_id,b.page_id # user, all user friends, page_id
    FROM Friendship as a
    JOIN Likes as b
    ON a.user2_id=b.user_id
    UNION SELECT a.user2_id,b.user_id,b.page_id
    FROM Friendship as a
    JOIN Likes as b
    ON a.user1_id=b.user_id
) a
WHERE CONCAT(user1_id,",",page_id) NOT IN
(SELECT CONCAT(user_id,",",page_id) FROM Likes)
GROUP BY user1_id,page_id;

----------------------------------------------

with t1 as (
    select user1_id as user_id, user2_id as friend_id from friendship
    union
    select user2_id as user_id, user1_id as friend_id from friendship)
    
-- then, join table
select t1.user_id, l.page_id, count(distinct t1.friend_id) as friends_likes
from t1
left join likes as l
on t1.friend_id=l.user_id

-- filter out pages that are already liked by the user
left join likes as l2
on t1.user_id=l2.user_id and l.page_id=l2.page_id
where l2.page_id is null

-- get the final output
group by t1.user_id, l.page_id


------------------------------------

SELECT f.user1_id as user_id,
l.page_id,
COUNT(DISTINCT user2_id) as friends_likes
FROM (
    SELECT user1_id, user2_id FROM Friendship 
    UNION ALL
    SELECT user2_id, user1_id FROM Friendship
     ) f
JOIN Likes l
ON f.user2_id = l.user_id
LEFT JOIN Likes l2
ON f.user1_id = l2.user_id
AND l.page_id = l2.page_id
WHERE l2.page_id is Null
GROUP BY 1,2
ORDER BY 1,3 desc
