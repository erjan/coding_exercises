'''

Write an SQL query to find the average daily percentage of posts that got removed after being reported as spam, rounded to 2 decimal places.

The query result format is in the following example.

'''

select round(sum(percent)/count(distinct action_date),2) as average_daily_percent
from
    (select a.action_date,
    count(distinct r.post_id)/count(distinct a.post_id)*100 as percent
    from actions a left join removals r
    on a.post_id = r.post_id
    where a.extra='spam'
    group by 1) temp;
    
    
-------------------

SELECT ROUND(100*AVG(rate), 2) average_daily_percent
FROM 
(SELECT a.action_date, SUM(a.action_date <= r.remove_date AND a.post_id = r.post_id)/COUNT(DISTINCT a.post_id) rate
FROM (SELECT DISTINCT post_id, action_date, extra FROM Actions) a, Removals r
WHERE a.extra = 'spam' 
GROUP BY 1) t1 
