'''
Given an array arr of positive integers sorted in a strictly increasing order, and an integer k.

Find the kth positive integer that is missing from this array.
'''


class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        
        s1 = list( i for i in range(1,1001))

        counter = 0
        
        a = arr
        for i in range(len(s1)):
            if s1[i] not in a:
                counter+=1
                if k == counter:
                    return s1[i]
                
        if k > counter:
            return len(arr) + k
