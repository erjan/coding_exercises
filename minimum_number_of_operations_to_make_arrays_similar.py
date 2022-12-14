'''
You are given two positive integer arrays nums and target, of the same length.

In one operation, you can choose any two distinct indices i and j where 0 <= i, j < nums.length and:

set nums[i] = nums[i] + 2 and
set nums[j] = nums[j] - 2.
Two arrays are considered to be similar if the frequency of each element is the same.

Return the minimum number of operations required to make nums similar to target. The test cases are generated such that nums can always be similar to target.
'''

class Solution:
    def makeSimilar(self, nm: List[int], tg: List[int]) -> int:
        nm.sort()
        tg.sort()
        p=0
        nme=[]
        nmo=[]
        for a in nm:
            if(a%2==0):
                nme.append(a)
            else:
                nmo.append(a)
        tge=[]
        tgo=[]
        for a in tg:
            if(a%2==0):
                tge.append(a)
            else:
                tgo.append(a)
        for i in range(len(tgo)):
            if(tgo[i]-nmo[i]>0):
                p+=tgo[i]-nmo[i]
        for i in range(len(tge)):
            if(tge[i]-nme[i]>0):
                p+=tge[i]-nme[i]
        return p//2
      
---------------------------------------------------------------------------------- 
class Solution:
    def makeSimilar(self, A, B):
        A1 = sorted(a for a in A if a % 2)
        B1 = sorted(a for a in B if a % 2)
        A2 = sorted(a for a in A if a % 2 == 0)
        B2 = sorted(a for a in B if a % 2 == 0)
        res1 = sum(abs(a - b) // 2 for a,b in zip(A1, B1))
        res2 = sum(abs(a - b) // 2 for a,b in zip(A2, B2))
        return (res1 + res2) // 2
