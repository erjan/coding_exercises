'''
You are given an n x n integer matrix board where the cells are labeled from 1 to n2 in a Boustrophedon style starting from the bottom left of the board (i.e. board[n - 1][0]) and alternating direction each row.

You start on square 1 of the board. In each move, starting from square curr, do the following:

Choose a destination square next with a label in the range [curr + 1, min(curr + 6, n2)].
This choice simulates the result of a standard 6-sided die roll: i.e., there are always at most 6 destinations, regardless of the size of the board.
If next has a snake or ladder, you must move to the destination of that snake or ladder. Otherwise, you move to next.
The game ends when you reach the square n2.
A board square on row r and column c has a snake or ladder if board[r][c] != -1. The destination of that snake or ladder is board[r][c]. Squares 1 and n2 do not have a snake or ladder.

Note that you only take a snake or ladder at most once per move. If the destination to a snake or ladder is the start of another snake or ladder, you do not follow the subsequent snake or ladder.

For example, suppose the board is [[-1,4],[-1,3]], and on the first move, your destination square is 2. You follow the ladder to square 3, but do not follow the subsequent ladder to 4.
Return the least number of moves required to reach the square n2. If it is not possible to reach the square, return -1.
'''

Thought process
simply apply BFS to find the length of shortest path from 1 to n*n
key point is to correctly compute the corresponding coordinates of the label
also remember to avoid circle by using a hashset to track visited positions
time complexity: O(n^2), n is the width and height of the grid
space complexity: O(n^2)
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        def label_to_position(label):
            r, c = divmod(label-1, n)
            if r % 2 == 0:
                return n-1-r, c
            else:
                return n-1-r, n-1-c
            
        seen = set()
        queue = collections.deque()
        queue.append((1, 0))
        while queue:
            label, step = queue.popleft()
            r, c = label_to_position(label)
            if board[r][c] != -1:
                label = board[r][c]
            if label == n*n:
                return step
            for x in range(1, 7):
                new_label = label + x
                if new_label <= n*n and new_label not in seen:
                    seen.add(new_label)
                    queue.append((new_label, step+1))
        return -1
-------------------------------------------------------------------------------------------
class Solution:
	def snakesAndLadders(self, board: List[List[int]]) -> int:
		n=len(board)
		start, end =1,n*n
		visited=set()
		queue=deque()
		queue.append((start,0))                                #initial state before throwing dice
		
		#the purpose of this function is to give row and column value of a cell after adding a move comes on dice
		def find_coordinates(current_position):
			row = n - 1 - (current_position - 1) // n          #normal calculation to find row number of a cell
			col = (current_position - 1) % n                   #normal calculation to find column number of a cell
			if row % 2 == n % 2:                               #board is in  Boustrophedon style so handle it we are checking this condition
				return (row, n - 1 - col)
			else:
				return (row, col)

		while queue:
			curr_pos, steps=queue.popleft()
			if curr_pos == end:                                         #when player reaches at end, return steps 
				return steps

			for dice in range(1,7):                                     #iterating on all numbers of dices
				if curr_pos + dice >end:                                #not valid position to move
					break
				next_row, next_col = find_coordinates(curr_pos + dice)  #got coordinates of row and column
				if (next_row, next_col) not in visited:                 #checking that cell is already not visited
					visited.add((next_row, next_col))
					if board[next_row] [next_col]!=-1:                  #if there is ladder
						queue.append((board[next_row][next_col],steps+1))
					else:
						queue.append((curr_pos + dice,steps+1))
		return -1
