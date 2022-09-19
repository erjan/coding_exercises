'''
A string originalText is encoded using a slanted transposition cipher to a string encodedText with the help of a matrix having a fixed number of rows rows.

originalText is placed first in a top-left to bottom-right manner.


The blue cells are filled first, followed by the red cells, then the yellow cells, and so on, until we reach the end of originalText. The arrow indicates the order in which the cells are filled. All empty cells are filled with ' '. The number of columns is chosen such that the rightmost column will not be empty after filling in originalText.

encodedText is then formed by appending all characters of the matrix in a row-wise fashion.
'''


class Solution:
    def decodeCiphertext(self, encodedText: str, rows: int) -> str:
        n = len(encodedText)
        res = []
        cols = n // rows
        
        for i in range(cols):
            for j in range(i, n, cols+1):
                res.append(encodedText[j])  # it is observed that skipping cols+1 from a given pos gives the required char
                
        return ''.join(res).rstrip(' ')  # removes trailing spaces from right
