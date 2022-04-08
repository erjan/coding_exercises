'''

Write an SQL query to report the IDs of the candidates who have at least two years of experience and the sum of the score of their interview rounds is strictly greater than 15.

Return the result table in any order.

The query result format is in the following example.

'''



with h as(

select candidate_id, years_of_exp 

from candidates 

inner join rounds

using(interview_id)

group by candidate_id
having sum(score) > 15)


select candidate_id from h
where years_of_exp  >=2



------------------------------------

WITH score AS
(
SELECT interview_id, SUM(score) AS score_sum
FROM rounds
GROUP BY interview_id
)

SELECT c.candidate_id AS candidate_id
FROM candidates c
JOIN score s
ON c.interview_id = s.interview_id AND c.years_of_exp >= 2 AND s.score_sum > 15
