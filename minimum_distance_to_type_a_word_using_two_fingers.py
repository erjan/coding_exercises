'''
You have a keyboard layout as shown above in the X-Y plane, where each English uppercase letter is located at some coordinate.

For example, the letter 'A' is located at coordinate (0, 0), the letter 'B' is located at coordinate (0, 1), the letter 'P' is located at coordinate (2, 3) and the letter 'Z' is located at coordinate (4, 1).
Given the string word, return the minimum total distance to type such string using only two fingers.

The distance between coordinates (x1, y1) and (x2, y2) is |x1 - x2| + |y1 - y2|.

Note that the initial positions of your two fingers are considered free so do not count towards your total distance, also your two fingers do not have to start at the first letter or the first two letters.
'''


from functools import lru_cache
class Solution:
    def minimumDistance(self, word: str) -> int:
        dist=lambda a,b: (abs(a//6-b//6)+abs(a%6-b%6)) if a!=-1 else 0
        arr=[ord(char)-ord('A') for char in word]
        @lru_cache(None)
        def dfs(f1,f2,index):
            if index==len(word):
                return 0
            return min(dfs(f1,arr[index],index+1)+dist(f2,arr[index]),dfs(arr[index],f2,index+1)+dist(f1,arr[index]))
        
        return dfs(-1,-1,0)
      
--------------------------------------------------------------------------------------------------------------------------
class Solution:
    def minimumDistance(self, W: str) -> int:
        A, B, I, W = {(ord(W[0])-65,-1):0}, {}, math.inf, [ord(w)-65 for w in W]
        def dist(u,v): return abs(u//6 - v//6) + abs(u % 6 - v % 6)
        for w in W[1:]:
            for a in A:
                B[(w,a[1])] = min(B.get((w,a[1]),I), A[a] + dist(a[0],w))
                B[(a[0],w)] = min(B.get((a[0],w),I), A[a] + (a[1] != -1)*dist(a[1],w))
            A, B = B, {}
        return min(A.values())
		
		
