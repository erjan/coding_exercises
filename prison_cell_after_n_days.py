'''
There are 8 prison cells in a row and each cell is either occupied or vacant.

Each day, whether the cell is occupied or vacant changes according to the following rules:

If a cell has two adjacent neighbors that are both occupied or both vacant, then the cell becomes occupied.
Otherwise, it becomes vacant.
Note that because the prison is a row, the first and the last cells in the row can't have two adjacent neighbors.

You are given an integer array cells where cells[i] == 1 if the ith cell is occupied and cells[i] == 0 if the ith cell is vacant, and you are given an integer n.

Return the state of the prison after n days (i.e., n such changes described above).
'''

class Solution:
    def prisonAfterNDays(self, cells: List[int], N: int) -> List[int]:
        def nextday(cells):
            next_day_cells = [0] *len(cells)
            for i in range(1,len(cells)-1):
                if cells[i-1] == cells[i+1]: 
                        next_day_cells[i] = 1
                else:
                        next_day_cells[i] = 0
            return next_day_cells
        
        seen = {}
        while N > 0:
            c = tuple(cells)
            if c in seen:
                N %= seen[c] - N
            seen[c] = N

            if N >= 1:
                N -= 1
                cells = nextday(cells)

        return cells
      
---------------------------------------------------------
class Solution:
    def prisonAfterNDays(self, cells: List[int], N: int) -> List[int]:
        
        def nextDay(cells):
            mask = cells.copy()
            for i in range(1, len(cells) - 1):
                if mask[i-1] ^ mask[i+1] == 0:
                    cells[i] = 1
                else:
                    cells[i] = 0
            cells[0] = 0
            cells[-1] = 0   
            return cells
        
        day1 = tuple(nextDay(cells))
        N -= 1
        count = 0
        
        while N > 0:
            day = tuple(nextDay(cells))
            N -= 1
            count += 1
            
            if day == day1:
                N = N % count
        return cells
      
--------------------------------------------------------------------------
class Solution(object):
    def prisonAfterNDays(self, cells, N):
        """
        :type cells: List[int]
        :type N: int
        :rtype: List[int]
        """
        def next(state):
            return tuple([1 if i>0 and i<len(state)-1 and state[i-1] == state[i+1] else 0 for i in range(len(state))])
        
        seen = {}
        state = tuple(cells)
        i = 0
        remaining = 0
        while i < N:
            if state in seen:
                cycle = i - seen[state]
                remaining = (N-i)%cycle
                break
            seen[state] = i
            state = next(state)
            i+=1
        
        while remaining > 0:
            state = next(state)
            remaining-=1
        return state
