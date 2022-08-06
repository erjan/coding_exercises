'''
Write an SQL query to find all numbers that appear at least three times consecutively.

Return the result table in any order.

The query result format is in the following example.
'''


select distinct l1.num as ConsecutiveNums from logs l1, logs l2 , logs l3

where l1.id = l2.id-1 and l2.id = l3.id-1
and l1.num = l2.num and l1.num = l3.num

