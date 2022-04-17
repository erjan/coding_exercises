
'''
Given an integer array nums of length n, return true if there is a triplet (i, j, k) which satisfies the following conditions:

0 < i, i + 1 < j, j + 1 < k < n - 1
The sum of subarrays (0, i - 1), (i + 1, j - 1), (j + 1, k - 1) and (k + 1, n - 1) is equal.
A subarray (l, r) represents a slice of the original array starting from the element indexed l to the element indexed r.
'''


class Solution:
    def splitArray(self, nums: List[int]) -> bool:
        front = [nums[0] for i in range(len(nums))]
        back = [nums[-1] for i in range(len(nums))]
        for i in range(1, len(nums)): #O(n)
            front[i] = front[i - 1] + nums[i]
        
        for i in reversed(range(len(nums) - 1)):#O(n)
            back[i] = back[i + 1] + nums[i]
            
        back2 = dict()
        for i in range(len(nums)):
            if back[i] not in back2:
                back2[back[i]] = [i]
            else:
                back2[back[i]].append(i)
                
        
        for i in range(len(nums)):#O(n)
            if front[i] in back2:
                for j in back2[front[i]]:
                    if i < j:
                        new_arr = nums[i + 2:j - 1]
                        second_front = [new_arr[0] for k in range(len(new_arr))]
                        second_back = [new_arr[-1] for k in range(len(new_arr))]
                        for k in range(1, len(new_arr)):
                            second_front[k] = second_front[k - 1] + new_arr[k]
                        for k in range(len(new_arr)):
                            if second_front[k] == front[i]:
                                if second_front[k] == sum(new_arr[k + 2:]) and new_arr[k + 2:] != []:
                                    return True
        return False
        
        
----------------------------------------


'''
The key idea is kind like divide and conquer (only twice though).

First, for every middle point j, we split nums into two subarray nums[:j] and nums[j+1:]. In the helper function split, try to remove one element from the subarray, if the the sums of two remaining left and right sub-subarray are equal, we keep the sum of sub-subarray in the set we return. Once we have any intersection between the two sets, we know we can make it.

Keep in mind len(nums) > 6 is a must since we need to split original array into four parts.
'''

class Solution:
    def splitArray(self, nums: List[int]) -> bool:
        sms = defaultdict(list)
        smsi = {}
        sm = 0
        for i, x in enumerate(nums):
            sm += x
            sms[sm].append(i)
            smsi[i] = sm
        
        N = len(nums)
        for i in range(1, N-5):
            targ = smsi[i-1]
            cand = smsi[N-1] - targ  #19
            if cand in sms:                   #sms[i-1]
                for k in sms[cand]:
                    if k > i + 3:
                        for j in range(i+2, k-1):
                            if smsi[j-1] - smsi[i] == targ and smsi[k-1] - smsi[j] == targ:
                                return True

        return False
      
      ------------------------------------
      
      class Solution(object):
    def splitArray(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        def split(A):
            total = sum(A)
            for i in range(1, len(A)): A[i] += A[i-1]
            return {A[i-1] for i in range(1, len(A)-1) if A[i-1] == total - A[i]}
            
        return len(nums) > 6 and any(split(nums[:j]) & split(nums[j+1:]) \
                             for j in range(3, len(nums)-3))
      
------------------------------------------------------------
Let A be the array. As in most problems involving querying the sum of contiguous elements of an array, let P[x] = sum(A[:x]) be the prefix sums of A, which can be found in linear time.

Then the sums in question are P[i] = P[j] - P[i+1] = P[k] - P[j+1] = P[-1] - P[k+1]. For every j < k, P[i] = P[-1] - P[k+1] is a necessary requirement to choose i, so let's iterate over those indices first. This gives us the advantage that since we are iterating over a sorted list of candidate indices i, we can break when i >= j.

def splitArray(self, A):
    P = [0]
    for x in A: P.append(P[-1] + x)
    
    N = len(A)
    Pinv = collections.defaultdict(list)
    for i, u in enumerate(P):
        Pinv[u].append(i)
        
    for j in xrange(1, N-1):
        for k in xrange(j+1, N-1):
            for i in Pinv[P[-1] - P[k+1]]:
                if i >= j: break
                if P[i] == P[j] - P[i+1] == P[k] - P[j+1]:
                    return True
    return False
