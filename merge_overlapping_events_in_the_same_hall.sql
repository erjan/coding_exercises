'''
Write an SQL query to merge all the overlapping events that are held in the same hall. Two events overlap if they have at least one day in common.

Return the result table in any order.

The query result format is in the following example.
'''



'''
Intuition
For each event hall, an event belongs to an onging series of events if its start_day <= max_prev_end_day of all preceding events (events starts earlier than this event).

For each event hall, we need to sequentially iterate events holded in this hall by their start_day in an ascending order and keep tracking of the max(end_day). For each event we:

test if it begins a new series of event start_day > max_prev_end_day
update the max_prev_end_day = max(max_prev_end_day, end_day)
Approach
We can do this with user defined variables (incoveniently it has been deprecated since MySQL 8.0), or with the window expression along with common table expression (CTE).
'''

WITH new_event_start AS (
  SELECT
  	IFNULL(start_day > MAX(end_day) OVER pw, 1) AS is_new_event_start,
  	hall_id,
    start_day,
  	end_day
  FROM
  	HallEvents
  WINDOW
  	pw AS (
      PARTITION BY hall_id 
      ORDER BY start_day ASC, end_day DESC
      ROWS BETWEEN UNBOUNDED PRECEDING AND 1 PRECEDING
    )
),
event_id AS (
  SELECT
  	SUM(is_new_event_start) OVER w AS event_id,
    hall_id,
    start_day,
    end_day
  FROM
  	new_event_start
  WINDOW
  	w AS (
      PARTITION BY hall_id
      ORDER BY start_day ASC, end_day DESC
    )
)
SELECT
	hall_id,
    min(start_day) AS start_day,
    max(end_day) As end_day    
FROM
	event_id
GROUP BY hall_id, event_id
  
