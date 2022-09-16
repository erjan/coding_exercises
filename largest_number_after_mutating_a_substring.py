'''
You are given a string num, which represents a large integer. You are also given a 0-indexed integer array change of length 10 that maps each digit 0-9 to another digit. More formally, digit d maps to digit change[d].

You may choose to mutate a single substring of num. To mutate a substring, replace each digit num[i] with the digit it maps to in change (i.e. replace num[i] with change[num[i]]).

Return a string representing the largest possible integer after mutating (or choosing not to) a single substring of num.

A substring is a contiguous sequence of characters within the string.
'''

class Solution:
def maximumNumber(self, num: str, change: List[int]) -> str:
    flag=0
    ls=list(num)
    for i in range(len(ls)):
        k=int(ls[i])
        if change[k]>k:
            ls[i]=str(change[k])
            flag=1
        elif flag==1 and change[k]<k:
            break
    
    return "".join(ls)
  
-----------------------------------------------------------------------
class Solution:
    def maximumNumber(self, num: str, change: List[int]) -> str:
        l = r = 0
        n = len(num)
        result = ''
        while r<n:
            curr_digit = int(num[r])
            new_digit = change[curr_digit]
            if curr_digit >= new_digit and l == r:
                result += num[r]
                l += 1
                r += 1
                continue

            if l < r and new_digit < curr_digit:
                break
            
            result += str(change[curr_digit])
            r += 1

        while r<n:
            result += num[r]
            r += 1
        
        return result
------------------------------------------------------
class Solution(object):
    def maximumNumber(self, num, change):
        """
        :type num: str
        :type change: List[int]
        :rtype: str
        """
        ans = [digit for digit in num]
        num_change = 0
        for i in range(len(num)): 
            if change[int(num[i])] > int(num[i]):
                ans[i] = str(change[int(num[i])])
                num_change += 1 

            elif change[int(num[i])] == int(num[i]):
                 pass 
            else:
                if num_change > 0:
                    return "".join(ans)
                else:
                    pass 
        

        return "".join(ans)
