'''
You are given a 0-indexed integer array nums. A pair of 
indices (i, j) is a bad pair if i < j and j - i != nums[j] - nums[i].

Return the total number of bad pairs in nums.
'''

def countBadPairs(self, nums: List[int]) -> int:
    return sum(x * (len(nums) - x) for x in Counter(i - num for i, num in enumerate(nums)).values()) // 2
  
----------------------------------------------------------------------------------------------------------------
class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        count=0
        n=len(nums)
        # for i in range(n):
        #     for j in range(i+1, n):
        #         if j-i!=nums[j]-nums[i]:
        #             count+=1
        # return count
        d={}
        for i in range(n):
            if nums[i]-i in d:
                count+=d[nums[i]-i]
                d[nums[i]-i]+=1
            else:
                d[nums[i]-i]=1

        return (n*(n-1)//2) - count
-------------------------------------------------------------------
def countBadPairs(self, nums: List[int]) -> int:
	good = 0
	n = len(nums)
	d = defaultdict(int)
	for i in range(n):
		if(nums[i]-i in d):
			good += d[nums[i]-i]
		d[nums[i]-i] += 1
	return (n*(n-1)//2) - good
