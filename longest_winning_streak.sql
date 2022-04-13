'''
The winning streak of a player is the number of consecutive wins uninterrupted by draws or losses.

Write an SQL query to count the longest winning streak for each player.

Return the result table in any order.

The query result format is in the following example.
'''

WITH cte AS (
SELECT player_id, result, match_day,
ROW_NUMBER() OVER(PARTITION BY player_id ORDER BY match_day) AS rnk
FROM matches ),
# Segregation of consecutive wins into separate groups for each player_id identified by group_id
temp AS (
SELECT player_id,
rnk - ROW_NUMBER() OVER(PARTITION BY player_id ORDER BY match_day) AS group_id
FROM cte
WHERE result = 'Win')

SELECT pl.player_id, IFNULL(MAX(ct.cnt),0) as longest_streak
FROM (SELECT DISTINCT player_id FROM matches) pl
LEFT JOIN
(SELECT player_id, group_id, COUNT(*) as cnt FROM temp GROUP BY 1, 2) ct
ON pl.player_id = ct.player_id
GROUP BY 1

------------------------------------------------

WITH base_data AS (
  SELECT
    M1.*,
    ROW_NUMBER() OVER (PARTITION BY M1.player_id ORDER BY M1.match_day) AS match_seq_num
  FROM
    Matches M1
), grps AS (
  SELECT
    BD.*,
    BD.match_seq_num - ROW_NUMBER() OVER (PARTITION BY BD.player_id ORDER BY BD.match_day) AS grp
  FROM
    base_data BD
  WHERE
    BD.result = 'Win'
), consec_counts AS (
  SELECT
    G.player_id,
    COUNT(G.grp) AS consec_count,
    ROW_NUMBER() OVER(PARTITION BY G.player_id ORDER BY COUNT(G.grp) DESC) AS consec_rnk
  FROM
    grps G
  GROUP BY
    G.player_id, G.grp
)
SELECT
  M2.player_id,
  (CASE WHEN CC.player_id IS NULL THEN 0 ELSE CC.consec_count END) AS longest_streak
FROM
  Matches M2
  LEFT JOIN consec_counts CC ON M2.player_id = CC.player_id
WHERE
  CC.consec_rnk = 1 OR CC.player_id IS NULL
GROUP BY
  M2.player_id, longest_streak;
Description: The problem description has all the trappings of a gaps and islands kind of problem. Specifically, we're trying to find the largest "island" or grouping of consecutive wins for each player.

The solution above will become easy to understand if we dissect it CTE by CTE:

base_data: This CTE has one simple goal: simplify the process of detecting islands and gaps by assigning a sequence number to each match based on player_id and match_day (i.e., each set of sequence numbers should be specific to a player_id and be ordered by match_date). How this simplifies the process will become clear in the next CTE.

+-----------+------------+--------+---------------+
| player_id | match_day  | result | match_seq_num |
+-----------+------------+--------+---------------+
|         1 | 2022-01-17 | Win    |             1 |
|         1 | 2022-01-18 | Win    |             2 |
|         1 | 2022-01-25 | Win    |             3 |
|         1 | 2022-01-31 | Draw   |             4 |
|         1 | 2022-02-08 | Win    |             5 |
|         2 | 2022-02-06 | Lose   |             1 |
|         2 | 2022-02-08 | Lose   |             2 |
|         3 | 2022-03-30 | Win    |             1 |
+-----------+------------+--------+---------------+
grps: We can now identify groups of consecutive wins by retaining only the desired result values, namely 'WIN', and then using the match_seq_num in an arithmetically effective fashion (i.e., consecutive wins for each player will have the same grp number--the "why" behind this may not be entirely clear at first, but think hard about it--this is the key to solving this problem, but it is also the hardest part to grok).

+-----------+------------+--------+---------------+-----+
| player_id | match_day  | result | match_seq_num | grp |
+-----------+------------+--------+---------------+-----+
|         1 | 2022-01-17 | Win    |             1 |   0 |
|         1 | 2022-01-18 | Win    |             2 |   0 |
|         1 | 2022-01-25 | Win    |             3 |   0 |
|         1 | 2022-02-08 | Win    |             5 |   1 |
|         3 | 2022-03-30 | Win    |             1 |   0 |
+-----------+------------+--------+---------------+-----+
consec_counts: The hardest part is done. The grps CTE gives us what we need to effectively "rank" the groupings of consecutive wins by player (i.e., groupings with the highest number of consecutive wins will be ranked first):

+-----------+--------------+------------+
| player_id | consec_count | consec_rnk |
+-----------+--------------+------------+
|         1 |            3 |          1 |
|         1 |            1 |          2 |
|         3 |            1 |          1 |
+-----------+--------------+------------+
All we have to do now is select records from the consec_counts CTE where consec_rnk = 1, but don't forget that we also need to account for players who had no wins at all. We can easily do this by using a LEFT JOIN and assigning a longest_streak of 0 to such players. This gives us our final desired result set:

+-----------+----------------+
| player_id | longest_streak |
+-----------+----------------+
|         1 |              3 |
|         2 |              0 |
|         3 |              1 |
+-----------+----------------+
Follow up: This is probably one of the nicest parts about this clean approach. The only change needed to solve the follow up question is to change BD.result = 'Win' within the grps CTE to BD.result != 'Lose'.
