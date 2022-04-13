'''
Leetcode has collected some posts from its social media website and is interested in finding the topics of each post. Each topic can be expressed by one or more keywords. If a keyword of a certain topic exists in the content of a post (case insensitive) then the post has this topic.

Write an SQL query to find the topics of each post according to the following rules:

If the post does not have keywords from any topic, its topic should be "Ambiguous!".
If the post has at least one keyword of any topic, its topic should be a string of the IDs of its topics sorted in ascending order and separated by commas ','. The string should not contain duplicate IDs.
Return the result table in any order.

The query result format is in the following example.
'''


SELECT post_id, 
IFNULL(GROUP_CONCAT(DISTINCT topic_id),"Ambiguous!") AS topic
FROM posts a
LEFT JOIN keywords b
ON CONCAT(' ',lower(a.content),' ') LIKE CONCAT('% ',lower(b.word),' %')
GROUP BY post_id
ORDER BY post_id
