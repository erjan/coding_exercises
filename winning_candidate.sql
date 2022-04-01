'''

Write an SQL query to report the name of the winning candidate (i.e., the candidate who got the largest number of votes).

The test cases are generated so that exactly one candidate wins the elections.

The query result format is in the following example.
'''

select candidate.name 

from candidate join vote on vote.candidateId = candidate.id

group by candidate.id
order by count(candidate.id)  desc limit 1


#another using window

select name from 
(
select name, dense_rank() over (order by count(CandidateId) desc) rnk 
from candidate c inner join vote v
on c.id = v.candidateid
group by name
) a
where a.rnk = 1
