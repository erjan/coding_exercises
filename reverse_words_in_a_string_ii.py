'''
Given a character array s, reverse the order of the words.

A word is defined as a sequence of non-space characters. The words in s will be separated by a single space.

Your code must solve the problem in-place, i.e. without allocating extra space.

IT MUST BE DONE IN-PLACE!!!!!!!!!!!!!!!!!!

'''
-----------------------
class Solution(object):
    def reverseWords(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
#       Reverse the whole array
        i=0
        j=len(s)-1
        while i<j:
            s[i],s[j]=s[j],s[i]
            i+=1
            j-=1
#       Reverse each word
        i=0
        j=0
        left=0
        right=0
        while j<len(s):
            while j<len(s) and s[j]!=" ":
                j+=1
            right=j-1
            left=i
            while left<right:
                s[left],s[right]=s[right],s[left]
                left+=1
                right-=1
            i=j+1
            j+=1
        return s
      
-----------------------
class Solution(object):
    def reverseWords(self, s):     
        s[:] = list(' '.join(reversed(''.join(s).split(' '))))
        
        
------------------------------
class Solution:
    def reverseWords(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        """
        first reverse the entire array - this will make the words appear in correct order
        then reverse each word thmselves -
        """
        self.reverse(s, 0, len(s)-1) # reverse all the words to get correct order
        
        # now find each word and reverse the word
        left, right = 0, 0
        while right <= len(s):
            if right == len(s) or s[right] == " ":
                self.reverse(s, left, right-1)
                left = right+1
            right+=1
    
    def reverse(self, s, left, right):
        while left < right:
            s[left], s[right] = s[right], s[left]
            left+=1
            right-=1
            
            
------------------------------
class Solution:
    def reverseWords(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        n = len(s)
        start = 0
        for i in range(len(s)): # O(n) + O(n/2) since we are at most going through the array one time for the swap of every word and we are also only looping until half of the word to swap it
            if i < n // 2:
                s[i],s[n - i -1] = s[n - i - 1],s[i]
            if s[i] == " ":
                count = 0
                for j in range(start,start + (i - start) // 2): 
                    s[j],s[i - count - 1] = s[i - count - 1],s[j]
                    count += 1
                start = i + 1
        count = 0
        for i in range(start,start + (n - start) //2): 
            s[i],s[n - 1 -count] = s[n - 1 - count],s[i]
            count += 1
        return s
	```
