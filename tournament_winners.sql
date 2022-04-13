'''
The winner in each group is the player who scored the maximum total points 
within the group. In the case of a tie, the lowest player_id wins.

Write an SQL query to find the winner in each group.

Return the result table in any order.

The query result format is in the following example.
'''


select group_id, player_id from 
(
    select p.player_id, p.group_id, 
    row_number() over(partition by p.group_id order by player_total.score desc, p.player_id asc) rank
    from players p join
        (
            select player_id, sum(player_score.score) as score
            from (
                    (select first_player as player_id, first_score as score from Matches)
                        union all
                    (select second_player as player_id, second_score as score from Matches)
                 ) player_score 
            group by player_id
        ) player_total
    on p.player_id = player_total.player_id
) rank_table 
where rank_table.rank = 1

---------------------------------------------------------
with main as (
select b.*, score
from (select first_player player_id, first_score score from matches
        UNION ALL
      select second_player player_id, second_score score from matches
) a
join players b
on a.player_id = b.player_id
),
sum_ranked as (
select group_id, player_id, sum(score) total_score
, rank() over (partition by group_id order by sum(score) desc, player_id asc) rank_val
from main
group by group_id, player_id
) 
select group_id, player_id 
from sum_ranked
where rank_val = 1


----------------------
This solution works on most databases (i.e. Oracle, PostgreSQL, MySQL etc.) and on the leetcode versions.

First, we can retrieve a set of all the players along with their scores per match using "union all" i.e. first player and their scores (first score) along with second players and their scores (second score):

select first_player as player, first_score as score from Matches
union all
select second_player, second_score from Matches
From this set, we can then add the scores for each player in all matches:

select player, sum(score) as score from
	(select first_player as player, first_score as score from Matches
	union all
	select second_player, second_score from Matches) s
group by player
We can refer to this as the players' scores. To get the group of each player we can simple join this "players' scores" set to Players set based on the player_id.

However, what we really need is the maximum score in each group, therefore we can use an aggregate function here along with the join:

select group_id, max(score)
from Players,
	(select player, sum(score) as score from
		(select first_player as player, first_score as score from Matches
		union all
		select second_player, second_score from Matches) s
	group by player) PlayerScores
where Players.player_id = PlayerScores.player
group by group_id
Now that we have the maximum score in each group, it is simply a matter of retrieving all players in the "players' score" set with that score

select group_id, player_id
from Players,
    (select player, sum(score) as score from
        (select first_player as player, first_score as score from Matches
        union all
        select second_player, second_score from Matches) s
    group by player) PlayerScores
    where Players.player_id = PlayerScores.player
        and (group_id, score) in                     # check against maximum score in each group
            (select group_id, max(score)
            from Players,
                (select player, sum(score) as score from
                    (select first_player as player, first_score as score from Matches
                    union all
                    select second_player, second_score from Matches) s
                group by player) PlayerScores
            where Players.player_id = PlayerScores.player
            group by group_id)
Final code for Solution 1:
Finally, we take care of players with the same score by retrieving the player with the id:

select group_id as GROUP_ID, min(player_id) as PLAYER_ID
from Players,
    (select player, sum(score) as score from
        (select first_player as player, first_score as score from Matches
        union all
        select second_player, second_score from Matches) s
    group by player) PlayerScores
where Players.player_id = PlayerScores.player and (group_id, score) in
	(select group_id, max(score)
	from Players,
		(select player, sum(score) as score from
			(select first_player as player, first_score as score from Matches
			union all
			select second_player, second_score from Matches) s
		group by player) PlayerScores
	where Players.player_id = PlayerScores.player
	group by group_id)
group by group_id
Solution 2:
In Solution 1, the PlayerScores set had to be created twice (first to get the scores and a second time to compare the scores with the maximum score in each group). One way to remove the repeating code segment would be to use Common Table Expression (however, I do not think this can be done in leetcode). Another way might be to use variables. However, we can also leverage a trick based on how MySQL handles aggregates when sql_mode=only_full_group_by is disabled (which is the case in leetcode). MySQL simple picks the first item in a row when a column is in the SELECT clause but not the GROUP BY clause. Other databases would throw an error. Therefore we can simply get the players' scores (ps) like we did in Solution 1 along with the group_id of each player by joining the subquery with the Players table. Then order them to make sure the first item of each group is what we are looking for:

select p.group_id, ps.player_id, sum(ps.score) as score from Players p,
	(select first_player as player_id, first_score as score from Matches
	union all
	select second_player, second_score from Matches) ps
where p.player_id = ps.player_id
group by ps.player_id order by group_id, score desc, player_id
Final code for Solution 2:
Aggregating this over the group_id will then give us our final result:

select group_id, player_id from (
	select p.group_id, ps.player_id, sum(ps.score) as score from Players p,
	    (select first_player as player_id, first_score as score from Matches
	    union all
	    select second_player, second_score from Matches) ps
	where p.player_id = ps.player_id
	group by ps.player_id order by group_id, score desc, player_id) top_scores
group by group_id
