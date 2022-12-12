'''
Given a m * n matrix seats  that represent seats distributions in a classroom. If a seat is broken, it is denoted by '#' character
otherwise it is denoted by a '.' character.

Students can see the answers of those sitting next to the left, right, upper left and upper right, but he cannot 
see the answers of the student sitting directly in front or behind him. Return the maximum number of 
students that can take the exam together without any cheating being possible..

Students must be placed in seats in good condition.
'''


class Solution:
    def maxStudents(self, seats: List[List[str]]) -> int:
        m, n = len(seats), len(seats[0]) # dimensions 
        
        valid = []
        for i in range(m): 
            val = 0
            for j in range(n): 
                if seats[i][j] == ".": val |= 1 << j 
            valid.append(val)
        
        @cache
        def fn(i, mask): 
            """Return max students taking seats[i:] given previous row as mask."""
            if i == len(seats): return 0 
            ans = fn(i+1, 0)
            for x in range(1 << n): 
                if x & valid[i] == x and (x >> 1) & x == 0 and (mask >> 1) & x == 0 and (mask << 1) & x == 0: 
                    ans = max(ans, bin(x).count("1") + fn(i+1, x))
            return ans 
        
        return fn(0, 0)
      
-----------------------------------------------------------------------------------------------------------------
# bitmask dp
# dp[i][mask]: maximum students in seats[:i+1] with valid mask in seats[i]
# dp[i][mask] = max(dp[i-1][mask'] + valid bit(mask))
# no adjacent students: x&(x>>1) == 0
# student on good seat: x&y == x                            (y = bit(seats[i]))
# can't see front guys: x&(y>>1) == 0 and (x>>1)&y == 0     (y = pre_mask)

class Solution:
    def maxStudents(self, seats: List[List[str]]) -> int:
        m, n = len(seats), len(seats[0])
        dp = [collections.defaultdict(int) for _ in range(m+1)]
        dp[-1][0] = 0
        
        bits = []
        for row in seats:
            num = 0
            for i in range(n):
                num += (row[i]=='.')<<n-1-i
            bits.append(num)
        # print(bits)
        
        for i in range(m):
            for x in range(2**n):
                for y in dp[i-1]:
                    if x&(x>>1) == 0 and x&bits[i] == x and x&(y>>1) == 0 and (x>>1)&y == 0:
                        dp[i][x] = max(dp[i][x], dp[i-1][y] + bin(x).count('1'))
        
        return max(dp[m-1][x] for x in dp[m-1])




















