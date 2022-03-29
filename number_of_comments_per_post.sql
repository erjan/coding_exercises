'''
Write an SQL query to find the number of comments per post. The result table should contain post_id and its corresponding number_of_comments.

The Submissions table may contain duplicate comments. You should count the number of unique comments per post.

The Submissions table may contain duplicate posts. You should treat them as one post.

The result table should be ordered by post_id in ascending order.

The query result format is in the following example.
'''



SELECT
    DISTINCT sub_id AS post_id,
    (SELECT COUNT(DISTINCT sub_id) FROM Submissions S2 WHERE S1.sub_id = S2.parent_id) AS number_of_comments
FROM
    Submissions AS S1
WHERE parent_id IS NULL
ORDER BY sub_id
