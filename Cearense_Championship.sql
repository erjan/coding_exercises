'''
The Soccer Cearense Championship attracts
thousands of fans every year and you work for a newspaper and are in charge 
to calculate the score table. Show a table with the following rows: the team 
name, number of matches, victories, defeats, draws, and scores. Knowing that the 
score is calculated with each victory valuing 3 points, draw valuing 1 and defeat 
valuing 0. In the end, show your table with the score from the highest to the lowest.
'''


with h as(SELECT teams.name,count(name) as matches, 
count( CASE WHEN (team_1_goals > team_2_goals and teams.id = team_1) or 
     (team_2_goals > team_1_goals and teams.id = team_2) then 1 end ) as victories,
     
count( CASE WHEN (team_1_goals > team_2_goals and teams.id = team_2) or 
(team_2_goals > team_1_goals and teams.id = team_1) then 1 end ) as defeats, 

count( CASE WHEN (team_1_goals = team_2_goals and teams.id = team_1) or 
(team_1_goals = team_2_goals and teams.id = team_2) then 1 end) as draws 



FROM teams left JOIN matches ON teams.id = matches.team_1 or teams.id = matches.team_2 

group by teams.id )

select name, matches, victories, defeats, draws,

victories *3 +  draws*1 as score
from h
order by score desc


#the idea is to use left join not inner join!
