'''
You are given an integer array nums and two integers limit and goal. The array nums has an interesting property that abs(nums[i]) <= limit.

Return the minimum number of elements you need to add to make the sum of the array equal to goal. The array must maintain its property that abs(nums[i]) <= limit.

Note that abs(x) equals x if x >= 0, and -x otherwise.
'''

Get target number by substracting from total sum of array to the goal
2. Since target can be postive or negative
3. Let take an example 10//3=3 and -10//3=-4 in Python
4. So take absolute of Target number
5. Add the quotient to the answer
6. If there is remainder then add 1 to the answer as remainder is less than limit otherwise no need to add


class Solution:
    def minElements(self, nums: List[int], limit: int, goal: int) -> int:
        s=sum(nums)
        target=goal-s
        ans=0
    
        ans+=abs(target)//limit
        if abs(target)%limit!=0:
            ans+=1
        return ans
