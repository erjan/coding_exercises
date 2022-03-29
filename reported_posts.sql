'''
Write an SQL query that reports the number of posts reported yesterday for each report reason. Assume today is 2019-07-05.

Return the result table in any order.

The query result format is in the following example.
'''


select extra as report_reason, count(distinct post_id) as report_count

from actions
where action = 'report' and action_date = date_add('2019-07-05',interval -1 day)
group by extra
