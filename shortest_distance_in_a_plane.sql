
'''

The distance between two points p1(x1, y1) and p2(x2, y2) is sqrt((x2 - x1)2 + (y2 - y1)2).

Write an SQL query to report the shortest distance between any two points from the Point2D table. Round the distance to two decimal points.

The query result format is in the following example.

'''
select


round(sqrt(power((p2.x - p1.x),2) + power((p2.y - p1.y),2) ),2) as shortest

from point2d p1 cross join point2d p2
where p1.x != p2.x or p2.y != p1.y
 order by shortest asc limit 1
