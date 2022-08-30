'''
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.
'''

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = Counter(nums)

        res = [k for k, v in d.most_common(k)]

        return res
        
------------------------------------------------------------------------------------
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        if  len(nums)  == 1:
            return [nums[0]]
    
        
        d = dict(Counter(nums))
        
        h = []
        
        for key in d:
            
            heappush(h, (d[key], key))
            if len(h) > k:
                heappop(h)
        
        res = []
        while h:
            _, item = heappop(h)
            res.append(item)
        return res

        
---------------------------------------------------------------------------------
class Solution:
	def topKFrequent(self, nums: List[int], k: int) -> List[int]:

		frequency = {}

		for num in nums:

			if num not in frequency:

				frequency[num] = 1

			else:

				frequency[num] = frequency[num] + 1

		frequency = dict(sorted(frequency.items(), key=lambda x: x[1], reverse=True))

		result = list(frequency.keys())[:k]

		return result
    
----------------------------------------------------------------------------------------------
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_table = {}
        for i in nums:
            freq_table[i] = freq_table.get(i, 0) + 1
        heap = []
        for i in freq_table.keys():
            if len(heap) == k: # If size is k then we dont want to increase the size further 
                heappushpop(heap, (freq_table[i], i))
            else: # Size is not k then freely push values
                heappush(heap, (freq_table[i], i))
		# After this operation the heap contains only k largest values of all the values in nums
        ans = []
        while k > 0:
            k -= 1
            ans.append(heappop(heap)[1])
        return ans
    
----------------------------------
class Solution:
    def topKFrequent(self, nums, k) :
        map=Counter(nums) # counter is used to count the frequency of each element
        result=[]
        for key,value in map.items():
            result.append([key,value])
        result.sort(key=lambda x:x[1],reverse=True) # sort with respect to the second element in the list
        return [x[0] for x in result[:k]] # return the first k elements in the list
