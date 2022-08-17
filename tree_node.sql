'''
Each node in the tree can be one of three types:

"Leaf": if the node is a leaf node.
"Root": if the node is the root of the tree.
"Inner": If the node is neither a leaf node nor a root node.
Write an SQL query to report the type of each node in the tree.

Return the result table ordered by id in ascending order.

The query result format is in the following example.
'''

select 

id as 'Id',

case when tree.id = (select atree.id from tree atree where atree.p_id is null) then 'Root'
     when tree.id in(select atree.p_id from tree atree) then 'Inner'
     else 'Leaf' end as Type
     
     from tree order by 'Id'

