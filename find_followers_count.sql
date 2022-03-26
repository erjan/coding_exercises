'''
Write an SQL query that will, for each user, return the number of followers.

Return the result table ordered by user_id.

The query result format is in the following example.
'''



select user_id, count(distinct follower_id) as followers_count from followers

group by user_id
