'''
A triplet is an array of three integers. You are given a 2D integer array triplets, where triplets[i] = [ai, bi, ci] describes the ith triplet. You are also given an integer array target = [x, y, z] that describes the triplet you want to obtain.

To obtain target, you may apply the following operation on triplets any number of times (possibly zero):

Choose two indices (0-indexed) i and j (i != j) and update triplets[j] to become [max(ai, aj), max(bi, bj), max(ci, cj)].
For example, if triplets[i] = [2, 5, 3] and triplets[j] = [1, 7, 5], triplets[j] will be updated to [max(2, 1), max(5, 7), max(3, 5)] = [2, 7, 5].
Return true if it is possible to obtain the target triplet [x, y, z] as an element of triplets, or false otherwise.
'''


class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        a, b, c = target
        maxi, maxj, maxk = 0, 0, 0
        
        for i, j, k in triplets:
            if i <= a and j <= b and k <= c:
                maxi = max(maxi, i)
                maxj = max(maxj, j)
                maxk = max(maxk, k)
                
        return maxi == a and maxj == b and maxk == c
      
------------------------------------------------------------------------------------------------------------

class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        i = 1
        cur = []
        for a,b,c in triplets:
            if a<=target[0] and b<=target[1] and c<= target[2]:
                cur = [a,b,c]
                break
        if not cur:
            return False
        while i<len(triplets):
            if cur == target:
                return True
            a,b,c = triplets[i]
            x,y,z = cur
            if max(a,x)<=target[0] and max(b,y)<=target[1] and max(c,z)<=target[2]:
                cur = [max(a,x), max(b,y), max(c,z)]
               
            
            i+= 1
        if cur == target:
            return True
        return False
      
----------------------------------------------------------------------------------------------------------------------------      
