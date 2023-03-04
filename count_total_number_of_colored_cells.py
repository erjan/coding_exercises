'''
There exists an infinitely large two-dimensional grid of uncolored unit cells. You are given a positive integer n, indicating that you must do the following routine for n minutes:

At the first minute, color any arbitrary unit cell blue.
Every minute thereafter, color blue every uncolored cell that touches a blue cell.
Below is a pictorial representation of the state of the grid after minutes 1, 2, and 3.
'''





'''
Approach
n*n: This calculates the number of cells in a square grid of size n by n. This is the number of cells that will be colored.

(n-1)(n-1): This calculates the number of cells that will be colored by the diagonals of the grid. Each diagonal consists of n-1 cells, so there are n-1 diagonals in each direction (horizontal and vertical). The total number of cells colored by the diagonals is therefore (n-1)(n-1).

nn + (n-1)(n-1): This adds the number of cells colored by the diagonals to the number of cells in the grid to get the total number of colored cells.

The final result is returned as an integer value.

So, in summary, the function coloredCells calculates the total number of cells that will be colored in a square grid of size n, where the cells are colored in a diagonal pattern as well.

The time complexity of the given algorithm is O(1) as the calculations involved are basic arithmetic operations that take constant time. Similarly, the space complexity of the algorithm is also O(1) as we are not using any additional data structure.
'''

class Solution:
    def coloredCells(self, n: int) -> int:
        return n*n + (n-1)*(n-1)
