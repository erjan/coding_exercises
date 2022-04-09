'''

Given an m x n picture consisting of black 'B' and white 'W' pixels and an integer target, return the number of black lonely pixels.

A black lonely pixel is a character 'B' that located at a specific position (r, c) where:

Row r and column c both contain exactly target black pixels.
For all rows that have a black pixel at column c, they should be exactly the same as row r.
'''

class Solution:
    def findBlackPixel(self, picture: List[List[str]], target: int) -> int:
        m, n = len(picture), len(picture[0])
        freq = defaultdict(int)
        rows = [0] * m
        cols = [0] * n
        for i in range(m): 
            for j in range(n): 
                if picture[i][j] == "B": 
                    rows[i] += 1
                    cols[j] += 1
            freq["".join(picture[i])] += 1
        
        ans = 0
        for i in range(m):
            key = "".join(picture[i])
            if freq[key] == target: 
                for j in range(n): 
                    if picture[i][j] == "B" and rows[i] == cols[j] == target: ans += 1
        return ans
