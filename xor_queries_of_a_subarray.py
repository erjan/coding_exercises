'''
You are given an array arr of positive integers. You are also given the array queries where queries[i] = [lefti, righti].

For each query i compute the XOR of elements from lefti to righti (that is, arr[lefti] XOR arr[lefti + 1] XOR ... XOR arr[righti] ).

Return an array answer where answer[i] is the answer to the ith query.
'''

class Solution:
    def xorQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        for i in range(len(nums) - 1):
            nums[i + 1] ^= nums[i] 
        return [nums[j] ^ nums[i - 1] if i else nums[j] for i, j in queries]
      
------------------------------------------------------------------------------------------
class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        l=[]
        
        l.append(arr[0])
        
        for i in range(1,len(arr)):
            l.append(arr[i]^l[-1])
        res=[]
        for q in queries:
            
            if q[0]==0:
                res.append(l[q[1]])
            else:
                res.append(l[q[1]]^l[q[0]-1])
        return res
        
