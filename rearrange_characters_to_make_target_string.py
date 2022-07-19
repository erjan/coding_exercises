'''
You are given two 0-indexed strings s and target. You can take some letters from s and rearrange them to form new strings.

Return the maximum number of copies of target that can be formed by taking letters from s and rearranging them.
'''

from collections import Counter

class Solution:
    def rearrangeCharacters(self, s: str, target: str) -> int:
        t = target
        tfreq = Counter(t)
        sfreq = Counter(s)

        res = 10**20

        for k in tfreq.keys():
            res = min(res, sfreq[k]//tfreq[k])
        return res
      
----------------------------------------------------------------------
class Solution:
    def rearrangeCharacters(self, s: str, target: str) -> int:
        counter_s = Counter(s)        
        return min(counter_s[c] // count for c,count in Counter(target).items())
      
      
---------------------------------------------
class Solution:
    def rearrangeCharacters(self, s: str, target: str) -> int:
        s = Counter(s)
        target = Counter(target)
        return min(s[c] // target[c] for c in target)
      
---------------------------------------------------------------------------------------

class Solution:
    def rearrangeCharacters(self, s: str, target: str) -> int:
        counter_s = Counter(s)
        res = float('inf')
        for k, v in Counter(target).items():
            res = min(res, counter_s[k] // v)
        return res
