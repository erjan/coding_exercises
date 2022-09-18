
'''
You are given two integers m and n, which represent the dimensions of a matrix.

You are also given the head of a linked list of integers.

Generate an m x n matrix that contains the integers in the linked list presented in spiral order (clockwise), starting from the top-left of the matrix. If there are remaining empty spaces, fill them with -1.

Return the generated matrix.
'''

class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        r, c = 0, 0
        xr, xc = 0, 1
        
        matrix = [[-1 for _ in range(n)] for _ in range(m)]
        while head:
            matrix[r][c] = head.val
            
            # Conditions to swap the direction
            if r + xr < 0 or r + xr >= m or c + xc < 0 or c + xc >= n or matrix[r+xr][c+xc] != -1:
                xr, xc = xc, -xr
            
            r += xr
            c += xc
            head = head.next
        
        return matrix
      
---------------------------------------------------------------------------------------------------------


class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        result = [ [-1] * n for _ in range(m) ]
        node = head
        
        
        
        UP = 2
        DOWN = 3
        LEFT = 1
        RIGHT = 0
        
        directions = ( (0,1), (0,-1), (-1,0), (1,0))
        direction = RIGHT
        
        uB, dB, lB, rB = 0, m-1, 0, n-1
        row, col = 0, 0

        while node:
            result[row][col] = node.val 
            node = node.next 

            if direction == RIGHT and col == rB and row != dB:
                direction = DOWN
                uB += 1
            

            if direction == DOWN and col == rB and row == dB:
                direction = LEFT
                rB -= 1
                
            if direction == LEFT and col == lB and row != uB:
                direction = UP
                dB -= 1
                
            if direction == UP and col == lB and row == uB:
                direction = RIGHT
                lB += 1
            
            dr,dc = directions[direction]
            row,col = row+dr, col+dc

        return result
