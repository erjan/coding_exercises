'''
You are given a 0-indexed integer array nums of length n. The number of ways to partition nums is the number of pivot indices that satisfy both conditions:

1 <= pivot < n
nums[0] + nums[1] + ... + nums[pivot - 1] == nums[pivot] + nums[pivot + 1] + ... + nums[n - 1]
You are also given an integer k. You can choose to change the value of one element of nums to k, or to leave the array unchanged.

Return the maximum possible number of ways to partition nums to satisfy both conditions after changing at most one element.

 
 '''

Create a map of list , going thru the indices and make diff between right half and left half as key.
Store all the indices in the list having the diff as x, as you gonna need it it later.
Now try to change all the indices and check how many indices could now become your pivot.
So you are changing a num, nums[i] to k.
Let's assume this i index is in the left of pivot. So by changing nums[i] to k, you are increasing the sum of left half by k-nums[i].
So all the pivots where the right half's sum was (k-nums[i]) grater than left half's sum, would now be balanced, as you have added that (k-nums[i]) to the left. So just find out how many indices are in the RIGHT of index i, having such diff. Now, those all will be counted as pivots.
Now go back to step 5. We had assumed the index i to be in the left of pivot. Nows the time to take it the other way.
Now the index i is inthe right of pivot. By changing nums[i] to k, we have increased right half by (k-nums[i]).
So search for all the indices having left half's sum more than rights's half by (k-nums[i]).
The ans for the index i would be the sum of the both assumptions we have taken.
Do the same for all the indices. Max of all will be your answer. :)
def waysToPartition(self, nums: List[int], k: int) -> int:
   l, r = 0, sum(nums)
   d = defaultdict(list)
   prev = nums[0]
   n = len(nums)
   ans = 0
   for i in range(1, n):
   	l += prev
   	r -= prev
   	if(l == r): ans += 1
   	d[r-l].append(i)
   	prev = nums[i]
   for i in range(n):
   	diff = k-nums[i]
   	left = right = 0
   	if(diff in d):
   		right = len(d[diff]) - bisect_left(d[diff], i+1)
   	if(d[-diff] and d[-diff][0] <= i):
   		left = bisect_right(d[-diff], i)
   	ans = max(ans, left+right)
   return ans

--------------------------------------------------------------------------------------
from collections import defaultdict
class Solution:
    def waysToPartition(self, nums: List[int], k: int) -> int:
        total = sum(nums)
        counts = defaultdict(int)
        t = 0
        for idx in range(len(nums)-1):
            t += nums[idx]
            counts[t] +=1
        res = counts[total//2] if total%2==0 else 0
        temp_counts = defaultdict(int)
        t,N = 0, len(nums)
        for idx in range(N):
            possible = t+k
            halves = (total+ k-nums[idx])
            if halves%2==1:
                t += nums[idx]
                temp_counts[t] +=1
            else:
                halves = halves//2
                t += nums[idx]
                total_halves_later = counts[halves-k+nums[idx]]- temp_counts[halves-k+nums[idx]]#if pivot happens later
                total_halves_before = temp_counts[halves]#if pivot happens before
                temp_counts[t] +=1
                res = max(res, total_halves_later+total_halves_before)
        return res
