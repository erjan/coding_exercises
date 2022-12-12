'''
A storekeeper is a game in which the player pushes boxes around in a warehouse trying to get them to target locations.

The game is represented by an m x n grid of characters grid where each element is a wall, floor, or box.

Your task is to move the box 'B' to the target position 'T' under the following rules:

The character 'S' represents the player. The player can move up, down, left, right in grid if it is a floor (empty cell).
The character '.' represents the floor which means a free cell to walk.
The character '#' represents the wall which means an obstacle (impossible to walk there).
There is only one box 'B' and one target cell 'T' in the grid.
The box can be moved to an adjacent free cell by standing next to the box and then moving in the direction of the box. This is a push.
The player cannot walk through the box.
Return the minimum number of pushes to move the box to the target. If there is no way to reach the target, return -1.
'''


class Solution:
    def minPushBox(self, grid) -> int:
        def gen_next(x, y):
            for dx, dy in [(0, -1), (0, 1), (1, 0), (-1, 0)]:
                new_x = x + dx
                new_y = y + dy
                if 0 <= new_x < len(grid) and 0 <= new_y < len(grid[0]):
                    yield new_x, new_y

        def find_people_pos(x, y, box_pos):
            visited.add((x, y))
            for new_x, new_y in gen_next(x, y):
                if grid[new_x][new_y] == "." and (new_x, new_y) != box_pos and (new_x, new_y) not in visited:
                    find_people_pos(new_x, new_y, box_pos)

        def compute_push_pos(new_box_pos, original_pos):
            return 2 * original_pos[0] - new_box_pos[0], 2 * original_pos[1] - new_box_pos[1]

        q = deque([])
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "T":
                    target_pos = i, j
                    grid[i][j] = "."
                elif grid[i][j] == "B":
                    grid[i][j] = "."
                    box_pos = i, j
                elif grid[i][j] == "S":
                    people_pos = i, j
                    grid[i][j] = "."
        if box_pos == target_pos:
            return 0

        q.append((box_pos, 0, people_pos))
        box_visited = set()
        while len(q) > 0:
            (x, y), cnt, people_pos = q.popleft()
            visited = set()
            find_people_pos(people_pos[0], people_pos[1], (x,y))
            for new_box_pos in gen_next(x, y):
                
                if (new_box_pos, (x,y)) in box_visited or grid[new_box_pos[0]][new_box_pos[1]] == "#":
                    continue
                push_pos = compute_push_pos(new_box_pos, (x, y))
                if push_pos in visited:
                    if new_box_pos == target_pos:
                        return cnt + 1
                    q.append((new_box_pos, cnt + 1, (x,y)))
                    box_visited.add((new_box_pos, (x, y)))

        return -1
      
---------------------------------------------------------------------------------------------------------------

class Solution:
    def minPushBox(self, grid: List[List[str]]) -> int:
        
        neighbors = [(0, -1), (0, 1), (-1, 0), (1, 0)]
        
        def player_bfs(st_row, st_col, tgt_row, tgt_col):
            nonlocal rows, cols
            if (st_row, st_col) == (tgt_row, tgt_col):
                return True
            q = deque([(st_row, st_col)]) 
            seen = [[False] * cols for _ in range(rows)]
            seen[st_row][st_col] = True
            
            while q:
                row, col = q.pop()
                for r, c in neighbors:
                    if 0 <= row+r < rows and 0 <= col+c < cols and not seen[row+r][col+c] and grid[row+r][col+c] == '.':
                        if row+r == tgt_row and col+c == tgt_col:
                            return True
                        seen[row+r][col+c] = True
                        q.appendleft((row+r, col+c))
            return False
            
        def box_bfs(st_row, st_col):
            nonlocal rows, cols, target
            q = deque([(st_row, st_col, start[0], start[1], 0)])
            seen = {st_row, st_col, start[0], start[1]}
            
            while q:
                row, col, prow, pcol, moves = q.pop()
                grid[row][col] = 'B'
                for r, c in neighbors:
                    box_can_move = 0 <= row+r < rows and 0 <= col+c < cols and (row+r, col+c, row-r, col-c) not in seen and grid[row+r][col+c] == '.'
                    if box_can_move and player_bfs(prow, pcol, row-r, col-c):
                        if (row+r, col+c) == target:
                            return moves + 1
                        seen.add((row+r, col+c, row-r, col-c))
                        q.appendleft((row+r, col+c, row-r, col-c, moves+1))
                grid[row][col] = '.'
            
            return -1
        
        start = target = box = None
        rows, cols = len(grid), len(grid[0])
        for r, row in enumerate(grid):
            for c, pos in enumerate(row):
                if pos == 'S':
                    start = (r, c)
                    grid[r][c] = '.'
                elif pos == 'T':
                    target = (r, c)
                    grid[r][c] = '.'
                elif pos == 'B':
                    box = (r, c)
                    grid[r][c] = '.'
        
        return box_bfs(*box)
