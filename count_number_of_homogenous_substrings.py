'''
Given a string s, return the number of homogenous substrings of s. Since the answer may be too large, return it modulo 109 + 7.

A string is homogenous if all the characters of the string are the same.

A substring is a contiguous sequence of characters within a string.
'''

#TLE

import itertools

class Solution:
    def countHomogenous(self, s: str) -> int:
        
        d = [''.join(g) for _, g in groupby(s)]

        res = 0

        for i in range(len(d)):
            item = d[i]

            res += len(list(itertools.combinations_with_replacement(d[i], 2)))

        return (res)
      
-----------------------------------------------------------------------------------------------------------------------------

'''
Explanation
cur is the previous character in type integer,
count the number of continuous same character.

We iterate the whole string character by character,
if it's same as the previous,
we increment the count,
otherwise we set it to 1.

There are count characters to start with,
ending at this current character,
in order to construct a homogenous string.
So increment our result res = (res + count) % mod.
'''

    def countHomogenous(self, s):
        res = 0
        for c, s in groupby(s):
            n = len(list(s))
            res += n * (n + 1) / 2
        return res % (10**9 + 7)
      
------------------------------------------------------------------------------  

'''
For each group of sequential characters say 'aaaa'
there are 1 + 2 + 3 + 4 possible homogenous substrings
4 'a', 3 'aa, '2 'aaa', 1 'aaaa'.
For 'a'*n there are (n + 1) * n / 2 possible homogenous substrings.

Collect the string into subgroups, itertools.groupby is a nifty tool for this.
'abcaadee' -> [['a'], ['b'], ['c'], ['a', 'a'], ['d'], ['e', 'e']].
Then the length of each subgroup is the number of sequential characters.

Iterate over the groups and add (n + 1) * n / 2 to the result.
'''

class Solution:
    def countHomogenous(self, s: str) -> int:
        MOD = 10**9 + 7
        groups = [list(g) for k, g in itertools.groupby(s)]
        res = 0
        for g in groups:
            n = len(g)
            res += (n + 1) * n // 2
        return res % MOD
      
----------------------------------------------------------------------------------------------------------------     

We just need to find the length of string + number of combinations of each homogenous substring (of length greater than 1) present in the string

If s='aa', then possible combinations is just 1 which is 'aa'
I'm considering only aa and not individual a's because length should be greater than 1

If s='aaa', then possible combinations are 'aa','aa' and 'aaa'
If s='aaaa', then possible combinations are 'aa','aa','aa','aaa','aaa','aaaa'
If s='aaaaa', then possible combinations are 4 sets of 'aa', 3 sets of 'aaa' , 2 sets of 'aaaa' and 'aaaaa' itself

So, the pattern is,
image

For nth term, the no. of possible combinations is (n*(n-1))/2
Example - For 7, it is (7*6)/2 = 21

So, the logic is traverse the string and if s[i] equals s[i-1],
then increment the count where count is the length of homogenous substring formed thus far

When s[i] does not equals to s[i-1], then current homogenous substring has come to an end.
Add (count*(count-1))/2 to res and reset count to 1

class Solution:
    def countHomogenous(self, s: str) -> int:
        res, count, n = 0, 1, len(s)
        for i in range(1,n):
            if s[i]==s[i-1]:
                count+=1
            else:
                if count>1:
                    res+=(count*(count-1)//2)
                count=1    
        if count>1:
            res+=(count*(count-1)//2)
        return (res+n)%(10**9+7)
