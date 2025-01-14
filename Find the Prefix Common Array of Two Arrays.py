'''
You are given two 0-indexed integer permutations A and B of length n.

A prefix common array of A and B is an array C such that C[i] is equal to the count of numbers that are present at or before the index i in both A and B.

Return the prefix common array of A and B.

A sequence of n integers is called a permutation if it contains all integers from 1 to n exactly once.
'''


class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        a = set()
        b = set()
        ans = []
        count = 0
        for i in range(0, len(A)):
            a.add(A[i])
            b.add(B[i])
            if A[i] == B[i]:
                count += 1
                ans.append(count)
                continue
            if A[i] in b:
                count += 1
            if B[i] in a:
                count += 1
            ans.append(count)
        return ans

-----------------------------------------------------------------------------------
class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        n  = len(A)

        freq = [ [0*n]  for _ in range(n)]
        
        res = [0]*n
        for i in range(1,n+1):
            prefA = A[:i]
            prefB = B[:i]

            p1 = set(prefA)
            p2 = set(prefB)

            
                  
            res[i-1] =  len(p1.intersection(p2))

        return res
