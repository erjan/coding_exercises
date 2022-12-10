'''
You are given an integer array arr.

We split arr into some number of chunks (i.e., partitions), and individually 
sort each chunk. After concatenating them, the result should equal the sorted array.

Return the largest number of chunks we can make to sort the array.
'''

class Solution:
	def maxChunksToSorted(self, arr: list[int]) -> int:
		max_chunk = 0

		min_left_i = [float('inf')]*(len(arr)+1)
		curr_min = math.inf

		# find the 
		for i in range(len(arr)-1, -1, -1):
			if arr[i] < curr_min:
				curr_min = arr[i]
			min_left_i[i] = curr_min


		max_till_i = arr[0]
		for i in range(len(arr)):
			if arr[i] > max_till_i:
				max_till_i = arr[i]

			# check to verify if there is no element to the right which is lower than the current.
			if max_till_i <= min_left_i[i+1]:
				max_chunk += 1

		return max_chunk
  
--------------------------------------------------------------------------------------------------------
class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        stack=[]
        for v in arr:
            maxVal=-float('inf')
            while stack and stack[-1]>v:
                maxVal=max(maxVal,stack.pop())
            stack.append(max(v,maxVal))
        return len(stack)
