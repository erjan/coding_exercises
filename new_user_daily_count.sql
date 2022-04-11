'''
Write an SQL query to reports for every date within at most 90 days from today, the number of users that logged in for the first time on that date. Assume today is 2019-06-30.

Return the result table in any order.

The query result format is in the following example.
'''


select login_date, count(user_id) as user_count
from
(select user_id, min(activity_date) as login_date
from Traffic
where activity = 'login'
group by user_id) t
where datediff('2019-06-30', login_date) <= 90
group by login_date

-----------

select login_date, count(1) user_count
from
(select user_id, min(activity_date) login_date
from traffic
where activity = 'login'
group by user_id) a
where login_date between date_add('2019-06-30', interval -90 day) and '2019-06-30'
group by login_date



Group data by user_id where activity is 'login', and extract the earliest date, put the result in a temporary table t;
Group table t by mindate such that it's within at most 90 days from today, then count the number of users.
MySQL solution



select login_date, count(user_id) as user_count
from
(select user_id, min(activity_date) as login_date
from Traffic
where activity = 'login'
group by user_id) t
where datediff('2019-06-30', login_date) <= 90
group by login_date

---------------------------------




with earliest_login_users as (
select 
user_id, min(activity_date) as login_date
from traffic where activity = 'login'
group by user_id)


select login_date, count(user_id) as user_count 
from earliest_login_users
where datediff('2019-06-30', login_date) <=90
group by login_date
