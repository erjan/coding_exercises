'''
You are given a 0-indexed integer array nums. A pair of indices i, j where 0 <= i < j < nums.length is called beautiful if the first digit of nums[i] and the last digit of nums[j] are coprime.

Return the total number of beautiful pairs in nums.

Two integers x and y are coprime if there is no integer greater than 1 that divides both of them. In other words, x and y are coprime if gcd(x, y) == 1, where gcd(x, y) is the greatest common divisor of x and y.


'''


class Solution:
    def countBeautifulPairs(self, nums: List[int]) -> int:
        res = 0
        n = len(nums)
        for i in range(n):
            for j in range(i+1,n):
                first = int(str(nums[i])[0])
                last = int(str(nums[j])[-1])

                if gcd(first,last) == 1:
                    res+=1
        return res

------------------------------------------------------------------------------------
    def countBeautifulPairs(self, nums: List[int]) -> int:
        pairs = 0
        for i, num in enumerate(nums):
            d = num % 10
            for j in range(i):
                n = nums[j]
                while n >= 10:
                    n //= 10
                pairs += gcd(d, n) == 1
        return pairs
