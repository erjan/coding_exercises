'''
This is an interactive problem.

You have a sorted array of unique elements and an unknown size. You do not have an access to the array but you can use the ArrayReader interface to access it. You can call ArrayReader.get(i) that:

returns the value at the ith index (0-indexed) of the secret array (i.e., secret[i]), or
returns 231 - 1 if the i is out of the boundary of the array.
You are also given an integer target.

Return the index k of the hidden array where secret[k] == target or return -1 otherwise.

You must write an algorithm with O(log n) runtime complexity.
'''


Explanation
Tho we don't know the exact size, we do know the upper limit which is 10000 by question description
The length of the array will be in the range [1, 10^4].

get method handle exception for us easily, so it's a pure vanilla binary search
Implementation


class Solution:
    def search(self, reader, target):
        l, r = 0, 10000
        while l <= r:
            mid = (l+r)//2
            val = reader.get(mid)
            if val == target: return mid
            elif val < target: l = mid+1
            else: r = mid-1 
        return -1
      
--------------------------------------------------

First, we need to know the search range, i.e., the reasonable right index. We can double the right index each time until the rightmost element is larger than the target.
Then we can do a binary search to find the target.

class Solution:
    def search(self, reader, target):
        """
        :type reader: ArrayReader
        :type target: int
        :rtype: int
        """
        # Since the size of the array is unknown, we need to determine the search range first, i.e., the right index of the array
        # initiate the array size as [0,1], keep doubling the size until we find target > reader.get[r].
        l,r = 0, 1
        while target > reader.get(r):
            r = r * 2
            
        # After we determined the search range, we can do a traditional binary search
        while l <= r:
            m = (l+r)>>1
            print(l,m,r)
            # we find the target, return the index
            if reader.get(m) == target:
                return m
            # Since we didn't find the target, we eliminate the half that the target isn't in.
            else:
                if reader.get(m) < target:
                    l = m + 1
                else:
                    r = m - 1
        # when it's outside the while loop, the algorithm can't find the target, return -1
        return -1
------------------------------------------------------

"""
Runtime O( log n)
Spacetime O(1)

-- submission stats --
Runtime: 28 ms, faster than 99.39% of Python3 online submissions for Search in a Sorted Array of Unknown Size.
Memory Usage: 13.9 MB, less than 100.00% of Python3 online submissions for Search in a Sorted Array of Unknown Size.
"""
from dataclasses import dataclass
OUT_OF_BOUNDS = 2147483647
NOT_FOUND = -1
    
@dataclass
class Bound: 
    low: int
    high: int
        
    @property
    def is_out_of_bounds(self):
        return self.low == OUT_OF_BOUNDS and self.high == OUT_OF_BOUNDS
        
class Solution:

    def get_searchable_bounds(self, reader, target):
        low = 0 
        high = 1
        
        while reader.get(high) != OUT_OF_BOUNDS and reader.get(high) < target:

            # we'll double our searching size until we're in a valid searchable bound
            current_searchable_size = (high - low) + 1
            next_searchable_size = current_searchable_size * 2
            # move our lower bound one above the previous, invalid, searchable space
            low = high + 1
            # move our high bound the {next_searchable_size} away from our new low bound
            # 1 is substracted since size is not zero indexed 
            high = low + (next_searchable_size - 1)
        
        if reader.get(low) == OUT_OF_BOUNDS:
            return Bound(OUT_OF_BOUNDS, OUT_OF_BOUNDS)
        return Bound(low, high)
            
    def search(self, reader, target):
        bound = self.get_searchable_bounds(reader, target)
        
        if bound.is_out_of_bounds:
            return NOT_FOUND
        
        low = bound.low
        high = bound.high
        while low <= high: 
            middle = (low + high) // 2
            candidate = reader.get(middle)
            
            if target == candidate:
                return middle
            
            if target > candidate:
                low = middle + 1
            
            if target < candidate:
                high = middle - 1 
        
        return NOT_FOUND
---------------------------------------------------------------

class Solution:
    def search(self, reader: 'ArrayReader', target: int) -> int:
        left=0
        right=target-reader.get(0)
        
        if reader.get(right)==target:
            return right
        elif reader.get(right)<target:
            return -1
        
        while left<=right:
            mid=left+(right-left)//2
            
            if reader.get(mid)==target:
                return mid
            
            if reader.get(mid)<target:
                left=mid+1
            else:
                right=mid-1
        return -1
      
      
      
