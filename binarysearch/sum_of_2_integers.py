Given a list of numbers nums and a number k, return whether any two elements from the list add up to k. You may not use the same element twice.

Note: Numbers can be negative or 0.
  

class Solution:
    def solve(self, nums, k):
        s = set()
        
        for e in nums:
            complement = k - e
            if complement in s:
                return True
            s.add(e)
        return False	
