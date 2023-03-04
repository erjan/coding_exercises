'''
You are given a 2D integer array ranges where ranges[i] = [starti, endi] denotes that all integers between starti and endi (both inclusive) are contained in the ith range.

You are to split ranges into two (possibly empty) groups such that:

Each range belongs to exactly one group.
Any two overlapping ranges must belong to the same group.
Two ranges are said to be overlapping if there exists at least one integer that is present in both ranges.

For example, [1, 3] and [2, 5] are overlapping because 2 and 3 occur in both ranges.
Return the total number of ways to split ranges into two groups. Since the answer may be very large, return it modulo 109 + 7.
'''






'''
First we sort ranges
Then we are counting numberOfGroups by merging ranges.

Finally we count answer
If group is going into FIRST -> assign 0
If group is going into SECOND -> assign 1

This means that the answer is power of 2.
'''


from itertools import permutations
class Solution:
    def countWays(self, ranges: List[List[int]]) -> int:
        
        
        intervals = sorted(ranges, key=lambda x: x[0])
        res = [intervals[0]]

        for cur in intervals[1:]:
            if cur[0] <= res[-1][1]:
                res[-1][1] = max(cur[1],res[-1][1])
            else:
                res.append(cur)
        

    
        tr = 10**9+7

        l = len(res)

        res = pow(2, len(res), tr)
        return res

------------------------------------------------------------------------------------------------        
        
class Solution:
    def countWays(self, ranges: List[List[int]]) -> int:
        ranges.sort()
        A,B=-1,-1 # Artificial first Range, smallest non-Overlapping
        numberOfGroups=0
        for a,b in ranges:
            if B<a:
                # starting New Group
                numberOfGroups+=1
                A,B=a,b
            else:
                # same Group
                B=max(B,b)
        return pow(2,numberOfGroups,10**9+7)      
