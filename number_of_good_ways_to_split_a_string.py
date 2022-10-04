'''
You are given a string s.

A split is called good if you can split s into two non-empty strings sleft and sright where their concatenation is equal to s (i.e., sleft + sright = s) and the number of distinct letters in sleft and sright is the same.

Return the number of good splits you can make in s.
'''


import collections
class Solution:
    def numSplits(self, s: str) -> int:
        myS1=collections.Counter() #s1 is now empty
        myS2=collections.Counter(s) #s2 is now has all string 
        ways=0 #when len of myS1= len of myS2 --> ways+=1

        for letter in s:    
            myS1[letter]+=1
            myS2[letter]-=1
            
            if myS2[letter]==0:
                myS2.pop(letter)
                
            if len(myS1)==len(myS2):
                ways+=1 
        return ways    
      
------------------------------------------------------------------------------------------
    def numSplits(self, s: str) -> int:
        total = collections.Counter(s)
        alter = collections.Counter()
        result = 0
        for i in range(len(s)):
            char = s[i]
            total[char] -=1
            if total[char] == 0:
                del total[char]
            alter[char] += 1
            if len(total) == len(alter):
                result +=1
        return result
