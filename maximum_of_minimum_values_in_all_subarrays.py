'''
You are given an integer array nums of size n. You are asked to solve n queries for each integer i in the range 0 <= i < n.

To solve the ith query:

Find the minimum value in each possible subarray of size i + 1 of the array nums.
Find the maximum of those minimum values. This maximum is the answer to the query.
Return a 0-indexed integer array ans of size n such that ans[i] is the answer to the ith query.

A subarray is a contiguous sequence of elements in an array.

 

Example 1:

Input: nums = [0,1,2,4]
Output: [4,2,1,0]
Explanation:
i=0:
- The subarrays of size 1 are [0], [1], [2], [4]. The minimum values are 0, 1, 2, 4.
- The maximum of the minimum values is 4.
i=1:
- The subarrays of size 2 are [0,1], [1,2], [2,4]. The minimum values are 0, 1, 2.
- The maximum of the minimum values is 2.
i=2:
- The subarrays of size 3 are [0,1,2], [1,2,4]. The minimum values are 0, 1.
- The maximum of the minimum values is 1.
i=3:
- There is one subarray of size 4, which is [0,1,2,4]. The minimum value is 0.
- There is only one value, so the maximum is 0.
Example 2:

Input: nums = [10,20,50,10]
Output: [50,20,10,10]
Explanation:
i=0:
- The subarrays of size 1 are [10], [20], [50], [10]. The minimum values are 10, 20, 50, 10.
- The maximum of the minimum values is 50.
i=1:
- The subarrays of size 2 are [10,20], [20,50], [50,10]. The minimum values are 10, 20, 10.
- The maximum of the minimum values is 20.
i=2:
- The subarrays of size 3 are [10,20,50], [20,50,10]. The minimum values are 10, 10.
- The maximum of the minimum values is 10.
i=3:
- There is one subarray of size 4, which is [10,20,50,10]. The minimum value is 10.
- There is only one value, so the maximum is 10.
'''



Approach #1 Naive Nested Loop
Explanation
In this approach, we essentially compare the minimum values for each window size from (1 to n). See comments below, it should be straightforward.
Obviously, such a naive approach will lead to a TLE for medium question like this one.
Time Complexity: O(N*N)
Implementation
class Solution:
    def findMaximums(self, nums: List[int]) -> List[int]:
        cur_nums = nums[:]
        n = len(nums)
        ans = [0] * n
        for i in range(n):                    # for each window size
            cur_ans = 0
            for j in range(n-i):              # compare and find the maximum among all minimum values
                cur = cur_nums[j]
                cur = min(cur, nums[j + i])   # get the minimum of current window size at index `j`
                cur_nums[j] = cur
                cur_ans = max(cur_ans, cur)   # compare to get the maximum
            ans[i] = cur_ans
        return ans
Approach #2 Mono-increase stack
Inspired by @votrubac
https://leetcode.com/problems/maximum-of-minimum-values-in-all-subarrays/discuss/1373739/Monostack-with-pictures
I came up with this version which I think is more or less easier to understand.

Explanation
Monotonic stack is very powerful and it has several important features, here let's take mono-increase stack as an example (mono-decrease stack will be the opposite)
Given arr = [5,3,1,7,6]
index = 0, mono_increase_stack = [5]
index = 1, mono_increase_stack = [3]
index = 2, mono_increase_stack = [1]
index = 3, mono_increase_stack = [1,7]
index = 4, mono_increase_stack = [1,6]
Features of mono-increase stack
The bottom of stack is the smallest number met so far
5 is the smallest up until index 0
3 is the smallest up until index 1
1 is the samllest up until index 2, 3, 4
Values in stack is always mono-increase (same thing holds if you chose to store indices in mono-stack)
The number being pop out from stack is defintely greater than or equals to the current value
When index = 1, we need to pop out 5 from the stack and push in 3 to comply with the mononotic characteristics, here 5 >= 3
The second value from the top of the stack is the first value less than the value at the top of stack, reading from right to left
When index = 3, you will find 1 is the first number less than 7 reading from right to left
We can also say 1 is the smallest between index 2 and index 3
Same logic holds when index = 4
Let's define a couple things here to better express this feature:
When index = i, the current value is arr[i]
current_value = arr[i], current_idx = i
stack_top_value = stack[-1] if len(stack) >= 1
stack_top_idx = index of stack[-1] in arr
second_stack_top_value = stack[-2] if len(stack) >= 2
second_stack_top_idx = index of stack[-2] in arr
Given above definition, if we adding previous three points 2, 3 & 4 together, we will get:
The stack_top_value is the smallest value between second_stack_top_idx + 1 and current_idx - 1

From bullet point 2 & 4, we know that any number in between second_stack_top_idx + 1 and stack_top_idx is greater than stack_top_value, because second_stack_top_value is the first value less than stack_top_value reading from right to left. (This is the left part: [second_stack_top_idx+1, stack_top_idx])
From bullet point 2 & 3, we know that stack_top_value > current_value, but due to monotonic characteristic, stack_top_value will be less than any value between stack_top_idx and current_idx - 1. (This is the right part: [stack_top_idx, current_idx - 1])
Thus, again we confirmed that stack_top_value is the smallest number between second_stack_top_idx+1 and current_idx - 1, inclusive.
From all 5 features mentioned above, now you know a little bit more about mono-increase stack. To solve this particular problem, feature 5 is the most important one, because it gives us any linear way to find the minimum number of multiple window sizes.
It's excellent that we have this feature using mono stack, but the question now becomes:
Does this method guarantee the maximum value for a certain window size?
Yes.
In the previous process, we are always getting the minimum for different windows
At the mean time, remember in bullet point 1 & 3, the values pushed into stack are always the smallest in certain range, thus as long as we follow the procedure, we are not gonna miss any small values
If we can keep track of all the smallest values in certain range, then we will easilly get the maximum among them all.
Does it guarantee to cover all the window size?
No, not all window size will be touched, but with a tiny tweak, it will definitely touch the largest window size, n = len(nums)
We append a 0 or a very small number to the end of nums, so it will definitely touch window size n, because now the current_idx is n and when we exhaust the stack by popping it, the second_stack_top_idx will be 0
Since not all window size are touched, we need to make sure those non-touched windows have their maximum-minimum value by moving and updating from large window sizes to smaller windows sizes. This is because, max-min value for larger windows will definitely less than or equals to max-min value for smaller window sizes.
Time Complexity: O(N)
Unfortunately, I am not able to get this solution by myself, this problem take advantage of mono-stack in a very subtle way. I feel more like the solution came first and then the problem was made up on top of it. Not a good day for me.
Implementation
class Solution:
    def findMaximums(self, nums: List[int]) -> List[int]:
        stack, n = [], len(nums)
        ans = [0] * n
        for i, num in enumerate(nums):
            while stack and nums[stack[-1]] >= num:              # ensure mono-increase
                min_idx = stack.pop()                            # min_idx is the `stack_top_idx` we mentioned earlier, smallest between `left` and `right` below
                left, right = (stack[-1] + 1) if stack else 0, i # left & right end of window, left is `second_stack_top_idx + 1`, right is `i`
                window = right - left - 1                        # window_size_idx = window size - 1
                ans[window] = max(ans[window], nums[min_idx])    # update maximum
            stack.append(i)
        else:
            while stack:                                         # at the end of iteration, we want to pop out all elements in stack. Here assuming the `current_value` is super small, so that every number in the stack will be popped out
                min_idx = stack.pop()
                left, right = (stack[-1] + 1) if stack else 0, n
                window = right - left - 1    
                ans[window] = max(ans[window], nums[min_idx])
        for i in range(n-2, -1, -1):                             # update non-touched windows using result for larger windows
            ans[i] = max(ans[i], ans[i+1])
        return ans
      
------------------------------------------------------------------------------------
For each element E in nums we want to check what is the maximal range R_E that includes E for which E is the minumum.
Now for each E we will set res[R_E] = max(res[R_E], E) ()
are we done? No bcs we did not actually cover all the ranges. For example in the array 2,1,2 R_1 = [2,1,2] R_2 = [2], R_2 = [2] but hey we did not set any ranges of size 2.., and here is the trick if
E is the minimum of R_E then there exist ranges with size 1,2, .., |R_E| for which E is the minimum. We could explicitely set them, but it will be not efficient. just rememeber this implcitely and before returning res simply iterate with j from the end to beginning and set res[j] = max(res[j], res[j+1]). (**) Now we covered all the ranges. why? Lets prove it.
Lets look at range R = [E1, E2,.., En] assume E_i is the minimum of this range.
If R_Ei = R then we covered this range by () if R_Ei is larger than R (obviosuly it can not be smaller bcs R_Ei is defined to be the largest range for which Ei is the minimum) then we covered it by (**)

Now the question is how we find R_E for each E?
well we use monotonic stack idea.
we iterate on all the elements in array. and for each element E we pop all the elements from stack that E is smaller then them.
Now:

for each such popped element P it holds that E is the first element right to P that is smaller than P. Why? well first of all obviosuly E is smaller than P :-) now lets prove that there is no other element E' between P and E that is smaller than P, well there is not such element bcs if there was such then P would already be popped.
for each popped element P let PP be the element before P in the stack then PP is the first element left to P that is not greater than P, lets assume that there is somebody else between PP and P that is not greater than P, so let PPP be the minimum between PP and P, but then PPP would have still exist in stack, who killed him?
thats it when popping some element E we know R_E and we are done.
note that I lie a bit, bcs if we 2 equal elements in the stack E1, E2 then R_E2 would not be correct bcs it did not include E1, but who care, we will pop E1 and get R_E1 which is correct. which was intended to be R_E2.

also note that I do 2 small tricks here.

adding -inf to the end of nums, and that will promise me that all the elements will be eventually popped.
starting stack with -1 inside and defining nums[-1] = -inf
those has nothing to do with correctness, but just a trick for shorter code.
otherwise I would need to (1) pop everything that left in the stack in the end of the iteration. (2) when looking at the previous element in the stack, I would need to conider the case there is no such element and understand that it means that all the elemente that are left to P are not smaller than him.
so its just for convinience.
'''

class Solution(object):
    def findMaximums(self, nums):
        res = [0] * len(nums)        
        nums += [-1 * sys.maxint]
        stack = [-1]
        for i in xrange(len(nums)):
            while nums[i] < (nums[stack[-1]] if stack[-1] >= 0 else -1 * sys.maxint):
                res[i - stack[-2] - 2] = max(res[i - stack[-2] - 2], nums[stack[-1]])
                stack.pop()
            stack.append(i)
        for i in reversed(xrange(len(nums) - 2)):
            res[i] = max(res[i + 1], res[i])
        return res  
-----------------------------------------------------------------------------------------------
class Solution:
    def findMaximums(self, nums: List[int]) -> List[int]:
        N = len(nums)
        cl = [None]*N
        cr = [None]*N
        
        stack = []
        for i in range(N):
            while stack and nums[stack[-1]]>=nums[i]:
                stack.pop()
            if not stack:
                cl[i] = i+1
            else:
                cl[i] = i-stack[-1]
            stack.append(i)
        # now cl[i]==a means that nums[i] is a minimum of the range of length a starting from i 
        # and going to the left
            
        stack = []
        for i in range(N-1,-1,-1):
            while stack and nums[stack[-1]]>=nums[i]:
                stack.pop()
            if not stack:
                cr[i] = N-i
            else:
                cr[i] = stack[-1]-i
            stack.append(i)
        # now cr[i]==b means that nums[i] is a minimum of the range of length b starting from i 
        # and going to the right
            
        
        cnt = [a+b-1 for a,b in zip(cl,cr)]
        # cnt[i]==c means that there is a subarray of length c where nums[i] is a minimum
        # and c is the maximum possible one
        
        cnti = sorted(range(N), key=cnt.__getitem__, reverse=True) # reverse argsort
        ofs = 0
        ans = [None]*N
        best = -10**10
        for L in range(N,0,-1):
            # will fill ans[L-1]
            # ans[L-1] is the max of all such nums[i] that cnt[i]>=L
            while ofs<N and cnt[cnti[ofs]]>=L:
                best = max(best,nums[cnti[ofs]])
                ofs += 1
            ans[L-1] = best
        return ans
------------------------------------
class Solution:
    def findMaximums(self, nums: List[int]) -> List[int]:
        ans = [0]*len(nums)
        stack = []
        for i, x in enumerate(nums + [0]): 
            while stack and stack[-1][1] >= x: 
                _, xx = stack.pop()
                k = i-stack[-1][0]-2 if stack else i-1
                ans[k] = max(ans[k], xx)
            stack.append((i, x))
        
        for i in reversed(range(len(nums)-1)): 
            ans[i] = max(ans[i], ans[i+1])
        return ans
-----------------------------------------------------------------------------
Monotonic Stack
Yes, I referred to other post for the optimal solution, and this problem should be marked as hard if N^2 solution is not accepted.

The first approach I came up with is to maintain running minimum within window of size of length using queue, updating the maximum value with the first element in the queue for each num. This approach denotes to O(N^2) time complexity, causing Time Limits Exceeded.

def findMaximums(self, nums: List[int]) -> List[int]:  
	def helper(length):
		queue = deque([])
        last = max_min = 0
        for i, num in enumerate(nums):
			if i - last + 1 > length:
				if queue[0] == last:
					queue.popleft()
				last += 1
			while queue and nums[queue[-1]] > num:
				queue.pop()
			queue.append(i)
            if i - last + 1 == length: 
				max_min = max(max_min, nums[queue[0]])
		return max_min
        
    return [helper(i + 1) for i in range(len(nums))]
It turned out that this is a tricky problem using monotonic stack, where the poped up value might be the result for the query with length of stack[-1] ... current i. Why?
We maintain the increasing monotonic stack, keeping popup the stack[-1] if nums[stack[-1]] >= num, and we havenums[stack[-2]] < nums[stack[-1]] >= num. So the nums[stack[-1]] is the minimum value of subarray with range of [stack[-2] +1: i - 1]. Because if there is any larger value x in the range, the stack[-1] should have been popped up when seeing x. So we can update the query[range] with nums[stack[-1]].
Finally, there is possible to be no result yet for some queris. With observation, the maximum value would be the result of query[0], and the minimum value would be the result of query[-1], so the query array is actually deceasing. Then we can fill up the empty slot in query array by propagating the previous value.

def findMaximums(self, nums: List[int]) -> List[int]:
	stack = []
    nums = [-1] + nums + [0]
    n = len(nums)
    res = [0] * (n - 2)
    for i, num in enumerate(nums):
		while stack and nums[stack[-1]] >= num:
			j = stack.pop()
            k = i - 1 - (stack[-1] + 1)
			res[k] = max(res[k], nums[j])
		stack.append(i)      

	for i in range(n - 3, 0, -1):
		res[i - 1] = max(res[i], res[i - 1])
	return res
        
        
        
      
