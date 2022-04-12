'''
Write an SQL query to recommend pages to the user with user_id = 1 using the pages that your friends liked. It should not recommend pages you already liked.

Return result table in any order without duplicates.

The query result format is in the following example.

 
 '''
 
 select distinct page_id as recommended_page
from
(select
case
when user1_id=1 then user2_id
when user2_id=1 then user1_id
end as user_id
from Friendship) a
join Likes
on a.user_id=Likes.user_id
where page_id not in (select page_id from Likes where user_id=1)


-----------------
# FIRST FIND ALL FRIENDS FOR user1_id = 1
WITH ALL_FRIENDS_TABLE AS(
                            SELECT user2_id 
                            FROM Friendship 
                            WHERE user1_id  = 1
                            UNION
                            SELECT user1_id 
                            FROM Friendship 
                            WHERE user2_id  = 1
                           )
## THEN FIND ALL DISTINCT PAGES THESE FRIEDS HAVE LIKED
SELECT DISTINCT(page_id) AS recommended_page 
FROM Likes
WHERE user_id IN (SELECT * FROM ALL_FRIENDS_TABLE)  
### AND FINALY EXCLUDE PAGES user1_id = 1 HAS LIKED
AND page_id NOT IN (SELECT page_id FROM Likes WHERE user_id = 1)

--------------

select distinct page_id as recommended_page
from likes
where user_id in (select case when user1_id = 1 then user2_id
                              when user2_id = 1 then user1_id
                         end as user_id
                  from friendship
                  where user1_id = 1 or user2_id = 1)
  and page_id not in (select page_id from likes where user_id = 1);
  
  
  
  ------------------
  SELECT DISTINCT page_id AS recommended_page
FROM Likes
WHERE user_id IN (
    SELECT user2_id AS friend_id FROM Friendship WHERE user1_id = 1
    UNION
    SELECT user1_id AS friend_id FROM Friendship WHERE user2_id = 1) AND
    page_id NOT IN (
      SELECT page_id FROM Likes WHERE user_id = 1
    )
