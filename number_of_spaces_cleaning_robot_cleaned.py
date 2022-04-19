'''
A room is represented by a 0-indexed 2D binary matrix room where a 0 represents an empty space and a 1 represents a space with an object. The top left corner of the room will be empty in all test cases.

A cleaning robot starts at the top left corner of the room and is facing right. The robot 
will continue heading straight until it reaches the edge of the room or it hits an object, after 
which it will turn 90 degrees clockwise and repeat this process. The starting space and all spaces that the robot visits are cleaned by it.

Return the number of clean spaces in the room if the robot runs indefinetely.
'''

class Solution:
    def numberOfCleanRooms(self, room: List[List[int]]) -> int:
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        state = cleaned = r = c = 0
        m, n = len(room), len(room[0])
        visited = set()
        room[0][0] = -1  # We need to mark that we have cleaned the first room. For this reason, also, we return cleaned + 1
        
        # The only time you'd want to revisit a tile is if you're passing over that tile while in a different state. So, the halting condition
        # is when you revisit a tile while in the same state as the first time that you entered it
        
        while True:            
            dx, dy = dirs[state]
            
            if 0 <= r + dx < m and 0 <= c + dy < n and room[r+dx][c+dy] != 1:
                r += dx
                c += dy
                if room[r][c] == 0:
                    cleaned += 1
                    room[r][c] = -1				
            else:
                state = (state + 1) % 4                
                    
            if (r, c, state) in visited:
                return cleaned+1
            visited.add((r, c, state))
            
            
-------------------------------------------------------------------------------------
BFS Solution:

class Solution:
    def numberOfCleanRooms(self, room: List[List[int]]) -> int:
        directions = { #movement
            "right": (0,1),
            "left": (0,-1),
            "up": (-1,0),
            "down": (1,0)
        }
        
        turn = { #If can't move, rotate directon
            "right": "down",
            "down": "left",
            "left": "up",
            "up": "right"
        }
        
        def isValid(i,j):
            return not(0 > i or 0 > j or len(room) <= i or len(room[0]) <= j or room[i][j] == 1)
        
		ans = 0
		queue = deque([(0,0,"right")])
        seen = set()
        counted = set()
        while queue:
            i, j, direction = queue.popleft()
            
            if (i,j,direction) in seen:
                continue
            seen.add((i,j,direction))
                
            if (i,j) not in counted:
                ans += 1
                counted.add((i,j))
                
            di, dj = directions[direction]
            
            ni, nj = i+di, j+dj
            if not isValid(ni, nj):
                queue.append((i,j,turn[direction])) # Can't move, rotate direction
            else:
                queue.append((ni, nj, direction)) # Can move, keep going
                
        return ans
            
DFS Solution:

class Solution:
    def numberOfCleanRooms(self, room: List[List[int]]) -> int:
        directions = { #movement
            "right": (0,1),
            "left": (0,-1),
            "up": (-1,0),
            "down": (1,0)
        }
        
        turn = { #If can't move, rotate directon
            "right": "down",
            "down": "left",
            "left": "up",
            "up": "right"
        }
        
        def isValid(i,j):
            return not(0 > i or 0 > j or len(room) <= i or len(room[0]) <= j or room[i][j] == 1)
        
		ans = 0
		queue = [(0,0,"right")]
        seen = set()
        counted = set()
        while queue:
            i, j, direction = queue.pop()
            
            if (i,j,direction) in seen:
                continue
            seen.add((i,j,direction))
                
            if (i,j) not in counted:
                ans += 1
                counted.add((i,j))
                
            di, dj = directions[direction]
            
            ni, nj = i+di, j+dj
            if not isValid(ni, nj):
                queue.append((i,j,turn[direction])) # Can't move, rotate direction
            else:
                queue.append((ni, nj, direction)) # Can move, keep going
                
        return ans
---------------------------------------------------------------

The robot move towards one direction until it meets a border or obstacle. Then it makes a right turn.
Therefore, for each position (i,j), a robot can have at most 4 different states which is the direction it's heading when it passed that position. So we can just use 4 bits to record that state in a visited map V. Just like the one we just to do a regular graph search. But this time, the value in V is not a single boolean bit but a 4-bit state.

So robot keeps moving in its current direction dfs(new_i, new_j, d), or makes the right turn if it cannot move further dfs(i, j, new_d).
If the direction d has already been visited in the position (i,j) or dth bit in V[i][j] has been set to 1, we stop the search.
Eventually we count all visited pisitions that V[i][j] is not 0.

def numberOfCleanRooms(room)
	D = (0,1,0,-1,0)
	m, n = len(room), len(room[0])
	V = [[0] * n for _ in range(m)]

	def dfs(i, j, d):
		if V[i][j] >> d & 1:
			return
		V[i][j] |= 1 << d
		x, y = i+D[d], j+D[d+1]
		if 0 <= x < m and 0 <= y < n and not room[x][y]:
			return dfs(x, y, d)
		return dfs(i, j, (d+1) % 4)

	dfs(0, 0, 0)
	return sum(x != 0 for r in V for x in r)
--------------------------------------------------------------------------------

Simulates the movements until the robot does a 360 (4 turns), at which point it returns the result ...

def numberOfCleanRooms(self, room):
    m, n = len(room), len(room[0])
    count = 0
    x, y = 0, 0
    seen = set()
    direction = 'right'
    turns = 0
    while True:
        if turns == 4:
            return count
        elif x>=0 and x<m and y>=0 and y<n and room[x][y] == 0:
            if (x, y) not in seen:
                seen.add((x, y))
                count+=1
                turns = 0
                
            if direction == 'right':
                y+=1
            elif direction == 'left':
                y-=1
            elif direction == 'up':
                x-=1
            else:
                x+=1
        else:
            if direction=='right':
                y-=1
                direction = 'down'
            elif direction =='down':
                x-=1
                direction = 'left'
            elif direction == 'left':
                direction = 'up'
                y+=1
            else:
                direction = 'right'
                x+=1
            turns+=1
----------------------------------------------            
            



      
