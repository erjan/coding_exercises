'''
Write an SQL query to find the IDs of the invalid tweets. The tweet is invalid 
if the number of characters used in the content of the tweet is strictly greater than 15.

Return the result table in any order.

The query result format is in the following example.
'''

select tweet_id from tweets

where length(content) >15
