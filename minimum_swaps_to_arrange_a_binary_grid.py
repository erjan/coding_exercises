'''
Given an n x n binary grid, in one step you can choose two adjacent rows of the grid and swap them.

A grid is said to be valid if all the cells above the main diagonal are zeros.

Return the minimum number of steps needed to make the grid valid, or -1 if the grid cannot be valid.

The main diagonal of a grid is the diagonal that starts at cell (1, 1) and ends at cell (n, n).
'''


class Solution:
    def minSwaps(self, grid: List[List[int]]) -> int:
        # find the number of tailing zero of each row
        zero, n = [], len(grid)
        for row in grid:
            tmp = 0
            while row and row.pop() == 0:
                tmp += 1
            zero.append(tmp)

        # similar to insertion sort
        res = 0
        for i in range(n):
            # skip since satisfies
            if zero[i] >= n-i-1:
                continue
            # find the closest valid one
            for j in range(i+1, n):
                if zero[j] >= n-i-1:
                    break
            # check if zero[j] is valid
            if zero[j] < n-i-1:
                return -1
            # insert step, move [i:j] one index forward
            zero[i+1:j+1] = zero[i:j]
            # add number of moves
            res += j-i
        return res
      
-------------------------------------------------------------------------------
class Solution:
    def minSwaps(self, grid: List[List[int]]) -> int:
        lenth=len(grid)
        zeros=[0]*lenth
        for i in range(lenth):
            row=grid[i]
            for j in range(lenth):
                if row[-j-1]==0:
                    zeros[i]=j+1
                else:
                    break
        
        
        count=0
        
        for i in range(lenth):
            print(zeros)
            if zeros[i]<lenth-1-i:
                
                did=0
                for next in range(lenth-i-1):
                    if zeros[i+next+1]>=lenth-1-i:
                        did=1
                        k=i+next+1
                        while k - i >0:
                            count+=1
                            zeros[k],zeros[k-1] =zeros[k-1],zeros[k]
                            k-=1
                        break
                        
                if did==0:
                    return -1
        return count
      
----------------------------------------------------------------------------------------------------------
class Solution:
    def minSwaps(self, grid) -> int:
        """
        This program computes the minimum number of swaps of adjacent
        rows that will create a valid grid. A grid is valid when all
        cells above the main diagonal are 0.

        :param grid: binary square matrix (0's and 1's)
        :type grid: list[list[int]]
        :return: minimum number of swaps needed to create valid grid
                 (all cells above the diagonal are 0)
        :rtype: int
        """

        """
        Initialize:
        - length of grid (length)
        - number of swaps (swaps) is the eventual answer
        - number of zeros (zeros) we are looking for in the current
          row above the diagonal
        - first index above the diagonal (start) in the current row
        """
        length = len(grid)
        swaps = 0
        zeros = length - 1
        start = 1

        """
        Determine minimum number of swaps needed to create valid grid.
        - In order for it to be possible to create a valid grid where
          the length of each row is length, there must exist a row that
          ends with length - 1 zeros, a row that ends with length - 2
          zeros, and so on down to one zero.
        - In the first pass through the while loop, search for the
          first row that ends with length - 1 zeros. Count the number
          of swaps needed to move the row to the top row of the grid.
          Remove the row from the current location. Since we do not
          examine this row again, there is no need to insert it at the
          top of the grid.
        - Repeat for the next pass, but decrement the number of zeros.
        - Continue until the number of zeros is 1 or no row is found
          that meets the qualification for a valid matrix.
        - If it is possible to create a valid matrix, return the
          total number of swaps. Otherwise, return -1.
        """
        while zeros > 0:
            swapped = False
            for k in range(length):
                if sum(grid[k][start:]) == 0:
                    swaps += k
                    grid.remove(grid[k])
                    swapped = True
                    zeros -= 1
                    start += 1
                    break
            if not swapped:
                return -1
            else:
                length -= 1
        return swaps
