'''
There is an m x n binary grid matrix with all the values set 0 initially. Design an algorithm to randomly pick an index (i, j) where matrix[i][j] == 0 and flips it to 1. All the indices (i, j) where matrix[i][j] == 0 should be equally likely to be returned.

Optimize your algorithm to minimize the number of calls made to the built-in random function of your language and optimize the time and space complexity.

Implement the Solution class:

Solution(int m, int n) Initializes the object with the size of the binary matrix m and n.
int[] flip() Returns a random index [i, j] of the matrix where matrix[i][j] == 0 and flips it to 1.
void reset() Resets all the values of the matrix to be 0.
 
 '''


class Solution:

    def __init__(self, m: int, n: int):
        self.rows = m
        self.cols = n
        self.flipped = set()

    def flip(self) -> List[int]:
        while True:
            i = random.randrange(self.rows)
            j = random.randrange(self.cols)
            if (i, j) not in self.flipped:
                self.flipped.add((i, j))
                return (i, j)

    def reset(self) -> None:
        self.flipped = set()
