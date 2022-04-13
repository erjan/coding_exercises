'''

You are given a 0-indexed integer array nums of length n.

The sum score of nums at an index i where 0 <= i < n is the maximum of:

The sum of the first i + 1 elements of nums.
The sum of the last n - i elements of nums.
Return the maximum sum score of nums at any index.

'''


class Solution:
    def maximumSumScore(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
                        
        n = nums
        n2 = n[::-1]

        suf = [0] * len(n)
        suf[0] = n2[0]
        for i in range(1, len(n2)):
            suf[i] = suf[i-1] + n2[i]

        suf = suf[::-1]

        # 10 6 3 5
        pref = [0] * len(n)
        pref[0] = n[0]
        for i in range(1, len(n)):

            pref[i] = pref[i-1] + n[i]

        print('prefix sum')
        print(pref)
        print('suffix sum')
        print(suf)
        print('-----------------------------')
        print('-----------------------------')
        print('-----------------------------')
        res = float('-inf')
        for i in range(len(pref)):
            print('comparing', pref[i], suf[i])

            temp = max(pref[i], suf[i])
            if temp > res:
                res = temp
        print('res', res)

        return res
      
      
------------------------------------------------------

class Solution:
    def maximumSumScore(self, nums: List[int]) -> int:
        ans = -sys.maxsize
        prefix = [0]
        for num in nums:
            prefix.append(prefix[-1] + num)
        s = prefix[-1]    
        for i, num in enumerate(nums):
            cur = max(prefix[i+1], s-prefix[i+1]+num)
            ans = max(ans, cur)
        return ans
      
-------------------
    def maximumSumScore(self, nums: List[int]) -> int:
        l = 0
        r = t = sum(nums)
        for n in nums:
            l += n
            t = max(t, l, r)
            r -= n
        return t
