'''
You are given a string s of even length consisting of digits from 0 to 9, and two integers a and b.

You can apply either of the following two operations any number of times and in any order on s:

Add a to all odd indices of s (0-indexed). Digits post 9 are cycled back to 0. For example, if s = "3456" and a = 5, s becomes "3951".
Rotate s to the right by b positions. For example, if s = "3456" and b = 1, s becomes "6345".
Return the lexicographically smallest string you can obtain by applying the above operations any number of times on s.

A string a is lexicographically smaller than a string b (of the same length) if in the first position where a and b differ, string a has a letter that appears earlier in the alphabet than the corresponding letter in b. For example, "0158" is lexicographically smaller than "0190" because the first position they differ is at the third letter, and '5' comes before '9'.
'''

import collections

class Solution:
    def findLexSmallestString(self, s: str, a: int, b: int) -> str:
        seen = set()
        deque = collections.deque([s])

        while deque:
            #print(deque)
            curr = deque.popleft()
            seen.add(curr)
            
            #1.add
            ad = self.add_(curr, a)
            if ad not in seen:
                deque.append(ad)
                seen.add(ad)

            
            #2. rotate:
            ro = self.rotate_(curr, b)
            if ro not in seen:
                deque.append(ro)
                seen.add(ro)

        return min(seen)
        
        
    def add_(self,s,a):
        res = ''
        for idx, i in enumerate(s):
            if idx % 2 == 1:
                num = (int(i) + a) % 10
                res += str(num)
            else:
                res += i
                
        return res
    
    
    def rotate_(self, s, b):
        idx = len(s)-b
        res = s[idx:] + s[0:idx]
        return res
-------------------------------------------
def add(s, a):
    return ''.join([str((int(x) + a)%10) if i%2==1 else x for i, x in enumerate(s)])

def move(s, b):
    return ''.join([s[i - b] for i in range(len(s))])

class Solution:
    def dp(self, s):
        if s in self.visited:
            return
        if int(self.min_s) > int(s):
            self.min_s = s
        self.visited.add(s)        
        self.dp(add(s, self.a))        
        self.dp(move(s, self.b))              
        
    def findLexSmallestString(self, s: str, a: int, b: int) -> str:
        self.visited = set()
        self.min_s = s
        self.a = a
        self.b = b
        self.dp(s)
        return self.min_s
      
