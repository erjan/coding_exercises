'''
A binary string is monotone increasing if it consists of some number of 0's (possibly none), followed by some number of 1's (also possibly none).

You are given a binary string s. You can flip s[i] changing it from 0 to 1 or from 1 to 0.

Return the minimum number of flips to make s monotone increasing.
'''

class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        
        # occurrence of 1 in strings s
        occ_of_1 = 0
        
        # counter of flips of 1->0 and 0->1
        flip = 0
        
        
        # scan each digit on substring s[:i], i = 1 ~ len(s)
        for char in s:
            
            if char == '1':
                
				# update occurrence of '1'
                occ_of_1 += 1
                
				# current digit is '1'
                # no need to flip when 1 is on the tail of current substring
            
            else:
                
				# current digit is '0'
                # need to flip when 0 is on the tail of current substring
                
                # option_1: flip current 0 to 1, keep leading digits, then substring is monotone increasing
                
                # option_2: flip leading 1s to 0s, keep current 0, then substring is monotone increasing
                
                # select optimal solution
                flip = min(flip+1, occ_of_1)
                
        return flip
      
------------------------------------------------------------------------
This question should be quite straightforward and no need to over think.
We check the string from left or right, and keep the substring prior to current position monotone increasing.

If we encounter a 1, do nothing since appending this won't break the monotonicity.
If we encounter a 0, then two options to keep substring with current char monotonic:

Flip this 0 to 1
Flip all previous 1 to 0
For second option, we need to know how many 1s are there up to now, simply by couting prefix sum.

class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        total = flip = 0
        for c in s:
            total += c == '1'
            if c == '0':
                flip = min(flip + 1, total)
        return flip
