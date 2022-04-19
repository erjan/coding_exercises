'''
Given an integer array nums and an integer k, you are asked to 
construct the array ans of size n-k+1 where ans[i] is the number 
of distinct numbers in the subarray nums[i:i+k-1] = [nums[i], nums[i+1], ..., nums[i+k-1]].

Return the array ans.
'''

Explanation
Count frequency of each character
Moving window from left to right
If frequency down to 0, cur (current count) decrease by 1
If frequency move from 0 to 1, cur (current count) increase by 1
Implementation
class Solution:
    def distinctNumbers(self, nums: List[int], k: int) -> List[int]:
        c = collections.Counter(nums[:k])
        cur = len(c)
        ans = [cur]
        for i in range(k, len(nums)):
            c[nums[i-k]] -= 1
            if c[nums[i-k]] == 0:
                cur -= 1
            if c[nums[i]] == 0:
                cur += 1
            c[nums[i]] += 1
            ans.append(cur)
        return ans
        
---------------------------------------------------------

start = 0
res = []
d = defaultdict(int)

for end in range(0,len(nums)):
	d[nums[end]] += 1   ## fill the dictionary with current window elements
	
	if end >= k-1:
		res.append(len(d))
		
		d[nums[start]] -= 1  ##to slide window, update the dictionary, decrease 1 from first element's value
		if d[nums[start]] == 0:  ##if first element's value becomes 0 then delete (key, value) pair
			del d[nums[start]]
		start = start+1  ##slide the window
			
return res
-----------------------------------------------------------------

class Solution:
    def distinctNumbers(self, nums: List[int], k: int) -> List[int]:
        ans = []
        freq = defaultdict(int)
        for i, x in enumerate(nums): 
            freq[x] += 1
            if i >= k: 
                freq[nums[i-k]] -= 1
                if freq[nums[i-k]] == 0: freq.pop(nums[i-k])
            if i+1 >= k: ans.append(len(freq))
        return ans
        
------------------------------------------------------------------------------------
The idea is to use a sliding window with a map for distinct elements in that window.
Specifically, that map will store the count of each distinct number within that window.

Update that map when incrementing the index, by reducing the count of the number that just passed outside the left of the window, and increasing the count of the number that just entered on the right.

The number of keys in this map gives the number of distinct elements in that window through len(windowMap), an O(1) operation.

        ret = []
		# initialize the window-map to map the first k nums; { num : count }
        windowMap = Counter(nums[:k]) 
		
		# intialize with the distinct number of elements in that first window 
        ret.append(len(windowMap)) 
        
		# for every window after, where the last left index is len(nums) - k
        for i in range(1, len(nums) - k + 1):
			# decrement the count of the number we passed
            windowMap[nums[i - 1]] -= 1 
			
			# if decremented to 0, delete from map so as not included in len()
            if windowMap[nums[i - 1]] == 0: 
                del windowMap[nums[i - 1]] 
				
			# increment the count number we just encountered
            windowMap[nums[i + k - 1]] += 1 
            
			# add the count of distinct elements (keys) in this window
			ret.append(len(windowMap))
            
        return ret
Since initialization is an O(k) operation, and each step of incrementing the sliding window is an O(1) operation performed n - k 
times, the time complexity is O(k + n - k) = O(n). The memory is the size of the map; O(k).
        
