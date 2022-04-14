'''
Write an SQL query to report the similar friends of Leetcodify users. A user x and user y are similar friends if:

Users x and y are friends, and
Users x and y listened to the same three or more different songs on the same day.
Return the result table in any order. Note that you must return the similar pairs of friends the same way they were represented in the input (i.e., always user1_id < user2_id).

The query result format is in the following example.

 
 '''
 
 The idea is to

find distinct combos of (user1, user2, day)
make sure they are also in the Friendship table (existing friendship)
filter to make sure that there are over 3 songs in overlap
Below is the code.

SELECT DISTINCT a.user_id AS user1_id, b.user_id AS user2_id # 1) Find distinct combos
FROM Listens a, Listens b
WHERE a.day = b.day
	AND a.song_id = b.song_id
	AND a.user_id != b.user_id
	AND (a.user_id, b.user_id) IN (SELECT * FROM Friendship) # 2) They are also in Friendship table
	
GROUP BY a.user_id, b.user_id, b.day
HAVING COUNT(DISTINCT a.song_id) >= 3 # 3) There are >= 3 overlaps

-----------------------
SELECT DISTINCT l1.user_id AS user1_id, l2.user_id AS user2_id
FROM Listens l1
JOIN Listens l2
ON l1.song_id = l2.song_id
AND l1.day = l2.day
AND l1.user_id < l2.user_id
AND (l1.user_id, l2.user_id) IN (SELECT * FROM Friendship)
GROUP BY l1.user_id, l2.user_id, l1.day
HAVING COUNT(DISTINCT l1.song_id) >= 3

-----------------------------------------------

select distinct user1_id, user2_id
from Listens L1
join Friendship F
on L1.user_id = F.user1_id
join Listens L2
on F.user2_id = L2.user_id and L1.song_id = L2.song_id and L1.day = L2.day
group by user1_id, user2_id, L1.day
having count(distinct L1.song_id)>=3
