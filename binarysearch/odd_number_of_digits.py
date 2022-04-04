'''

Given a list of positive integers nums, return the number of integers that have odd number of digits.

'''


class Solution:
    def solve(self, nums):

        nums = list(map(lambda x: len(str(x)  ), nums ))
        nums = list(filter(lambda x: x%2 == 1, nums))
        return len(nums)
        
        
#another

class Solution:
    def solve(self, nums):
        def digits(n):
            c = 0
            while n > 0:
                c += 1
                n //= 10
            return c

        # ONELINER return sum(map(lambda x: x%2!=0,(digits(i) for i in nums)))
        tot = 0
        for i in nums:
            if digits(i) & 1:
                tot += 1
        return tot
