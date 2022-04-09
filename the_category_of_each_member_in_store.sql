'''

A store wants to categorize its members. There are three tiers:

"Diamond": if the conversion rate is greater than or equal to 80.
"Gold": if the conversion rate is greater than or equal to 50 and less than 80.
"Silver": if the conversion rate is less than 50.
"Bronze": if the member never visited the store.
The conversion rate of a member is (100 * total number of purchases for the member) / total number of visits for the member.

Write an SQL query to report the id, the name, and the category of each member.

Return the result table in any order.

The query result format is in the following example.

 
 
 '''


with s as(
select 

members.member_id, name,

100 * IFNULL(COUNT(DISTINCT purchases.visit_id),0) / count(visits.visit_id) as rate

from members left join visits on members.member_id = visits.member_id
left join purchases on visits.visit_id = purchases.visit_id


group by member_id)


select member_id, name,

case when rate >=80 then 'Diamond'
    when rate >=50 and rate < 80 then 'Gold'
    when rate < 50 then 'Silver'
    else 'Bronze' end as category

from s

-----------------------------------------------

select m.member_id, m.name,
CASE
WHEN count(v.visit_date) = 0 THEN "Bronze"
WHEN (100 * count(p.charged_amount)/count(v.visit_date)) >=80 THEN "Diamond"
WHEN (100 * count(p.charged_amount)/count(v.visit_date)) >=50 AND (100 * count(p.charged_amount)/count(v.visit_id)) < 80 THEN "Gold"
WHEN (100 * count(p.charged_amount)/count(v.visit_date)) <50 THEN "Silver" END AS category
from members m
left join visits v
on m.member_id = v.member_id
left join purchases p
on v.visit_id = p.visit_id
GROUP BY m.member_id, m.name
ORDER BY m.member_id;
