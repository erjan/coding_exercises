'''
You would like to compute the scores of all teams after all matches. Points are awarded as follows:
A team receives three points if they win a match (i.e., Scored more goals than the opponent team).
A team receives one point if they draw a match (i.e., Scored the same number of goals as the opponent team).
A team receives no points if they lose a match (i.e., Scored fewer goals than the opponent team).
Write an SQL query that selects the team_id, team_name and num_points of each team in the tournament after all described matches.

Return the result table ordered by num_points in decreasing order. In case of a tie, order the records by team_id in increasing order.

The query result format is in the following example.

right join - Because a team might have not played any matches


'''

select 

team_id,
team_name,

sum(case 
    
    when team_id = host_team and host_goals > guest_goals then 3 
    when team_id = guest_team and host_goals < guest_goals then 3 
    when host_goals = guest_goals then 1 else 0 end) as num_points
    

from matches m right join teams t 
on m.host_team = t.team_id or m.guest_team = t.team_id
group by team_id
order by num_points desc, team_id


-------------------------

select t.team_id, t.team_name, ifnull(sum(sub.team_points),0) as num_points
from teams t
left join
((select host_team as team,
        case when host_goals > guest_goals then 3
            when host_goals = guest_goals then 1
            else 0 end as team_points
  from matches)
 union all
(select guest_team as team,
        case when host_goals < guest_goals then 3
            when host_goals = guest_goals then 1
            else 0 end as team_points
 from matches))sub
on t.team_id = sub.team
group by t.team_id
order by 3 desc, 1
