'''
Write an SQL query to count the number of apples and oranges in all the boxes. If a box contains a chest, you should also include the number of apples and oranges it has.

The query result format is in the following example.
'''


select 

sum(boxes.apple_count) + IFNULL(SUM(chests.apple_count), 0) as apple_count ,

sum(boxes.orange_count)+ IFNULL(SUM(chests.orange_count), 0)
as orange_count 



from boxes
left join chests using(chest_id)



------------------------------------------

SELECT SUM(b.apple_count + IFNULL(c.apple_count,0)) AS apple_count,SUM(b.orange_count + IFNULL(c.orange_count,0)) AS orange_count
FROM Boxes AS b
LEFT JOIN Chests AS c
USING(chest_id)
