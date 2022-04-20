'''
Given a binary array nums, return the maximum number of consecutive 1's in the array if you can flip at most one 0.

 

Example 1:

Input: nums = [1,0,1,1,0]
Output: 4
Explanation: Flip the first zero will get the maximum number of consecutive 1s. After flipping, the maximum number of consecutive 1s is 4.
Example 2:

Input: nums = [1,0,1,1,0,1]
Output: 4
 

Constraints:

1 <= nums.length <= 105
nums[i] is either 0 or 1.
 

Follow up: What if the input numbers come in one by one as an infinite stream? In other words, you can't store all numbers coming from the stream as it's too large to hold in memory. Could you solve it efficiently?
'''


 def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = temp = 0
        flipped = -1 #remebers the last flipped position
        for i,v in enumerate(nums):
            if v == 1:
                temp += 1
            elif flipped == -1:
                flipped = i
                temp += 1
            else:
                temp = i - flipped # start right after the last flipped position
                flipped = i # setting current zero's position as new flipped position
            count = max(count, temp)
        return count
I hope that you've found the solution useful.
In that case, please do upvote and encourage me to on my quest to document all leetcode problems😃
PS: Search for mrmagician tag in the discussion, if I have solved it, You will find it there😸
  
----------------------------------------------------

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        before = True
        beforeCount = 0
        afterCount = 0
        maxCount = 0

        for i in range(len(nums)):
            if nums[i] == 1 and before:
                beforeCount += 1
            elif nums[i] == 1 and not before:
                afterCount += 1
            elif nums[i] == 0 and before:
                beforeCount += 1
                before = False
            elif nums[i] == 0 and not before:
                currentCount = beforeCount + afterCount
                maxCount = max(currentCount, maxCount)

                beforeCount = afterCount + 1
                afterCount = 0
                before = False

        currentCount = beforeCount + afterCount
        maxCount = max(currentCount, maxCount)

        return maxCount
----------------------------------------------------

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        '''
        need a varialble for store if we use flip
        or two variable:
        - one store with flip
        - another store without flip
        if meet a zero
        withflip = without flip + 1
        withoutflip = 0
        if cur == 1:
            withflip+=1
            withoutflip+=1
        else:
            withflip = 1+withoutflip
            withoutflip = 0
        '''
        maxx = 1
        withf = 0
        withoutf = 0
        for n in nums:
            if n:
                withf+=1
                withoutf+=1
            else:
                withf = withoutf + 1
                withoutf = 0
            if withf>maxx:
                maxx = withf
        return maxx
      
-------------------------------------------------------------

1: stringify list
2: split list by '0'
3: make a list that has length of consecutive 1.

Let's guess nums are [1,1,1,1,1,0,0,1,1,0,1,1,1,1]
Following above steps
[1,1,1,1,1,0,0,1,1,0,1,1,1,1] -> "11111001101111" -> ["11111","","11","1111"] -> [5,0,2,4]

Last, use zip to get length sums of two adjecent of 1.

def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
    t = list(map(len, (''.join(map(str,nums))).split('0')))
    return max([a+b+1 for a,b in zip(t, t[1:])]) if len(t)>1 else len(nums)
----------------------------------------------------------

Algo
Define a slideing window from ii to i in which at most one 0 can exist.

Implementation

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        ans = cnt = ii = 0
        for i, x in enumerate(nums): 
            cnt += 1 - nums[i]
            while cnt > 1: 
                cnt -= 1 - nums[ii]
                ii += 1
            ans = max(ans, i - ii + 1)
        return ans 
Analysis
Time complexity O(N)
Space complexity O(1)

To answer the follow-up, we have to alter the algo as the sliding window approach needs to store the whole array. Here, we use two numbers prev and curr to store the lengths of the most revent two consecutive 1's (seperated by one 0).

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        ans = curr = 0
        prev = -1
        for x in nums: 
            if x == 0: prev, curr = curr, 0
            else: curr += 1
            ans = max(ans, prev + 1 + curr)
        return ans 
----------------------------------------------------------------------------------------------------      
      
      
