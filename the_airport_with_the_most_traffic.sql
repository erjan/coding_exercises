'''

Write an SQL query to report the ID of the airport with the most traffic. The airport with the most traffic is the airport that has the largest total number of flights that either departed from or arrived at the airport. If there is more than one airport with the most traffic, report them all.

Return the result table in any order.

The query result format is in the following example.

'''


select airport_id from(
    select airport_id, sum(flights_count) flights_count, rank() over (order by sum(flights_count) desc) rnk 
    from (
         select departure_airport airport_id , flights_count 
         from flights 
         union all 
         select arrival_airport , flights_count
         from flights
    )
    group by airport_id
)
where rnk = 1

-----------------------

WITH CTE AS (
  SELECT airport_id, RANK() OVER(ORDER BY SUM(flights_count) DESC) AS RN
  FROM ( SELECT departure_airport AS airport_id, flights_count FROM Flights
           UNION ALL
       SELECT arrival_airport AS airport_id, flights_count FROM Flights ) T
  GROUP BY airport_id )

SELECT airport_id FROM CTE WHERE RN = 1
