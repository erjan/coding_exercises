'''

Write an SQL query to independently:

order first_col in ascending order.
order second_col in descending order.
The query result format is in the following example.
'''


SELECT first_col, second_col
FROM (
    SELECT first_col, ROW_NUMBER() OVER(ORDER BY first_col ASC) AS r
    FROM Data
) a
JOIN (
    SELECT second_col, ROW_NUMBER() OVER(ORDER BY second_col DESC) AS r
    FROM Data
) b
ON a.r = b.r


-------------------


Explanation: First a comment on the difficulty rating: I'm not sure how this problem is supposed to be "Easy". Sure, it's fairly easy if you know all about window functions, as this answer and the two other currently existing answers demonstrate. But if you don't know about window functions, then good luck. This is neither a "Hard" problem nor an "Easy" problem. Hm. I wonder what it should be categorized as. Anyway ...

The chief difficulty in this problem lies in trying to treat first_col and second_col as "individual units" of some sort. If we could do that, then we would at least have a starting point. That's what the ROW_NUMBER() window function allows us to do, namely by assigning a "rank" or "order" number to the data set based on whatever criteria we choose. Since we want to treat first_col and second_col as separate entities, we simply use ROW_NUMBER() twice in such a way that we treat first_col and second_col separately and record information about their ordering or ranking. The result set of the col_ranks CTE gives us this information:

+-----------+------------+--------+--------+
| first_col | second_col | fc_rnk | sc_rnk |
+-----------+------------+--------+--------+
|         1 |          4 |      1 |      1 |
|         2 |          3 |      2 |      2 |
|         4 |          2 |      4 |      3 |
|         3 |          1 |      3 |      4 |
+-----------+------------+--------+--------+
What really needs to happen now is we need the fc_rnk and sc_rnk values to match up--we need to report the first_col and second_col values in such a way that the values in fc_rnk and sc_rnk run from 1 to n in sequential fashion (i.e., 1, 2, ..., n-1, n). We can easily accomplish this by INNER JOINing the col_ranks CTE with itself on the condition that CR1.fc_rnk = CR2.sc_rnk. All that's left to do now is to select the first_col and second_col values and order them by either CR1.fc_rnk or CR2.sc_rnk. The choice is arbitrary since they both represent the same value (as evidenced by our join condition).


WITH col_ranks AS (
  SELECT
    D.first_col,
    D.second_col,
    ROW_NUMBER() OVER (ORDER BY D.first_col) AS fc_rnk,
    ROW_NUMBER() OVER (ORDER BY D.second_col DESC) AS sc_rnk
  FROM
    Data D
)
SELECT
  CR1.first_col,
  CR2.second_col
FROM
  col_ranks CR1
  INNER JOIN col_ranks CR2 ON CR1.fc_rnk = CR2.sc_rnk
ORDER BY
  CR1.fc_rnk;
