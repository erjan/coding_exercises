'''
A valid IP address consists of exactly four integers separated by single dots. Each integer is between 0 and 255 (inclusive) and cannot have leading zeros.

For example, "0.1.2.201" and "192.168.1.1" are valid IP addresses, but "0.011.255.245", "192.168.1.312" and "192.168@1.1" are invalid IP addresses.
Given a string s containing only digits, return all possible valid IP addresses that can be formed by inserting dots into s. You are not allowed to reorder or remove any digits in s. You may return the valid IP addresses in any order.

 

Example 1:

Input: s = "25525511135"
Output: ["255.255.11.135","255.255.111.35"]
Example 2:

Input: s = "0000"
Output: ["0.0.0.0"]
Example 3:

Input: s = "101023"
Output: ["1.0.10.23","1.0.102.3","10.1.0.23","10.10.2.3","101.0.2.3"]
 

Constraints:

1 <= s.length <= 20
s consists of digits only.
'''

class Solution(object):
    def restoreIpAddresses(self, s):
        res = []
        self.dfs(s, 0, "", res)
        return res
    
    def dfs(self, s, idx, path, res):
        if idx > 4:
            return 
        if idx == 4 and not s:
            res.append(path[:-1])
            return 
        for i in range(1, len(s)+1):
            if s[:i]=='0' or (s[0]!='0' and 0 < int(s[:i]) < 256):
                self.dfs(s[i:], idx+1, path+s[:i]+".", res)
---------------------------------------------------------------------------

TL;DR
Iterative solution. No pruning done.
Python
  def restoreIpAddresses(self, s):
    ret = []
    for a in range(1, 4):
      for b in range(1, 4):
        for c in range(1, 4):
          d = len(s) - a - b - c
          """
          Last number must use all remaining digits. Check;
          1. The size of the last number is valid
          2. Every number uses 1 digit for 0 and is less than 255 if using 3 digits
          """
          if (1 <= d <= 3 and
            (1 == a or '0' != s[0        ]) and (a != 3 or s[         :a        ] <= "255") and
            (1 == b or '0' != s[a        ]) and (b != 3 or s[a        :a + b    ] <= "255") and
            (1 == c or '0' != s[a + b    ]) and (c != 3 or s[a + b    :a + b + c] <= "255") and
            (1 == d or '0' != s[a + b + c]) and (d != 3 or s[a + b + c:         ] <= "255")):
            ret.append('.'.join([s[0:a], s[a:a + b], s[a + b:a + b + c], s[a + b + c:]]))
    return ret
  
  
  
  -----------------------------------------------------------------------------------------
  The underlying backtracking algorithm is the same with problem 39/40/46/47/90.
But this problem has more constraints thus needs to consider how to include each constraint in the codes.
Firstly, the condition to append one single answer to the answer list. I started with len(s) == 0 but found out I could have something like 0.0.0.0.0, which is an invalid IP address. Thus I added a counter k for each '.' and k==4 is added to the condition

Second, I need to stop the operation if either hit the end(len(s)==0) or k==4.

Also, I need to include some validation conditions like below wihin the loop.
'''
if int(s[:i+1])>255:
continue
if i != 0 and s[0]=='0':
'''

The backtracking process illustrated below for better understanding. Also refer to my post for these backtracking problems for your information.
39. Combination Sum
40. Combination Sum II
46. Permutations

image

'''
def restoreIpAddresses(self, s: str) -> List[str]:
    ans = []
    k = 0
    self.backtrack(s,ans,k,'')
    return ans
    


def backtrack(self, s, ans,k, temp=''):
    if k==4 and len(s)==0:
        ans.append(temp[:-1])
        return
    if k==4 or len(s)==0:
        return
    
    for i in range(3):
        if k>4 or i+1>len(s):
            break
        
        if int(s[:i+1])>255:
            continue
        if i != 0 and s[0]=='0':
            continue
                
        self.backtrack(s[i+1:], ans, k+1, temp+s[:i+1]+'.')
        
-------------------------------------------------------------------------------------------
def restoreIpAddresses(self, s: str) -> List[str]:
        path = []
        result = []
        self.dfs(s, path, result)
        return result
    
    def dfs(self, s: str, path: List, result: List):
        
        if not s and len(path) == 4:
            s = '.'.join(path[::-1])
            result.append(s)
            return
        elif len(path) == 4: return 
        else:
            for i in range(1, min(3, len(s))+1):
                if int(s[:i]) >= 0 and int(s[:i]) <= 255:
                    if i > 1 and s[0]=='0': continue
                    else: self.dfs(s[i:], [s[:i]]+path, result)
            return
----------------------------------------------------------------------------

class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res = []
        
        def backtrack(comb, s, level):
            if (level == 0) and (s == ""):
                res.append(comb[:-1])
            elif (level != 0):
                for i in range(1,min(3+1, len(s)+1)):
                    if (i > 1) and (s[0] == '0'): # cannot start with '0', i.e. '1.001.0.1'
                        continue
                    if ( 0<= int(s[0:i]) <=255 ) :
                        backtrack(comb+s[0:i]+'.', s[i:], level-1)
        
        backtrack("", s, 4)
        return res
------------------------------------------------------------

class Solution:
    def __init__(self):
        self.ans=[]
    def restoreIpAddresses(self, s: str) -> List[str]:
        self.recurse(s,3,0)
        return self.ans
    
    def recurse(self,s:str,dots:int,idx:int)->None:
        if dots==0:
            if self.isValid(s[idx:]): 
                self.ans.append(s)
            return 
        dots-=1
        self.recurse(s[:idx+1]+"."+s[idx+1:],dots,idx+2)
        if self.isValid(s[idx:idx+2]):
            self.recurse(s[:idx+2]+"."+s[idx+2:],dots,idx+3)
        if self.isValid(s[idx:idx+3]):
            self.recurse(s[:idx+3]+"."+s[idx+3:],dots,idx+4)
        
    def isValid(self,s:str)->bool:
        if len(s)==0:
            return False
        if len(s)==1: 
            return True
        if len(s)==2: 
            return (s[0]!="0")
        return (s[0]!="0") and int(s)<=255
        
        
        
            
                

