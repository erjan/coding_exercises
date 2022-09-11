'''
Given an integer array nums, return the most frequent even element.

If there is a tie, return the smallest one. If there is no such element, return -1.
'''

class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        
        
        nums = list(filter(lambda x: x % 2 == 0, nums))

        if len(nums) == 0:
            return -1

        d = Counter(nums)

        freq = d.most_common(1)[0][1]
        print('freq is %d' % freq)

        res = float('inf')
        d = dict(d)
        print(d)

        for k, v in d.items():
            if v == freq:
                res = min(res, k)

        print(res)
        return res
---------------------------------------------------------
class Solution:
	def mostFrequentEven(self, nums):
		#Create a dictionary to store the frequency of each number
		freq = {}
		for i in nums:
			if i in freq:
				freq[i] += 1
			else:
				freq[i] = 1
		#Create a list of even numbers
		even = []
		for i in freq:
			if i % 2 == 0:
				even.append(i)
		#If there are no even numbers, return -1
		if len(even) == 0:
			return -1
		#Find the most frequent even number
		maxFreq = 0
		for i in even:
			if freq[i] > maxFreq:
				maxFreq = freq[i]
		#Create a list of the most frequent even numbers
		mostFreq = []
		for i in even:
			if freq[i] == maxFreq:
				mostFreq.append(i)
		#Return the smallest most frequent even number
		return min(mostFreq)
