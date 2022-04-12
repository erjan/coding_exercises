'''
Write an SQL query to:

Find the name of the user who has rated the greatest number of movies. In case of a tie, return the lexicographically smaller user name.
Find the movie name with the highest average rating in February 2020. In case of a tie, return the lexicographically smaller movie name.
The query result format is in the following example.
'''

(SELECT name results
FROM users u
JOIN movierating mr
ON u.user_id = mr.user_id
GROUP BY 1
ORDER BY count(rating) desc, 1 asc Limit 1)

UNION

(SELECT title results
FROM movies m
JOIN movierating mr
ON m.movie_id = mr.movie_id
WHERE month(created_at) = 2
GROUP BY 1
ORDER BY avg(rating) desc, 1 asc
Limit 1)

---------------------

(
  SELECT u.name AS results
  FROM Movie_Rating r LEFT JOIN Users u
  ON (r.user_id = u.user_id)
  GROUP BY r.user_id
  ORDER BY COUNT(r.movie_id) DESC, u.name 
  LIMIT 1
)
UNION
(
  SELECT m.title AS results
  FROM Movie_Rating r LEFT JOIN Movies m
  ON (r.movie_id = m.movie_id)
  WHERE r.created_at LIKE '2020-02%'
  GROUP BY r.movie_id
  ORDER BY AVG(r.rating) DESC, m.title 
  LIMIT 1
)

----------------------------------------------

with CTE1 as
(
select u.name,  dense_rank() over(order by count(m.rating) desc, u.name asc) as rnk1
from MovieRating as m
join Users as u 
using (user_id)
group by user_id
),

CTE2 as
(
select m2.title, dense_rank() over(order by avg(rating) desc, m2.title asc) as rnk2 
from MovieRating as m1
join Movies as m2
using (movie_id)
where m1.created_at between '2020-02-01' and '2020-02-29'
group by movie_id

)

select name as results 
from CTE1
where rnk1 = 1

union all

select title as results
from CTE2
where rnk2 = 1
;
