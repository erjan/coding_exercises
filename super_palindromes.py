'''
Let's say a positive integer is a super-palindrome if it is a palindrome, and it is also the square of a palindrome.

Given two positive integers left and right represented as strings, return the number of super-palindromes integers in the inclusive range [left, right].

 
 '''

class Solution:
def superpalindromesInRange(self, left: str, right: str) -> int:
    
    left = int(left)
    right= int(right)
    limit= 100000
    c=0
    
    def is_pal(num):
        return str(num)==str(num)[::-1]
    
    #For even length palindrome
    for i in range(limit):
        s=str(i)
        s=s+s[::-1]
        p=int(s)
        p2=p**2
        if p2>right:
            break
        if p2>left and is_pal(p2):
            c+=1
    
    #For odd length palindrome
    for i in range(1,limit):
        s=str(i)
        s=s+s[::-1][1:]
        p=int(s)
        p2=p**2
        if p2>right:
            break
        if p2>=left and is_pal(p2):
            c+=1
    
    return c
  -------------------------------------------------------------------------------------------------------
  class Solution:
    def superpalindromesInRange(self, left: str, right: str) -> int:
        left  = int(left)
        right = int(right)
        ans = 0
		# for odd length numbers like 1234321
        for i in range(1, 100000):
            s1 = str(i)
            s2 = s1[-2::-1]
            num = int(s1 + s2)**2
            if num > right:
                break
            if num >= left and str(num) == str(num)[::-1]:
                ans += 1
				
        # for even length numbers like 12344321
        for i in range(1, 100000):
            s1 = str(i)
            s2 = s1[::-1]
            num = int(s1 + s2)**2
            if num > right:
                break
            if num >= left and str(num) == str(num)[::-1]:
                ans += 1
        return ans
            
  
  
