'''

The confirmation rate of a user is the number of 'confirmed' messages divided by the total number of requested confirmation messages. The confirmation rate of a user that did not request any confirmation messages is 0. Round the confirmation rate to two decimal places.

Write an SQL query to find the confirmation rate of each user.

Return the result table in any order.

The query result format is in the following example.

'''

select
user_id,
round(
    sum(case when action = 'confirmed' then 1 else 0 end)/ count(*)
    
    
    ,2) as confirmation_rate

from signups left join confirmations using(user_id)
group by user_id


---------------------------

SELECT 
  s.user_id,
  ROUND(AVG(CASE WHEN action = 'confirmed' THEN 1.00 ELSE 0.00 END),2) AS confirmation_rate
FROM Signups s LEFT JOIN Confirmations c ON s.user_id = c.user_id
GROUP BY s.user_id
