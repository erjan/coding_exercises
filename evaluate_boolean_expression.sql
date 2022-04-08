'''

Write an SQL query to evaluate the boolean expressions in Expressions table.

Return the result table in any order.

The query result format is in the following example.

'''


SELECT e.left_operand, e.operator, e.right_operand,
    (
        CASE
            WHEN e.operator = '<' AND v1.value < v2.value THEN 'true'
            WHEN e.operator = '=' AND v1.value = v2.value THEN 'true'
            WHEN e.operator = '>' AND v1.value > v2.value THEN 'true'
            ELSE 'false'
        END
    ) AS value
FROM Expressions e
JOIN Variables v1
ON e.left_operand = v1.name
JOIN Variables v2
ON e.right_operand = v2.name

----------------

SELECT e.left_operand, e.operator, e.right_operand,
       CASE WHEN operator = '>' THEN IF(v1.value > v2.value, 'true', 'false')
            WHEN operator = '<' THEN IF(v1.value < v2.value, 'true', 'false')
            ELSE IF(v1.value = v2.value, 'true', 'false')
       END AS value
FROM Expressions e
JOIN Variables v1 ON v1.name = e.left_operand
JOIN Variables v2 ON v2.name = e.right_operand;
