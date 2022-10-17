'''
You are given two strings a and b of the same length. Choose an index and split both strings at the same index, splitting a into two strings: aprefix and asuffix where a = aprefix + asuffix, and splitting b into two strings: bprefix and bsuffix where b = bprefix + bsuffix. Check if aprefix + bsuffix or bprefix + asuffix forms a palindrome.

When you split a string s into sprefix and ssuffix, either ssuffix or sprefix is allowed to be empty. For example, if s = "abc", then "" + "abc", "a" + "bc", "ab" + "c" , and "abc" + "" are valid splits.

Return true if it is possible to form a palindrome string, otherwise return false.

Notice that x + y denotes the concatenation of strings x and y.
'''



class Solution:
    def checkPalindromeFormation(self, a: str, b: str) -> bool:
        n=len(a)
        
        # Brute Force: TLE
        # for i in range(n):
        #     s1=a[:i]+b[i:]
        #     s2=b[:i]+a[i:]
        #     if s1==s1[::-1] or s2==s2[::-1]:
        #         return True
        # return False
        
        # 2 pointers
        def check(s1,s2):
            l=0
            r=n-1
            while l<=r and s1[l]==s2[r]:
                l+=1
                r-=1
            
            if l>r or s1[l:r+1]==s1[l:r+1][::-1] or s2[l:r+1]==s2[l:r+1][::-1]:
                return True
            return False
        return check(a,b) or check(b,a)
      
-------------------------------------------------------------------------------------------------------
class Solution:
    def checkPalindromeFormation(self, a: str, b: str) -> bool:
        if a == a[::-1] or b == b[::-1]:
            return True
        len_a = len(a)
        len_a1 = len_a - 1

        i = 0
        while a[i] == b[len_a1 - i]:
            i += 1
        p1 = a[:i] + b[i:]
        p2 = a[:len_a - i] + b[len_a - i:]
        if p1 == p1[::-1] or p2 == p2[::-1]:
            return True

        i = 0
        while b[i] == a[len_a1 - i]:
            i += 1
        p1 = b[:i] + a[i:]
        p2 = b[:len_a - i] + a[len_a - i:]
        if p1 == p1[::-1] or p2 == p2[::-1]:
            return True

        return False
      
-------------------------------------------------------------------------
class Solution:
    def checkPalindromeFormation(self, a: str, b: str) -> bool:
        for x, y in [[a, b], [b, a]]:
            i, j = 0, len(x) - 1
            while x[i] == y[j]:
                i += 1
                j -= 1
            if ((midx := x[i:j+1]) == midx[::-1] or
                (midy := y[i:j+1]) == midy[::-1]):
                return True
        return False 
