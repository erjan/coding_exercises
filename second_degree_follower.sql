'''

A second-degree follower is a user who:

follows at least one user, and
is followed by at least one user.
Write an SQL query to report the second-degree users and the number of their followers.

Return the result table ordered by follower in alphabetical order.

The query result format is in the following example.

'''

SELECT followee AS follower, COUNT(DISTINCT follower) AS num FROM follow 
WHERE followee IN (SELECT follower FROM follow)
GROUP BY followee


--------------------------------------------------------
select f1.follower, count(distinct f2.follower) as num
from follow f1
join follow f2 on f1.follower = f2.followee
group by f1.follower
order by f1.follower;


--------------------
select f1.follower, 
count(distinct f2.follower) as num 
FROM follow f1 JOIN follow f2 ON f1.follower = f2.followee 
GROUP BY f1.follower

