'''
You are given a 0-indexed integer array nums. Initially on minute 0, the array is unchanged. Every minute, the leftmost element in nums is removed until no elements remain. Then, every minute, one element is appended to the end of nums, in the order they were removed in, until the original array is restored. This process repeats indefinitely.

For example, the array [0,1,2] would change as follows: [0,1,2] → [1,2] → [2] → [] → [0] → [0,1] → [0,1,2] → [1,2] → [2] → [] → [0] → [0,1] → [0,1,2] → ...
You are also given a 2D integer array queries of size n where queries[j] = [timej, indexj]. The answer to the jth query is:

nums[indexj] if indexj < nums.length at minute timej
-1 if indexj >= nums.length at minute timej
Return an integer array ans of size n where ans[j] is the answer to the jth query.

 

Example 1:

Input: nums = [0,1,2], queries = [[0,2],[2,0],[3,2],[5,0]]
Output: [2,2,-1,0]
Explanation:
Minute 0: [0,1,2] - All elements are in the nums.
Minute 1: [1,2]   - The leftmost element, 0, is removed.
Minute 2: [2]     - The leftmost element, 1, is removed.
Minute 3: []      - The leftmost element, 2, is removed.
Minute 4: [0]     - 0 is added to the end of nums.
Minute 5: [0,1]   - 1 is added to the end of nums.

At minute 0, nums[2] is 2.
At minute 2, nums[0] is 2.
At minute 3, nums[2] does not exist.
At minute 5, nums[0] is 0.
Example 2:

Input: nums = [2], queries = [[0,0],[1,0],[2,0],[3,0]]
Output: [2,-1,2,-1]
Minute 0: [2] - All elements are in the nums.
Minute 1: []  - The leftmost element, 2, is removed.
Minute 2: [2] - 2 is added to the end of nums.
Minute 3: []  - The leftmost element, 2, is removed.

At minute 0, nums[0] is 2.
At minute 1, nums[0] does not exist.
At minute 2, nums[0] is 2.
At minute 3, nums[0] does not exist.
'''

Let's make note of something before we start:

The length of the cycle is len(nums)*2, so queries at time t, t*len(nums)*2 ... t*len(nums)*2*n will be equal.
Let's set time %= len(nums)*2 for simplicity
There are two cases

The array is shrinking (or is empty) if 0 <= time <= len(nums):

At a given time, the new array is nums[time:] and is of length len(nums)-time. The element at position idx+time in the original array corresponds to the element at position idx in the new array, so nums[idx+time] == nums[time:][idx] if 0 <= idx+time < len(nums), else the query is out of bounds so we return -1.
The array is growing if len(nums) < time < 2*len(nums):

At a given time, the new array is nums[:time-len(nums)] and is of length time-len(nums). Since we are adding back elements in their original order, the element at idx in the original array equals the element at idx in the new array, as nums[idx] == nums[:time-len(nums)][idx] if 0 <= idx < time-len(nums), else the query is out of bounds so we return -1.
def elementInNums(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        def answerQuery(query):
            time, idx = query
            time %= len(nums)*2
            if time <= len(nums):
                return nums[idx+time] if 0 <= idx+time < len(nums) else -1
            else:
                return nums[idx] if 0 <= idx < time-len(nums) else -1
        
        return [answerQuery(query) for query in queries]
        
----------------------------------------------------------------
class Solution:
	def elementInNums(self, nums: List[int], queries: List[List[int]]) -> List[int]:
		n = len(nums)
		matrix = [[] for i in range(n * 2 + 1)]
		res = []
		for i in range(len(nums)):
			matrix[i] = nums[i:] + [-1] * i
			matrix[len(matrix) - 1 - i] = nums[:n - i] + [-1] * i
		matrix[n] = [-1] * n
		for time, index in queries:
			res.append(matrix[time % (len(matrix) - 1)][index])
		return res
--------------------------------------------------------------------------------------------------
class Solution:
    def elementInNums(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        cycle = len(nums)*2
        output = []
        for minute,idx in queries:
            minute %= cycle
            if minute < len(nums):
                rotated = nums[minute:]
            else:
                minute%=len(nums)
                rotated = nums[:minute]
            
            if len(rotated)>idx:
                result = rotated[idx]
            else:
                result = -1
            output.append(result)
        return output
        
----------------------------------------------------
class Solution:
    def elementInNums(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        N = len(nums)
        cycle = 2 * N # 2 * N is a cycle for the next full list
        ans = []
        for t, idx in queries:
            t = t % cycle
            if t <= N:
                l = N - t
            else:
                l = t - N
            if idx >= l:
                ans.append(-1)
            elif t < N:
                ans.append(nums[idx + N - l])
            else:
                ans.append(nums[idx])
        return ans
        
    
