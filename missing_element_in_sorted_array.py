'''
Given an integer array nums which is sorted in ascending order and all of its elements are unique and given also an integer k, return the kth missing number starting from the leftmost number of the array.

 

Example 1:

Input: nums = [4,7,9,10], k = 1
Output: 5
Explanation: The first missing number is 5.
Example 2:

Input: nums = [4,7,9,10], k = 3
Output: 8
Explanation: The missing numbers are [5,6,8,...], hence the third missing number is 8.
Example 3:

Input: nums = [1,2,4], k = 3
Output: 6
Explanation: The missing numbers are [3,5,6,7,...], hence the third missing number is 6.
'''

I'm writing this because I saw a lot of comments by people being confused about the binary search boundries. Hopefully this will help clear it up.
As a general rule of thumb, before starting to write down your binary search code, you should know what exactly you are searching for. is it a specific number ? is it a range of numbers? I would argue for this question it's much easier to approach by looking at it's binary search solution as a range.

Heres what I mean:
For [4,7,9,10], our missing function will give out the values: [0,2,3,3]
IF we have K=1, meaning that we are looking for the 2nd missing number, by looking at the missing indices we can see that at index 0 we have no missing numbers and yet, at index 1, we have 2 missing numbers. so the number we are looking for, is defintely between the numbers of 4 and 7. In other words, (4,7) non-inclusive.

Now let's consider K=3. Using the same reasoning we can say that our missing number is in (7,9).

So all we need to do is to find a range of length 2 where we know our missing number is going to be in. Heres the binary search code which you might notice is a bit different than the Official solution and I would argue is easier to understand:

l = 0
r = len(nums)-1
while r-l>1 : # stop when size of the subarray is =2 ( r = l + 1 )
            mid = l + (r-l)//2
            x = missing(mid) 
            if x>=k:   # If at this index we have (for example) 5 missing numbers, and looking for the 3rd one, we know that our range is in the lower half. 
                r = mid
            elif x<k:   # If at this index we have (for example) 2 missing numbers, and looking for the 3rd one, we know that our range is in the upper half. 
                l = mid		
Why do we do r=mid if x==k ?
Let's say at index i we have 3 missing numbers and are looking for the 3rd one meaning x==k. If you think about it This still means that our missing number is on the left side and therefore we can limit our search to the left side of mid.

What happens after the binary search ends?
Because of our termination condition r-l>1 we will end up with a range of length two. In other words, l and r are going to be adjacent to eachother and mark the start and end of our range.
So we can use l (or even r if you want) to calculate the final answer. This part is exactly like the official solution so I wont get into it.

Why don't we do r=mid-1 and l=mid+1 ?
Because at each iteration we don't have enough information to decide whether we should remove mid or not. Feel free to try it out with some examples to make sure. No matter if missing(mid)>K or missing(mid)<K or missing(mid)=K, the element, mid itself might still end up being your l or r.

Here is the full code (Beats 96%):

    def missingElement(self, nums: List[int], k: int) -> int:
        l = 0
        r = len(nums)-1
        missing = lambda idx: nums[idx] - nums[0] - idx
        if k > missing(r) : return nums[-1]+k - missing(r)
        
        while r-l>1 :
            mid = l + (r-l)//2
            x = missing(mid) 
            if x>=k:
                r = mid
            elif x<k:
                l = mid
       
        return nums[l] + k - missing(l)
--------------------------------------------------------------------------------

# O(n) solution: ONe pass
class Solution:
    def missingElement(self, nums: List[int], k: int):
        for i in range(1, len(nums)):
            diff = nums[i] - nums[i-1] -1 
            if diff >= k:
                return nums[i-1] + k 
            else:
                k -= diff  
        return nums[-1] + k            

 
    
# O(log(n)) solution: binary search 
class Solution: 
       
    def missingElement(self, nums, k):
        def calculateMissings(i):
            return nums[i] - nums[0] - i
        
        left , right = 0,len(nums)
        
        while left < right:
            middle = (left + right)//2
            if calculateMissings(middle) < k: 
                left=middle + 1
            else:
                right=middle
            
        return nums[0]+k+left -1
-----------------------------------------------------------------------------

class Solution:
    def missingElement(self, nums: List[int], k: int) -> int:
        for i in range(1,len(nums)):
            if k <= nums[i] - nums[i-1] - 1:
                return nums[i-1] + k
            elif k > nums[i] - nums[i-1] - 1:
                k -= (nums[i] - nums[i-1] - 1)
        return nums[-1] + k
---------------------------------------------------------------------

class Solution:
    def missingElement(self, nums: List[int], k: int) -> int:
        diff = [a - b for a, b in zip(nums, range(nums[0], nums[0] + len(nums)))]
        i = bisect.bisect(diff, k-1)
        if i > len(nums) - 1:
            return nums[-1] + k - diff[-1]
        return list(range(nums[i-1]+1, nums[i]))[k-1-diff[i-1]]
----------------------------------------------------------------

class Solution:
    def missingElement(self, nums: List[int], k: int) -> int:
        if not nums:
            return k
        cur = nums[0]
        i=1
        while i < len(nums):
            diff = nums[i]-cur-1 
            if diff==k:
                return nums[i]-1
            elif k<diff:
                return cur+k
            else:
                k-=diff
                cur = nums[i]
            i+=1
        
        if k!=0:
            return cur+k
        return -1   
---------------------------------------------------------------------------

It exceeds the time limit but works in the real life.

Idea: create a list with missing elements. If provided k is not larger than the length of the list with missing elements, then return a respective element from the list. Otherwise, you need to calculate an "additional" element that goes beyond the provided list nums.

def missingElement(nums, k): 
        full = [i for i in range(nums[0], nums[-1] + 1)]
        missing = [j for j in full if j not in nums]
        if k <= len(missing):
            return missing[k - 1]
        else:
            return nums[-1] + 1 * (k - len(missing))
          
          
      
      
      
      
      
