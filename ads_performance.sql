'''
A company is running Ads and wants to calculate the performance of each Ad.

Performance of the Ad is measured using Click-Through Rate (CTR) where:


Write an SQL query to find the ctr of each Ad. Round ctr to two decimal points.

Return the result table ordered by ctr in descending order and by ad_id in ascending order in case of a tie.

The query result format is in the following example.
'''

SELECT 

ad_id, 

IFNULL(ROUND(AVG(CASE WHEN action = 'Clicked' THEN 1
                         WHEN action = 'Viewed' THEN 0
                         ELSE NULL END)*100,2),0) AS ctr
FROM Ads
GROUP BY ad_id
ORDER BY ctr DESC, ad_id



#another

select ad_id, 
ifnull(round(sum(case when action = 'Clicked' then 1 else 0 end) / sum(case when action = 'Clicked' or action = 'Viewed' then 1 else 0 end) * 100, 2), 0) as ctr
from Ads
group by ad_id
order by ctr desc, ad_id asc
