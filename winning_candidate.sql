
select candidate.name 

from candidate join vote on vote.candidateId = candidate.id

group by candidate.id
order by count(candidate.id)  desc limit 1
