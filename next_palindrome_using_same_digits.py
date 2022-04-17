You are given a numeric string num, representing a very large palindrome.

Return the smallest palindrome larger than num that can be created by rearranging its digits. If no such palindrome exists, return an empty string "".

A palindrome is a number that reads the same backward as forward.


class Solution:
    def nextPalindrome(self, num: str) -> str:
        mid = len(num) // 2
        center = ""
        if len(num) % 2 != 0:
            center = num[mid]
        aux_num = list(num[:mid])
        i = len(aux_num) - 2
        while i >= 0 and aux_num[i] >= aux_num[i + 1]:
            i -= 1
        if i < 0:
            return ""
        
        j = len(aux_num) - 1
        while j >= 0 and aux_num[i] >= aux_num[j]:
            j -= 1
        aux_num[i], aux_num[j] = aux_num[j], aux_num[i]
        aux_num[i + 1:] = reversed(aux_num[i + 1:])
        return ''.join(aux_num) + center + ''.join(reversed(aux_num))
      
-------------------------------------------------------------------------

The idea is:

find the next permutation that is greater than the first half of the palindrome, say greaterHalf
add it to the mid item if there is one and to reversed of greaterHalf
The code is below:

class Solution:
    def get_next_larger(self, sList):
        i = len(sList) - 2
        while i >= 0 and sList[i] >= sList[i + 1]:
            i -= 1
        if i < 0:
            return []

        j = len(sList) - 1
        while j>=0 and sList[i] >= sList[j]:
            j -= 1

        sList[i], sList[j] = sList[j], sList[i]
        sList[i + 1:] = reversed(sList[i + 1:])
        
        return sList
    
    def nextPalindrome(self, num: str) -> str:
        num_list = list(num)
        mid = len(num) // 2
        midStr = "" if (len(num) % 2 == 0) else num_list[mid]
        
        left_greater = self.get_next_larger(num_list[: mid])
        if not left_greater:
            return ""
        
        
        return  "".join(left_greater) + midStr + "".join(reversed(left_greater))
      
------------------------------------------------------------------------------------------------------
class Solution:
    def nextPalindrome(self, num: str) -> str:
        n = len(num)
        k, r = divmod(n, 2)
        mid = num[k] if r else ''

        if k > 1:
            s = num[:k]
            stack = []
            for j in range(k-1, -1, -1):
                if not stack or s[j] >= s[j+1]:
                    stack += s[j],
                else:
                    index = bisect.bisect_right(stack, s[j])
                    x, stack[index] = stack[index], s[j]
                    sub = s[:j] + x + ''.join(stack)
                    return sub + mid + sub[::-1]
        return ''
