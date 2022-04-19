'''
You are given an integer array ribbons, where ribbons[i] represents the length of the ith ribbon, and an integer k. You may cut any of the ribbons into any number of segments of positive integer lengths, or perform no cuts at all.

For example, if you have a ribbon of length 4, you can:
Keep the ribbon of length 4,
Cut it into one ribbon of length 3 and one ribbon of length 1,
Cut it into two ribbons of length 2,
Cut it into one ribbon of length 2 and two ribbons of length 1, or
Cut it into four ribbons of length 1.
Your goal is to obtain k ribbons of all the same positive integer length. You are allowed to throw away any excess ribbon as a result of cutting.

Return the maximum possible positive integer length that you can obtain k ribbons of, or 0 if you cannot obtain k ribbons of the same length.
'''


The crux of the problem is implementing Binary Search.
The goal is to figure out what the maximum length of a ribbon could be so that we get k ribbons of that max length.
One way to think of it would be that the ribbon length could be anywhere from 1 to the max length of the a ribbon available in the list.

So what we do is go through the list (using Binary Search since we need to optimize linear search), find the mid of the given array and then iterate through the list testing the length with each element and summing the number of ribbons that can be made with the mid value. Then change mid accordingly

class Solution:
    def maxLength(self, ribbons: List[int], k: int) -> int:
        # The minumum length of the ribbon that we can cut is 1
        start = 1
        # The maximum length of the ribbon can be the maximum element in the list
        end = max(ribbons)
        
        # In this binary search, we are trying to go through the origin list and figure out which integer(from 1 -> ribbon of max length) is the deired length for the the target k pieces
        while(start <= end):
            mid = start + (end - start) // 2
            res = 0
            for i in ribbons:
                res += i // mid
            # If the value is >= target, we know that there could be a larger integer that will satisfy the same conditon
            if res >= k:
                start = mid+1
            else:
            # If lesser than k, then there could be a value lesser than the mid that could satisfy the condition
                end = mid -1
        return end
      
----------------------------------------------------------------------------------
Explanation
All possible solution will format a continuous sequence
Use binary search to search on this sequence and return the maxiumum one
Time: O(NlogN)
Implementation
class Solution:
    def maxLength(self, ribbons: List[int], k: int) -> int:
        s = sum(ribbons)             # impossible case: when total length sum of all ribbons are less than `k`
        if s < k: return 0
        n = len(ribbons)
        def ok(mid):                 # is it `ok` to form `k` ribbon with length `mid`?
            nonlocal ribbons, k
            cnt = 0
            for r in ribbons:
                cnt += r // mid
            return cnt >= k    
        l, r = 1, max(ribbons)
        while l <= r:                # binary search
            mid = (l+r) // 2
            if ok(mid):
                l = mid + 1
            else:
                r = mid - 1
        return r         
------------------------------------------------------------------------------------------------------------------------
class Solution:
    def maxLength(self, ribbons: List[int], k: int) -> int:
	
        minPossible = 1             # minimum possible ribbon length
        maxPossible = max(ribbons)  # maximum possible ribbon length
        
        while minPossible <= maxPossible:
            currentLength = minPossible+(maxPossible-minPossible)//2 # length of current try
            numOfPiecesWithcurrentLength = 0
            for ribbon in ribbons:  # getting number of possible ribbons with current length
                numOfPiecesWithcurrentLength += ribbon//currentLength  
				
            if numOfPiecesWithcurrentLength >= k: # we have longer pieces than we need so we can try longer lengths == increase lower bound (minPossible)
                minPossible = currentLength + 1
            else:
                maxPossible = currentLength - 1

        return maxPossible
      
------------------------------------------------------------------------------------
Brute Force
The problem asks us to the max length of k ribbons. Lets first consider what lengths can we get.

We know that min length is 1 (e.g, ribbons = [3], k = 3). If we could not get length 1 (e.g. ribbons = [2], k = 3), then we return 0. Now the max length is a bit tricky, at first, I though it is min(ribbons). based on the example ribbons = [9,7,5], k = 3. However, we can easily find a counter example ribbons = [10,10,1], k = 2 there is a similar test case, this one is simplified.

Problem is simple now, just go from 1 to max(ribbons), find the largest length with the number of ribbons == k. Problem solved with time complexity O(max(ribbons))

Binary Search
Can we do better? Yes! If you think through the problem, we are given some index [1, max(ribbons)], and we want to find the largest index such that length2ribbon[index] == k (I will explain the meaning of the array latter). Sounds familiar? If such an array length2ribbon is sorted, we could use binary search!

The real question is whether the array is sorted? Fortunately, yes it is. length2ribbon is the array containing number of ribbons we get if we use length index to cut them. More formally, we calculate the array by [float('inf')] + [sum([ribbon // length for ribbon in ribbons]) for length in range(1, max(ribbons))]. Its a bit complicated, but essentially, the number at index i is the number of ribbons we get if we are using length i to cut. The first term is the correction for 1 indexed array. We can easily prove that this array is non increasing.(when you are cutting with a larger length, it is not possible to get more ribbons!) This means we can do binary search on it.

This is the basic idea why we are legitimate to do binary search. In most answers, including the code I give, we do not actually construct the array as I have mentioned above becuase it is not necessary. But it is nice to reason yourself out why you can do binary search on sth that does not seems like an array.

Here is my code, ask questions if I do not explain it clearly! Hope it is helpful.

Binary search is a lard topic! I find it challening for a long time. Try to solve problem https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/, carefully reason through why your code works by loop invariant!

 class Solution:
    def maxLength(self, ribbons: List[int], k: int) -> int:
        if sum(ribbons) < k:
            return 0 # we will not able to make k ribbons 
				# think about binary search left and right index
        left, right = 1, max(ribbons) 
        while left < right:
						# a classical way of finding the largest index by binary search
            mid = (left+right) // 2 + 1
						# think of getting the value at index mid 
            cuts = sum([ribbon // mid for ribbon in ribbons])
            if cuts >= k:
                left = mid
            elif cuts < k:
                right = mid-1
        return right
      
-----------------------------------------------------------------------------
Folks, I am lazy, if there is a built-in function to do the job I will use it. It's not the quickest coming in at ~70%. But essentially the bisect built in library gives you the functionality to do a binary search, since python 3.10 you can add a key function. I make a key function that calculates how many ribbons you could cut given a length. You then just do the binary search over the possible ribbon lengths (you can do this because the number of possible ribbons increases monotonically with decreasing ribbon lengths). Hope it helps.

from functools import partial
class Solution:
        def maxLength(self, ribbons,k): 
            max_rib = max(ribbons)
            search = FakeArray(max_rib)
            key = partial(total_ribbons, ribbons = ribbons)
            position = bisect.bisect_left(search, k, key = key)
			#The if block here just handles the boundary cases... It doesn't really add to the algo. 
            if position==0:
                return len(search)
            elif position == len(search):
                return 0
            else:
                return len(search)-position
            
def total_ribbons(x,ribbons):
	""" Returns the total ribbons that could be cut from the given 
	ribbons. 
	"""
    return sum([rib//x for rib in ribbons])

class FakeArray():
    """
    Just abusing python duck typing so that bisect_left thinks
    it's searching an array without having to put it all in memory
    Equivalent to having search = list(range(max_rib,0,-1)). 
	I did this optimization just out of interest. 
    """
    def __init__(self, max_rib):
        self.max_rib = max_rib
        
    def __len__(self):
        return self.max_rib
    
    def __getitem__(self, idx):
		""" We search from largest to smallest ribbon size thus the following equation. 
		"""
        return self.max_rib-idx
      
      
      
      
