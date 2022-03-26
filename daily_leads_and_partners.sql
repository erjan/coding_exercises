'''
Write an SQL query that will, for each date_id and make_name, return the number of distinct lead_id's and distinct partner_id's.

Return the result table in any order.

The query result format is in the following example.
'''

select date_id, make_name, count(distinct lead_id) as unique_leads, 
count(distinct partner_id) as unique_partners

from dailysales

group by date_id, make_name
