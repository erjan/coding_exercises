'''
Given a m x n binary matrix mat. In one step, you can choose one cell and flip it and all the four neighbors of it if they exist (Flip is changing 1 to 0 and 0 to 1). A pair of cells are called neighbors if they share one edge.

Return the minimum number of steps required to convert mat to a zero matrix or -1 if you cannot.

A binary matrix is a matrix with all cells equal to 0 or 1 only.

A zero matrix is a matrix with all cells equal to 0.
'''

# class Solution:
#     def minFlips(self, mat: List[List[int]]) -> int:
class Solution:
    def minFlips(self, mat: List[List[int]]) -> int:
        '''
        Flatten the matrix into a string, so we can use it as a state, then
        use BFS to find the target which would be '0000..000' depending on the size of the matrix.
        
        Nothing special. This problem is similar to 773. Sliding Puzzle.
        '''
        rows, cols = len(mat), len(mat[0])
        initial = ''.join(str(cell) for row in mat for cell in row)
        target = '0' * (rows * cols)
        '''bfs'''
        flips = { '1': '0', '0': '1' }
        def flip(node, pos):
            node[pos] = flips[node[pos]]
            if pos % cols != 0:
                left = pos - 1
                node[left] = flips[node[left]]
            if pos % cols < cols - 1:
                right = pos + 1
                node[right] = flips[node[right]]
            if pos >= cols:
                top = pos - cols
                node[top] = flips[node[top]]
            if pos < (rows - 1) * cols:
                bottom = pos + cols
                node[bottom] = flips[node[bottom]]
        
        q = collections.deque([initial])
        steps = 0
        visited = set()
        while q:
            for _ in range(len(q)):
                node = q.popleft()
                if node == target:
                    return steps
                if node in visited:
                    continue
                visited.add(node)
                for i in range(len(node)):
                    nextNode = list(node)
                    flip(nextNode, i)
                    q.append(''.join(nextNode))
            steps += 1

        return -1
--------------------------------------------------------------------------------------------------
class Solution:
    def minFlips(self, mat: List[List[int]]) -> int:
        row_count, col_count = len(mat), len(mat[0])
        
        # 2d list -> 2d tuple
        def matrix_to_state(matrix):
            return tuple([tuple(row) for row in matrix])
        
        # 2d tuple -> 2d list
        def state_to_matrix(state):
            return [list(row) for row in state]
        
        # state -> state
        def flip(state, ri, ci):
            matrix = state_to_matrix(state)
            for tmp_ri, tmp_ci in [(ri, ci), (ri+1, ci), (ri-1, ci), (ri, ci+1), (ri, ci-1)]:
                if (0 <= tmp_ri < row_count) and (0 <= tmp_ci < col_count):
                    matrix[tmp_ri][tmp_ci] = 1 - matrix[tmp_ri][tmp_ci]
            return matrix_to_state(matrix)
    
        # state -> bool
        def is_goal_state(state):
            return all([cell == 0 for row in state for cell in row])
        
        # BFS
        q = [(matrix_to_state(mat), 0)]
        visited_states = set()
        for state, steps in q:
            if is_goal_state(state):
                return steps
            
            if state in visited_states:
                continue
            visited_states.add(state)
            
            # try flip each cell
            for flip_ri in range(row_count):
                for flip_ci in range(col_count):
                    next_state = flip(state, flip_ri, flip_ci)
                    q.append((next_state, steps + 1))
            
        return -1
      
