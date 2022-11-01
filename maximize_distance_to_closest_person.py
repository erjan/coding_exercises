'''
You are given an array representing a row of seats where seats[i] = 1 represents a person sitting in the ith seat, and seats[i] = 0 represents that the ith seat is empty (0-indexed).

There is at least one empty seat, and at least one person sitting.

Alex wants to sit in the seat such that the distance between him and the closest person to him is maximized. 

Return that maximum distance to the closest person.
'''


class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        n = len(seats)
        empty, result, idx1, idx2 = 0, 0, -1, -1
        
        for i in range(n):
            if seats[i] == 1:
                empty = 0
                if idx1 == -1: idx1 = i
                idx2 = i
            else:
                empty += 1
                result = max(result, (empty+1)//2)
        result = max(result, idx1, n-1-idx2)
        return result
----------------------------------------------------------------------------------------------------------------------

class Solution(object):
    def maxDistToClosest(self, seats):
        pre_zeros, suf_zeros, max_zeros, zeros = -1, -1, -1, 0
        for seat in seats:
            if seat == 0: zeros += 1
            else:
                if pre_zeros == -1: 
                    pre_zeros = zeros
                else:
                    max_zeros = max(max_zeros, zeros)
                zeros = 0
        suf_zeros = zeros
        return max(pre_zeros, suf_zeros, (max_zeros + 1) // 2)
