'''
Given a collection of numbers, nums, that might contain duplicates, return all possible unique permutations in any order.
'''

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        
        return set(itertools.permutations(nums))
      
---------------------------------------------------------------------------------------------------------------------------------------
def permuteUnique(self, nums):
    res, visited = [], [False]*len(nums)
    nums.sort()
    self.dfs(nums, visited, [], res)
    return res
    
def dfs(self, nums, visited, path, res):
    if len(nums) == len(path):
        res.append(path)
        return 
    for i in xrange(len(nums)):
        if not visited[i]: 
            if i>0 and not visited[i-1] and nums[i] == nums[i-1]:  # here should pay attention
                continue
            visited[i] = True
            self.dfs(nums, visited, path+[nums[i]], res)
            visited[i] = False
----------------------------------------------------------------------------------------------------------
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        
        permutations = []
        counter = Counter(nums)
        def findAllPermutations(res):
            if len(res) == len(nums):
                permutations.append(res)
                return 
            
            for key in counter:
                if counter[key]:
                    counter[key]-=1 # decrement visited key
                    findAllPermutations(res + [key])    
                    counter[key]+=1 # restore the state of visited key to find the next path
                
        findAllPermutations([])
        return permutations
