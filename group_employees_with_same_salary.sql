'''

A company wants to divide the employees into teams such that all the members on each team have the same salary. The teams should follow these criteria:

Each team should consist of at least two employees.
All the employees on a team should have the same salary.
All the employees of the same salary should be assigned to the same team.
If the salary of an employee is unique, we do not assign this employee to any team.
A team's ID is assigned based on the rank of the team's salary relative to the other teams' salaries, where the team with the lowest salary has team_id = 1. Note that the salaries for employees not on a team are not included in this ranking.
Write an SQL query to get the team_id of each employee that is in a team.

Return the result table ordered by team_id in ascending order. In case of a tie, order it by employee_id in ascending order.

The query result format is in the following example.

'''

SELECT employee_id, name, salary, DENSE_RANK() OVER (ORDER BY salary) as team_id
FROM 
    (SELECT employee_id, name, salary, count(*) OVER (PARTITION BY salary) as cnt
     FROM employees) emp
WHERE cnt>=2;
