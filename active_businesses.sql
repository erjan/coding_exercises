'''
The average activity for a particular event_type is the average occurences across all companies that have this event.

An active business is a business that has more than one event_type such that their occurences is strictly greater than the average activity for that event.

Write an SQL query to find all active businesses.

Return the result table in any order.

The query result format is in the following example.
'''

select business_id                                      # Finally, select 'business_id'
from
(select event_type, avg(occurences) as ave_occurences   # First, take the average of 'occurences' group by 'event_type'
 from events as e1
 group by event_type
) as temp1
join events as e2 on temp1.event_type = e2.event_type   # Second, join Events table on 'event_type'
where e2.occurences > temp1.ave_occurences              # Third, the 'occurences' should be greater than the average of 'occurences'
group by business_id
having count(distinct temp1.event_type) > 1             # (More than one event type with 'occurences' greater than 1)

---------------------
SELECT business_id
FROM Events
WHERE
occurences > (
SELECT sum(occurences) / count(DISTINCT event_type)
FROM Events
GROUP BY event_type
)
GROUP BY business_id
HAVING count(event_type) > 1

------------------------------

WITH r2 AS(
SELECT *, CASE WHEN occurences > AVG(occurences) OVER (PARTITION BY event_type) THEN 1 ELSE 0 END AS chosen
FROM Events)
SELECT business_id
FROM r2
GROUP BY business_id
HAVING SUM(chosen) >1;
