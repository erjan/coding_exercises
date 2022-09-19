'''
Given an array arr that represents a permutation of numbers from 1 to n.

You have a binary string of size n that initially has all its bits set to zero. At each step i (assuming both the binary string and arr are 1-indexed) from 1 to n, the bit at position arr[i] is set to 1.

You are also given an integer m. Find the latest step at which there exists a group of ones of length m. A group of ones is a contiguous substring of 1's such that it cannot be extended in either direction.

Return the latest step at which there exists a group of ones of length exactly m. If no such group exists, return -1.
'''

#recursive dfs

def findLatestStep(arr, m):
    """
    :type arr: List[int]
    :type m: int
    :rtype: int
    """
    def dfs(start, end, step, target):
            
        if end - start + 1 < target:
            return -1
        
        elif end - start + 1 == target:
            return step
        
        x, res = arr[step - 1], -1

        if start <= x <= end:
            res = max(res, dfs(start, x - 1, step - 1, target), dfs(x + 1, end, step - 1, target))
        else:
            res = max(res, dfs(start, end, step - 1, target)) 
        return res
        
    n = len(arr)
    if m == n:
        return n
    else:
        return dfs(1, n, n, m)
      
------------------------------------------------------------------------------------------------------------------------
from collections import defaultdict

class Solution:
    def findLatestStep(self, arr: List[int], m: int) -> int:
        
        size = len(arr)
        
        if size == m:
            
            # Quick response for simple case
            # total m flips and m is equal to array size
            
            return size
        
        
        
        # key: length of substring with contiguous 1s
        # value: the count of substring with contiguous 1s with specified length, initialized as 0
        counter_of_len = defaultdict(lambda :0)
        
        
        # index: i
        # value: length of substring with contiguous 1s, which covers index i
        # +1 padding on head, +1 padding on tail, total + 2 to avoid index out-of-boundary
        len_of_cont_1s = [0] * ( size + 2 )
        
        
        last_good_step = -1
        
        # flip cur_idx to 1, and update information of length of 1s as well as count of 1s
        for step, cur_idx in enumerate(arr, 1):
            
            # get original length of 1s on left border and right border
            left_1s_length = len_of_cont_1s[cur_idx - 1]
            right_1s_length = len_of_cont_1s[cur_idx + 1]
            
            
            # compute the new length of 1s after flipping
            combined_1s_length = left_1s_length + 1 + right_1s_length
            
            
            # update new length of 1s on left borader and right border
            len_of_cont_1s[cur_idx - left_1s_length] = combined_1s_length
            len_of_cont_1s[cur_idx + right_1s_length] = combined_1s_length
            
            
            # update counter_of_len dictionary after flipping
            counter_of_len[combined_1s_length] += 1
            counter_of_len[left_1s_length] -= 1
            counter_of_len[right_1s_length] -= 1
                
                
            if counter_of_len[m] > 0:
                # now we still have substring of contiguous 1s with length exactly equal to m
                last_good_step = step
        
        
        return last_good_step
