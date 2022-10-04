'''
There are n rooms labeled from 0 to n - 1 and all the rooms are locked except for room 0. Your goal is to visit all the rooms. However, you cannot enter a locked room without having its key.

When you visit a room, you may find a set of distinct keys in it. Each key has a number on it, denoting which room it unlocks, and you can take all of them with you to unlock the other rooms.

Given an array rooms where rooms[i] is the set of keys that you can obtain if you visited room i, return true if you can visit all the rooms, or false otherwise.
'''

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited_rooms = set()
        stack = [0] # for rooms that we need to visit and we start from room [0]
        
        while stack: 
            room = stack.pop() 
            visited_rooms.add(room)
            for key in rooms[room]:
                if key not in visited_rooms:
                    stack.append(key)
        return len(visited_rooms) == len(rooms)  
      
--------------------------------------

class Solution:
    def canVisitAllRooms(self, R: List[List[int]]) -> bool:
        vis, stack, count = [False for _ in range(len(R))], [0], 1
        vis[0] = 1
        while stack:
            keys = R[stack.pop()]
            for k in keys:
                if not vis[k]:
                    stack.append(k)
                    vis[k] = True
                    count += 1
        return len(R) == count
      
------------------------------------------------------------------------------------------------
DFS:

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = [True] + [False]*(len(rooms) - 1)
        stack = [0]
        while stack:
            cur = stack.pop()
            for room in rooms[cur]:
                if not visited[room]:
                    visited[room] = True
                    stack.append(room)
        return all(visited)
BFS:

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = [True] + [False]*(len(rooms) - 1)
        dq = deque([0])
        while dq:
            cur = dq.popleft()
            for room in rooms[cur]:
                if not visited[room]:
                    visited[room] = True
                    dq.append(room)
        return all(visited)
