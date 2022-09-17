'''
A game is played by a cat and a mouse named Cat and Mouse.

The environment is represented by a grid of size rows x cols, where each element is a wall, floor, player (Cat, Mouse), or food.

Players are represented by the characters 'C'(Cat),'M'(Mouse).
Floors are represented by the character '.' and can be walked on.
Walls are represented by the character '#' and cannot be walked on.
Food is represented by the character 'F' and can be walked on.
There is only one of each character 'C', 'M', and 'F' in grid.
Mouse and Cat play according to the following rules:

Mouse moves first, then they take turns to move.
During each turn, Cat and Mouse can jump in one of the four directions (left, right, up, down). They cannot jump over the wall nor outside of the grid.
catJump, mouseJump are the maximum lengths Cat and Mouse can jump at a time, respectively. Cat and Mouse can jump less than the maximum length.
Staying in the same position is allowed.
Mouse can jump over Cat.
The game can end in 4 ways:

If Cat occupies the same position as Mouse, Cat wins.
If Cat reaches the food first, Cat wins.
If Mouse reaches the food first, Mouse wins.
If Mouse cannot get to the food within 1000 turns, Cat wins.
Given a rows x cols matrix grid and two integers catJump and mouseJump, return true if Mouse can win the game if both Cat and Mouse play optimally, otherwise return false.
'''



from collections import defaultdict, deque
class Solution:
    def canMouseWin(self, grid: List[str], catJump: int, mouseJump: int) -> bool:
        m, n = len(grid), len(grid[0])
        # Grab the positions for mouse, cat, and food
        init_pos = {
            grid[r][c]: (r, c)
            for r in range(m) for c in range(n)
            if grid[r][c] in 'MCF'
        }
        
        def next_positions(r, c, jump):
            yield r, c
            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                for k in range(1, jump + 1):
                    rr, cc = r + k * dr, c + k * dc
                    if not (0 <= rr < m and 0 <= cc < n): break
                    if grid[rr][cc] == '#': break
                    yield rr, cc
        
        cache, G_mouse, G_cat = defaultdict(int), {}, {}
        # Queue elements in format (pos_mouse, pos_cat, who_move_last)
        # Queue contains all states that mouse will win
        queue = deque()
        for r in range(m):
            for c in range(n):
                if grid[r][c] == '#': continue
                # Fill the cache with final states
                for turn in 'MC':
                    # Cat catches mouse
                    cache[((r, c), (r, c), turn)] = 2
                    # Cat reaches food
                    cache[((r, c), init_pos['F'], turn)] = 2
                    # Mouse reaches food
                    cache[(init_pos['F'], (r, c), turn)] = 1
                    # Add mouse win states to the queue
                    queue.append((init_pos['F'], (r, c), turn))
                # Build graphs that mouse and cat can move for the next step
                G_mouse[(r, c)] = set(next_positions(r, c, mouseJump))
                G_cat[(r, c)] = set(next_positions(r, c, catJump))
        
        while queue:
            pos_mouse, pos_cat, turn = queue.popleft()
            if turn == 'M':  # Last time move by mouse
                for last_pos_mouse in G_mouse[pos_mouse]:
                    last_state = (last_pos_mouse, pos_cat, 'C')
                    if cache[last_state] > 0: continue
                    # Mouse win moves from last_pos_mouse to pos_mouse and win
                    cache[last_state] = 1
                    # Once enter this state mouse will be guaranteed to win
                    queue.append(last_state)
            else:  # Last time move by cat
                for last_pos_cat in G_cat[pos_cat]:
                    last_state = (pos_mouse, last_pos_cat, 'M')
                    if cache[last_state] > 0: continue
                    # Warn cat should not move from last_pos_cat to pos_cat
                    cache[last_state] -= 1
                    # No matter how cat moves from last_pos_cat, it will enter a state that mouse win
                    if -cache[last_state] == len(G_cat[last_pos_cat]):
                        cache[last_state] = 1
                        queue.append(last_state)
                        
        # We only need to consider the case of mouse win. Both cat win and draw cause mouse to lose.
        init_state = (init_pos['M'], init_pos['C'], 'C')
        return cache[init_state] == 1
