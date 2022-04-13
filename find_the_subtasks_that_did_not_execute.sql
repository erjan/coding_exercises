'''
Write an SQL query to report the IDs of the missing subtasks for each task_id.

Return the result table in any order.

The query result format is in the following example.
'''

WITH RECURSIVE CTE AS (
    SELECT task_id, subtasks_count
    FROM Tasks
    UNION ALL
    SELECT task_id, subtasks_count - 1
    FROM CTE
    WHERE subtasks_count > 1
)

SELECT task_id, subtasks_count AS subtask_id
FROM CTE 
WHERE (task_id, subtasks_count) NOT IN (SELECT * FROM Executed)



----------------------------
/*

write based on subtask_count for each task write those many rows
for each task id
2.1st table except 2nd table
*/
with cte as
(

select task_id, 1 as n
from tasks
union all
select t.task_id, n+1
from tasks t join
cte c on t.task_id = c.task_id
where n< t.subtasks_count
)

select task_id,n as subtask_id
from cte
except
select task_id , subtask_id
from Executed
