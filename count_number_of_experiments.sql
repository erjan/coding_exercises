'''

Write an SQL query to report the number of experiments done on each of the three platforms for each of the three given experiments. Notice that all the pairs of (platform, experiment) should be included in the output including the pairs with zero experiments.

Return the result table in any order.

The query result format is in the following example.

'''


WITH CTE AS (
              SELECT platform, experiment_name
              FROM (SELECT 'IOS' AS platform UNION SELECT 'Android' UNION SELECT 'Web') E1 
                   CROSS JOIN
                   (SELECT 'Programming' AS experiment_name UNION SELECT 'Sports' UNION SELECT 'Reading') E2
            )

SELECT CTE.platform, CTE.experiment_name, COUNT(E.experiment_id) AS num_experiments
FROM CTE 
LEFT JOIN Experiments E ON CTE.platform = E.platform AND CTE.experiment_name = E.experiment_name
GROUP BY CTE.platform, CTE.experiment_name
ORDER BY 1 ASC
