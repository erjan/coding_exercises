'''
Two elements can form a bond if one of them is 'Metal' and the other is 'Nonmetal'.

Write an SQL query to find all the pairs of elements that can form a bond.

Return the result table in any order.

The query result format is in the following example.
'''



select distinct e1.symbol as metal, 
e2.symbol as nonmetal from elements e1  join elements e2

where (e1.type='Metal' and e2.type='Nonmetal') -- or (e1.type='Nonmetal' and e2.type='Metal')


---------------------------------------------------------------------------------------------------
# The idea here is to filter the records and then perform a cross product.

SELECT M.SYMBOL AS METAL, NM.SYMBOL AS NONMETAL
FROM 
( SELECT SYMBOL FROM ELEMENTS AS E WHERE E.TYPE = 'Metal' ) AS M ,
( SELECT SYMBOL FROM ELEMENTS AS E  WHERE E.TYPE = 'Nonmetal' ) AS NM 


-------------------------------------------------------------------------------
SELECT e.symbol as metal, e1.symbol as nonmetal
FROM Elements as e
JOIN Elements as e1
ON (e.type = "Metal" AND e1.type = "Nonmetal");
