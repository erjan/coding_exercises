'''
Given a string s and an integer k, return the maximum number of vowel letters in any substring of s with length k.

Vowel letters in English are 'a', 'e', 'i', 'o', and 'u'.
'''


class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        
        vowels = ["a","e","i","o","u"]
        
        #start point of the window
        start     = 0        
        #number of vowels in a window of k length
        window    = 0
        #answer
        maxCount  = 0
        
        #end pointer of the window of  k length
        for end in range(len(s)):
            
            #current letter
            letter = s[end]
            
            #is it in vowel ?
            if letter in vowels:
                window += 1
            
            #once the length of window is equals to k then we check for number of vowels
            #this will happen each iteration once we first get the window of length k
            if end - start + 1 == k:
                #setting the maxcount
                maxCount = max(maxCount,window)
                #first pointer value
                left = s[start]
                #if first pointer is a vowel
                #we sub from the running window of k length number of vowels as it will be missing for the next
                #iteration
                if left in vowels:
                    window -= 1
                #we shrink the window by one by movingh the start pointer to right
                start = start + 1                                
            
            #if a window has the max number of possible vowels which is k
            #then we just quit as we have gotten the largest possible value
            if maxCount == k:
                return maxCount        
        return maxCount
        
        
-------------------------------------------------------------------------------------------------------------------------------        
class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        n = len(s)
        v = 0
        for i in range(k):
            if s[i] in "aeiou":
                v += 1
        res = v
        for i in range(n - k):
            if s[i] in "aeiou":
                v -= 1
            if s[i + k] in "aeiou":
                v += 1
            res = max(res, v)
        return res
      
---------------------------------------------------------------------------------------------------      
class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        letterList = [i for i in s]
        maxCount = 0
        vowels = ['a', 'e', 'i', 'o', 'u']
        if k == 1 : 
            for i in vowels : 
                if i in letterList : 
                    return 1
        else :
            for i in range(len(letterList)-k+1) : 
                if i == 0 : 
                    toCheck = letterList[i:i+k]
                    totalVowelCount = toCheck.count('a') + toCheck.count('e') + toCheck.count('i') + toCheck.count('o') + toCheck.count('u')
                else :
                    if letterList[i-1] in vowels : 
                        totalVowelCount -= 1
                    if (letterList[i+k-1] in vowels) : 
                        totalVowelCount += 1
                if totalVowelCount > maxCount : 
                    maxCount = totalVowelCount
                    
            return maxCount
