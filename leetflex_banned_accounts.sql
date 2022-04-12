
'''
Write an SQL query to find the account_id of the accounts that should be banned from Leetflex. An account should be banned if it was logged in at some moment from two different IP addresses.

Return the result table in any order.

The query result format is in the following example.

 
 '''


select distinct a.account_id
from LogInfo a join LogInfo b
on a.account_id = b.account_id and a.ip_address ! = b.ip_address 
and ((a.logout between b.login and b.logout) or (b.logout between a.login and a.logout))


select account_id
from loginfo a
where exists (select 1 from loginfo 
              where a.account_id = account_id 
              and a.login between login and logout and a.ip_address != ip_address) 
group by account_id

-------------------
WITH CTE AS (
            SELECT *,
                    LEAD(ip_address) OVER(PARTITION BY account_id ORDER BY login) AS NEXT_IP,
                    LEAD(login) OVER(PARTITION BY account_id ORDER BY login) NEXT_LOGIN
            FROM LogInfo 
            )
SELECT DISTINCT account_id  
FROM CTE
WHERE NEXT_LOGIN <= logout AND ip_address != NEXT_IP


------------
select
distinct a.account_id
from LogInfo a, LogInfo b
where a.login between (b.login) and (b.logout)
and a.account_id = b.account_id
and a.ip_address !=b.ip_address
