'''
Given an array of digits digits, return the largest multiple of three that can be formed by concatenating some of the given digits in any order. If there is no answer return an empty string.

Since the answer may not fit in an integer data type, return the answer as a string. Note that the returning answer must not contain unnecessary leading zeros.
'''


class Solution:
    def largestMultipleOfThree(self, digits):
        running_sum, ans0, ans1, ans2 = 0, [], [], []

        for i in digits:
            running_sum += i

            if i%3 == 0:
                ans0.append(i)
            elif i%3 == 1:
                ans1.append(i)
            else:
                ans2.append(i)

        ans1.sort(reverse = True)
        ans2.sort(reverse = True)

        if running_sum%3 == 1:
            if ans1:
                ans1.pop()
            else:
                if ans2:
                    ans2.pop()
                else:
                    return ""

                if ans2:
                    ans2.pop()
                else:
                    return ""


        if running_sum%3 == 2:
            if ans2:
                ans2.pop()
            else:
                if ans1:
                    ans1.pop()
                else:
                    return ""

                if ans1:
                    ans1.pop()
                else:
                    return ""

        result = ans0 + ans1 + ans2

        result.sort(reverse = True)

        s = ""

        for i in result:
            s += str(i)

        return str(int(s)) if s else ""


------------------------------------------------------------------------------------------------------
class Solution:
    def largestMultipleOfThree(self, digits: List[int]) -> str:
        count = collections.Counter(digits)
        
        mod1 = count[1] + count[4] + count[7]
        zeroMod1 = not mod1
        mod1 %= 3
        
        mod2 = count[2] + count[5] + count[8]
        zeroMod2 = not mod2
        mod2 %= 3
        
        nums1, nums2 = (1, 4, 7), (2, 5, 8)
        
        def removeK(nums, k):
            for i in nums:
                rem = min(count[i], k)
                count[i] -= rem
                k -= rem  
        
        if mod1 == mod2:
            removeK((), 0)
        elif zeroMod1:
            removeK(nums2, mod2)
        elif zeroMod2:
            removeK(nums1, mod1)
        elif (mod1 - mod2) % 3 == 1:
            removeK(nums1, 1)
        else:
            removeK(nums2, 1)
        
        res = ''.join(str(digit) * count[digit] for digit in range(9, -1, -1))
        return res if not res or res[0] != '0' else '0'
      
----------------------------------------------------------------------------------------------------------

            

