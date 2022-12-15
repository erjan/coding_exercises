'''
There is a hotel with n rooms. The rooms are represented by a 2D integer array rooms where rooms[i] = [roomIdi, sizei] denotes that there is a room with room number roomIdi and size equal to sizei. Each roomIdi is guaranteed to be unique.

You are also given k queries in a 2D array queries where queries[j] = [preferredj, minSizej]. The answer to the jth query is the room number id of a room such that:

The room has a size of at least minSizej, and
abs(id - preferredj) is minimized, where abs(x) is the absolute value of x.
If there is a tie in the absolute difference, then use the room with the smallest such id. If there is no such room, the answer is -1.

Return an array answer of length k where answer[j] contains the answer to the jth query.
'''

from sortedcontainers import SortedList

class Solution:
    def closestRoom(self, rooms: List[List[int]], queries: List[List[int]]) -> List[int]:
        rooms.sort(key=lambda x: (-x[1], x[0])) # descending order 
        
        ans = [-1] * len(queries)
        sl = SortedList()
        k = 0 
        
        for (preferred, msz), i in sorted(zip(queries, range(len(queries))), key=lambda x: (-x[0][1], x[0][0])): # descending order 
            while k < len(rooms) and rooms[k][1] >= msz: 
                sl.add(rooms[k][0])
                k += 1
            v = sl.bisect_left(preferred)
            if sl: 
                if v == len(sl) or v > 0 and preferred - sl[v-1] <= sl[v] - preferred: ans[i] = sl[v-1]
                else: ans[i] = sl[v]
        return ans 
      
-------------------------------------------------------------------------------------------------------------------------------------------------

When you first look at this problem, you already know that you have to use binary search when searching for the ideal room for each query because linear search is trivial to implement.

The difficult part is figuring out how to perform binary search on the subset of rooms where room_size >= preferred_size and where that subset is sorted by room_id.

The key to solving the above statement requires the following steps:

Sort the rooms and queries by room size in descending order. This allows us to grow our subset of rooms to search without having to remove any rooms. (Example: a query with preferred size 1 will always include all the rooms for a query with preferred size 2)
When iterating through each query, you will add the new rooms into your search data structure. It is necessary for this data structure to have O(logn) insert and O(logn) search. That is a binary tree. If you want to get fancy, you can say AVL tree.
Search the binary tree for the best room_id and add it to your result array
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        
class Solution:
    def closestRoom(self, rooms: List[List[int]], queries: List[List[int]]) -> List[int]:
		# sort by room size
		rooms.sort(key=lambda x: -x[1])
        queries = sorted([[q[0], q[1], i] for i, q in enumerate(queries)], key=lambda x: -x[1])
        
		# pointer for iterating through your rooms in one pass
        r = 0
        
        root = None
        res = [-1] * len(queries)

        # pref size is going to be in descending order
        for pref_id, pref_size, index in queries:
            
			# add room_ids to your tree data structure
            while r < len(rooms) and rooms[r][1] >= pref_size:
                room_id = rooms[r][0]
                if root is None:
                    root = Node(room_id)
                else:
                    insert(root, room_id)
                    
                r += 1

			# search your tree data structure for best room_id
            if root is not None:
                res[index] = search(root, pref_id, math.inf)
        
        return res
    
def insert(root, val):
    # each val is guaranteed to be unique
    if val < root.val:
        if root.left is None:
            root.left = Node(val)
            return
        else:
            return insert(root.left, val)
    else:
        if root.right is None:
            root.right = Node(val)
            return
        else:
            return insert(root.right, val)

def search(root, val, res):
    if abs(val - root.val) < abs(val - res):
        res = root.val
        
    elif abs(val - root.val) == abs(val - res):
        res = min(res, root.val)
    
    if val < root.val:
        if root.left is None:
            return res
        else:
            return search(root.left, val, res)
    else:
        if root.right is None:
            return res
        else:
            return search(root.right, val, res)
