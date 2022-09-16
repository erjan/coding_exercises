'''
Given a string s, return the maximum number of ocurrences of any substring under the following rules:

The number of unique characters in the substring must be less than or equal to maxLetters.
The substring size must be between minSize and maxSize inclusive.
'''

def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        # count frequency of characters
        count = collections.Counter()
        
        # Check only for minSize
        for i in range(len(s) - minSize + 1):
            t = s[i : i+minSize]
            if len(set(t)) <= maxLetters:
                count[t] += 1
        
        return max(count.values()) if count else 0
        
---------------------------------------------

class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        s1 = []
        count ={}
        while minSize <= maxSize:
            for i in range(0,len(s)):
                if (i+ minSize) <=len(s) and len(set(s[i: i+ minSize])) <= maxLetters:
                    s1.append(s[i: i+ minSize])
            minSize += 1         
        for i in s1:
            count[i] = count[i] + 1 if i in count  else 1      
        return max(count.values()) if count else 0
        
-----------------------------------------------------------
def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
    d = defaultdict(int)
    for i in range(len(s)-minSize+1):
        if len(set(s[i:i+minSize]))<=maxLetters:
            d[s[i:i+minSize]] +=1
    return max(d.values()) if d else 0
