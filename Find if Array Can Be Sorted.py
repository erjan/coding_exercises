You are given a 0-indexed array of positive integers nums.

In one operation, you can swap any two adjacent elements if they have the same number of 
set bits
. You are allowed to do this operation any number of times (including zero).

Return true if you can sort the array, else return false.
-------------------------------------------------------------------------------------------------
my code:
class Solution:
    def canSortArray(self, nums: List[int]) -> bool:

        d = dict()

        for n in nums:

            numbits = str(bin(n)[2:]).count('1')

            if numbits not in d:
                d[numbits] = [n]
            else:
                d[numbits].append(n)
        
        for k,v in d.items():
            d[k] = sorted(d[k])
        
        d = [[k,v] for k,v in d.items()]

        for i in range(1,len(d)):
            prev = d[i-1]
            cur = d[i]

            if prev[-1]>cur[0]:
                return False
        return True
---------------------------------------------------------------------
class Solution:
    def canSortArray(self, nums: List[int]) -> bool:

        prevmax, curmin,curmax = 0,0,0
        prevBit = -1
        for x in nums:
            b = x.bit_count()
            if prevBit !=b:
                if curmin<prevmax: return False
                prevmax = curmax
                curmin,curmax = x,x
                prevBit = b
            else:
                curmin = min(curmin, x)
                curmax = max(curmax,x)
        return curmin>=prevmax

