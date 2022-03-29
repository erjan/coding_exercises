'''
Write an SQL query to find the number of comments per post. The result table should contain post_id and its corresponding number_of_comments.

The Submissions table may contain duplicate comments. You should count the number of unique comments per post.

The Submissions table may contain duplicate posts. You should treat them as one post.

The result table should be ordered by post_id in ascending order.

The query result format is in the following example.
'''

SELECT s.sub_id AS post_id,

(SELECT COUNT(DISTINCT(s1.sub_id)) 
 
 FROM Submissions s1 WHERE s1.parent_id = s.sub_id)
 
AS number_of_comments
FROM Submissions s
WHERE s.parent_id IS null
GROUP BY s.sub_id
