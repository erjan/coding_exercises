'''
You are given a 0-indexed integer array nums and an integer pivot. Rearrange nums such that the following conditions are satisfied:

Every element less than pivot appears before every element greater than pivot.
Every element equal to pivot appears in between the elements less than and greater than pivot.
The relative order of the elements less than pivot and the elements greater than pivot is maintained.
More formally, consider every pi, pj where pi is the new position of the ith element and pj is the new position of the jth element. For elements less than pivot, if i < j and nums[i] < pivot and nums[j] < pivot, then pi < pj. Similarly for elements greater than pivot, if i < j and nums[i] > pivot and nums[j] > pivot, then pi < pj.
Return nums after the rearrangement.
'''

class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        
        
        before = list(filter(lambda x: x < pivot, nums))

        equal = list(filter(lambda x: x == pivot, nums))
        after = list(filter(lambda x: x > pivot, nums))


        nums = before + equal + after
        print(nums)
        return nums

    
--------------------------------------------------------------------------------------------------
class Solution:
	def pivotArray(self, nums: List[int], pivot: int) -> List[int]:

		ans=[]

		nums.remove(pivot)

		i=0
		ans.append(pivot)

		for j in nums:
			if j<pivot:
				ans.insert(i,j)
				i=i+1
			elif j==pivot:
				ans.insert(i+1,j)
			else:
				ans.append(j)

		return ans
