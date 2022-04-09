'''

Write an SQL query to report all possible axis-aligned rectangles with a non-zero area that can be formed by any two points from the Points table.

Each row in the result should contain three columns (p1, p2, area) where:

p1 and p2 are the id's of the two points that determine the opposite corners of a rectangle.
area is the area of the rectangle and must be non-zero.
Return the result table ordered by area in descending order. If there is a tie, order them by p1 in ascending order. If there is still a tie, order them by p2 in ascending order.

The query result format is in the following table.

'''


SELECT  pt1.id as P1, pt2.id as P2,
		ABS(pt2.x_value - pt1.x_value)*ABS(pt2.y_value-pt1.y_value) as AREA
FROM Points pt1 JOIN Points pt2 
ON pt1.id<pt2.id
AND pt1.x_value!=pt2.x_value 
AND pt2.y_value!=pt1.y_value
ORDER BY AREA DESC, p1 ASC, p2 ASC;


----------------


SELECT t1.id p1, t2.id p2, ABS(t1.x_value-t2.x_value)*ABS(t1.y_value-t2.y_value) area
FROM Points t1, Points t2
WHERE t1.id <> t2.id AND t1.x_value <> t2.x_value AND t1.y_value <> t2.y_value AND t1.id < t2.id
ORDER BY 3 DESC, p1, p2
