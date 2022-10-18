'''
Given a positive integer n, find the smallest integer which has exactly the same digits existing in the integer n and is greater in value than n. If no such positive integer exists, return -1.

Note that the returned integer should fit in 32-bit integer, if there is a valid answer but it does not fit in 32-bit integer, return -1.
'''

from itertools import permutations

class Solution:
    def nextGreaterElement(self, n: int) -> int:
        all_nums_of_same_digits = [int(''.join(i)) for i in set(permutations(str(n)))]
        all_nums_of_same_digits.sort()
        i = all_nums_of_same_digits.index(n)
        try:
            return all_nums_of_same_digits[i + 1] if all_nums_of_same_digits[i + 1] <= 2**31 else -1
        except:
            return -1
            
----------------------------------------------------------------------------------------------------------

sjoin's avatar
sjoin
299
Last Edit: December 25, 2020 8:00 PM

459 VIEWS

This solution is based on the protocol of C++ next_permutation(), which permutes the array into the next permutation in lexicographical order with respect to <. It returns True if such a next permutation exists.

@Ritik26 has a good explaination on how next_permutation() works in this post. The code below is a more condensed implementation of the same idea, where i is where the first element smaller than the right, j == i + 1, k is where l[k] is "just greater than" l[i]. We don't need to sort but just reverse l[j:] because we know it is already in descending order.

def next_permutation(l):
    """implementing C++ <algorithm> next_permutation()."""
    n = len(l)
    if n <= 1:
        return False
    i = n - 1
    while True:
        j = i
        i -= 1  
        if l[i] < l[j]:
            k = n - 1
            while not (l[i] < l[k]):  
                k -= 1
            l[i], l[k] = l[k], l[i]
            l[j:] = reversed(l[j:])
            return True
        if i == 0:  
                l.reverse()
                return False 

class Solution:
    def nextGreaterElement(self, n: int) -> int:
        l = list(str(n))
        has_next = next_permutation(l)
        ans = int(''.join(l))
        return ans if has_next and ans < 2 ** 31 else -1
----------------------------------------------------------------------------------------------------------------------
 def nextGreaterElement(self, n: int) -> int:
        s = list(str(n))
        
        
        fst = -1
        for i in range(len(s)-2,-1,-1):
            if s[i]<s[i+1]:
                fst = i
                break
        if fst==-1 :
            return -1
        
        scd = -1
        for i in range(len(s)-1,-1,-1):
            if s[i]>s[fst]:
                scd = i
                break
        
        s[fst],s[scd]=s[scd],s[fst]
        
        s[fst+1:]=s[fst+1:][::-1]
        
        ans = int(''.join(s))
        
        return ans if ans < 2147483648 else -1
        
-----------------------------------------------------------------------------------------------------------------
def nextGreaterElement(self, n: int) -> int:
    if n == 0:
        return -1
    
    nums = list(str(n))
    ln = len(nums)
    i = ln-1
    # find the first non increasing sequence from the right
    while i > 0:
        if nums[i-1] < nums[i]:
            break
        i -= 1
    
    #this is the number to be replaced as it is smaller
    # than any other element on the right of it
    i -= 1  
    
    if i < 0:
        return -1

    # look for the min largest number greater than nums[i]
    # and swap it and sort the rest
    temp = ln-1
    while temp > i:
        if nums[i] < nums[temp]:
            break
        temp -= 1
    
    nums[i], nums[temp] = nums[temp], nums[i]
    
    #sort rest of the stuff from [i+1, ln-1]
    nums[i+1:] = sorted(nums[i+1:]) 
    res = int("".join(nums))
    return  res if (res > n and res <= (2**31-1)) else -1
    
-----------------------------------------------------------------------------------------------
class Solution:
    def nextGreaterElement(self, n: int) -> int:
        digits = list(str(n))
        j = i = len(digits)-1
        while i and digits[i] <= digits[i-1]: i-=1
        if i == 0: return -1
        while digits[j] <= digits[i-1]: j-=1
        digits[j],digits[i-1] = digits[i-1],digits[j]
        digits[i:] = digits[i:][::-1]
        res = ''.join(digits)
        return res if int(res) < 2**31 else -1
