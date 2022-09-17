'''
Bob is standing at cell (0, 0), and he wants to reach destination: (row, column). He can only travel right and down. You are going to help Bob by providing instructions for him to reach destination.

The instructions are represented as a string, where each character is either:

'H', meaning move horizontally (go right), or
'V', meaning move vertically (go down).
Multiple instructions will lead Bob to destination. For example, if destination is (2, 3), both "HHHVV" and "HVHVH" are valid instructions.

However, Bob is very picky. Bob has a lucky number k, and he wants the kth lexicographically smallest instructions that will lead him to destination. k is 1-indexed.

Given an integer array destination and an integer k, return the kth lexicographically smallest instructions that will take Bob to destination.

 '''

from math import comb
class Solution:
    def kthSmallestPath(self, destination: List[int], k: int) -> str:
        i,j = destination
        
        @lru_cache(None)
        def helper(i,j,k):
            if k == 1:
                return "H"*j+"V"*i
            else:
                horizontal = comb(i+j-1,j-1)
                if k <= horizontal:
                    return "H" + helper(i,j-1,k)
                else:
                    return "V" + helper(i-1,j,k-horizontal)
        
        return helper(i,j,k)
      
----------------------------------------------------------------------------
class Solution:
    def kthSmallestPath(self, destination: List[int], k: int) -> str:
        
        m, n = destination
        base = ["H" for i in range(m+n)] 
        t = k-1 # num of instructions smaller than the kth smallest one
        v_left = m # how many "V" left to be put to the right side
        
        
        for i in range(m+n):
            if comb(m+n-i-1, v_left) <= t:
                base[i] = "V"
                t -= comb(m+n-i-1, v_left)
                v_left -= 1

                
            #if t == 0, that means the left "V" should all be put to the rightmost places
            if t == 0:
                for j in range(m+n-v_left, m+n):
                    base[j] = "V"
                break
        
        return "".join(base)
        
