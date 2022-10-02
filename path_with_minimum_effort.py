'''
You are a hiker preparing for an upcoming hike. You are given heights, a 2D array of size rows x columns, where heights[row][col] represents the height of cell (row, col). You are situated in the top-left cell, (0, 0), and you hope to travel to the bottom-right cell, (rows-1, columns-1) (i.e., 0-indexed). You can move up, down, left, or right, and you wish to find a route that requires the minimum effort.

A route's effort is the maximum absolute difference in heights between two consecutive cells of the route.

Return the minimum effort required to travel from the top-left cell to the bottom-right cell.
'''
class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        
        rows = len(heights)
        cols = len(heights[0])
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        # Use a heap, store the max diff. we find as the first element to be sorted by.
        hq = [(0, heights[0][0], 0, 0)]
        heapq.heapify(hq)
		# Mark that we visited this node.
        heights[0][0] = '#'
        while hq:
            md, prev, r, c = heapq.heappop(hq)
            heights[r][c] = '#'
			# Given the nature of our algorithm, the first option we come across at the end location
			# will be the most optimal.
            if r == rows-1 and c == cols-1:
                return md
            for y, x in directions:
                nr = r + y
                nc = c + x
                if 0 <= nr < rows and 0 <= nc < cols and heights[nr][nc] != '#':
				    # Take the max of the next potential move or the largest we've seen so far.
                    heapq.heappush(hq, (max(abs(heights[nr][nc]-prev), md), heights[nr][nc], nr, nc))
        
        return -1
      
--------------------------------------------------------------------------------      
import collections
class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        r, c = len(heights), len(heights[0])


        def check(cost): # return Ture if we can otherwise False
            # this is check for each cell if we can reach the 
            # bottom right
            visited = set((0,0))
            queue = collections.deque([(0, 0)])
            
            # four diection we can search
            directions = [(0,-1), (0, 1), (1, 0), (-1, 0)]
            
            while queue:
                x, y = queue.popleft()
                if x == r-1 and y == c - 1: #reach the bottom right
                    return True
                for dx, dy in directions:
                    if 0<=x+dx<r and 0<=y+dy<c and (x+dx, y+dy) not in visited:
                        diff = abs(heights[x+dx][y+dy]-heights[x][y])
                        if diff <= cost:
                            visited.add((x+dx, y+dy))
                            queue.append((x+dx, y+dy))
            
            return False


        # we check use binary search from the 
        # largest possible value
        left = 0
        right = 10**6
        while left < right:
            mid = (left+right) // 2
            if check(mid):
                right = mid
            else:
                left = mid + 1
        return left
      
---------------------------------------------------------------------------------------------

class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        m, n = len(heights), len(heights[0])
        res = 0
        heap = [(0, 0, 0)] # path, row, col
        
        while heap:
            diff, x, y = heappop(heap)
            
            res = max(res, diff)
            
            if x == m-1 and y == n-1:
                return res
            
            if heights[x][y] == 0:
                continue
                
            curr_height = heights[x][y]
            heights[x][y] = 0
            
            for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                new_x, new_y = x + dx, y + dy
                
                if 0 <= new_x < m and 0 <= new_y < n and heights[new_x][new_y] != 0:
                    new_diff = abs(heights[new_x][new_y] - curr_height)
                    heappush(heap, (new_diff, new_x, new_y))
        
        return res
