'''
Write an SQL query to recommend friends to Leetcodify users. We recommend user x to user y if:

Users x and y are not friends, and
Users x and y listened to the same three or more different songs on the same day.
Note that friend recommendations are unidirectional, meaning if user x and user y should be recommended to each other, the result table should have both user x recommended to user y and user y recommended to user x. Also, note that the result table should not contain duplicates (i.e., user y should not be recommended to user x multiple times.).

Return the result table in any order.

The query result format is in the following example.
'''

with c as (
    select l1.user_id as uid1, l2.user_id as uid2, count(distinct l1.song_id) as ct
    from listens l1
    join listens l2
    on l1.song_id=l2.song_id and l1.day=l2.day and l1.user_id<>l2.user_id  # make sure l1.user_id != l2.user_id, we don't wanna join on user_id itself
    group by l1.user_id, l2.user_id, l1.day
    having ct>=3  # make sure the number of different songs on each day >=3
), f (uid1, uid2) as (
    select user1_id, user2_id from friendship
    union
    select user2_id, user1_id from friendship
)
select uid1 as user_id, uid2 as recommended_id
from c
where (uid1, uid2) not in (select uid1, uid2 from f)
group by uid1, uid2;
Explanations
Step I - calculate number of different songs for each (user1_id, user2_id) pair on each day.
This part is done by CTE c. The following is the result of CTE c using the initial test case.
user1_id   user2_id   ct(num_different_songs)      day
	1          2                3               2021-03-15
	1          3                3               2021-03-15
	2          1                3               2021-03-15
	2          3                3               2021-03-15
	3          1                3               2021-03-15
	3          2                3               2021-03-15
Step II - collect bidirectional (user1_id, user2_id) friend pair from Friendship table
This is part is done by CTE f. The following is the result of CTE f.
user1_id   user2_id
	1          2
	2          1
Step III - select all distinct (user1_id, user2_id) pair from CTE c AND remove all possible friend pairs from CTE f
This part is done in the main SELECT. The following is the final result.
user_id   recommended_id
   1           3
   2           3
   3           1
   3           2
Remember that user x and user y are not friend.
==> Remove both (x, y) and (y, x)
Remember that duplicates are not allowed, i.e. user y should not be recommended to user x multiple times.
==> I used GROUP BY uid1, uid2. Or, you can use SELECT DISTINCT uid1 AS user_id, uid2 AS recommended_id


---------------------------------
WITH
allRecs AS (
SELECT DISTINCT
  l1.user_id AS user1_id,
  l2.user_id AS user2_id
FROM Listens l1 INNER JOIN Listens l2 ON l1.song_id = l2.song_id AND l1.day=l2.day AND l1.user_id < l2.user_id
WHERE NOT EXISTS(SELECT * FROM Friendship f WHERE l1.user_id = f.user1_id AND l2.user_id = f.user2_id)
GROUP BY l1.user_id, l2.user_id, l1.day
HAVING COUNT(DISTINCT l1.song_id) >= 3
) 
SELECT user1_id AS user_id,
       user2_id AS recommended_id
FROM allRecs
UNION
SELECT user2_id AS user_id,
       user1_id AS recommended_id
FROM allRecs
