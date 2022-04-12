'''
A telecommunications company wants to invest in new countries. The company intends to invest in the countries where the average call duration of the calls in this country is strictly greater than the global average call duration.

Write an SQL query to find the countries where this company can invest.

Return the result table in any order.

The query result format is in the following example.
'''

#from comments
# p.id IN (c.caller_id, c.callee_id) is equal to calls.caller_id = person.id OR calls.callee_id = person.id


SELECT
 co.name AS country
FROM
 person p
 JOIN
     country co
     ON SUBSTRING(phone_number,1,3) = country_code
 JOIN
     calls c
     ON p.id IN (c.caller_id, c.callee_id)
GROUP BY
 co.name
HAVING
 AVG(duration) > (SELECT AVG(duration) FROM calls)
 
 
 --------------------
 
 select distinct country 
from(
    select c.name country, ca.duration
        ,avg(ca.duration) over(partition by c.name) avg_duration
        ,avg(ca.duration) over() avg_total
    from calls ca left join person p on (ca.caller_id = p.id) or (ca.callee_id = p.id)
    inner join country c on substring(p.phone_number,1,3) = c.country_code
) a
where avg_duration > avg_total

----------------------------

SELECT
 co.name AS country
FROM person p 
INNER JOIN country co
     ON LEFT(phone_number,3) = country_code
     
 INNER JOIN calls c
     ON p.id = c.caller_id
     OR p.id = c.callee_id
GROUP BY
 co.name
HAVING
 AVG(duration) > (SELECT AVG(duration) FROM calls)
