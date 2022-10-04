'''
There is an integer array perm that is a permutation of the first n positive integers, where n is always odd.

It was encoded into another integer array encoded of length n - 1, such that encoded[i] = perm[i] XOR perm[i + 1]. For example, if perm = [1,3,2], then encoded = [2,1].

Given the encoded array, return the original array perm. It is guaranteed that the answer exists and is unique.
'''

class Solution:
    def decode(self, encoded: List[int]) -> List[int]:
        n = len(encoded)+1
        XOR = 0
        for i in range(1,n+1):
            XOR = XOR^i
        
        s = 0
        for i in range(1,n,2):
            s = s^encoded[i]
        res = [0]*n
        res[0] = XOR^s
        
        for j in range(1,n):
            res[j] = res[j-1]^encoded[j-1]
        return res
