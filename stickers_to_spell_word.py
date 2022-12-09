'''
We are given n different types of stickers. Each sticker has a lowercase English word on it.

You would like to spell out the given string target by cutting individual letters from your collection of stickers and rearranging them. You can use each sticker more than once if you want, and you have infinite quantities of each sticker.

Return the minimum number of stickers that you need to spell out target. If the task is impossible, return -1.

Note: In all test cases, all words were chosen randomly from the 1000 most common US English words, and target was chosen as a concatenation of two random words.
'''


class Solution:
    def minStickers(self, stickers: List[str], target: str) -> int:

        stickers = [Counter(s) for s in stickers if set(s)&set(target)]
        dp = {}
        def generate(target):
            if not target: return 0
            if target in dp: return dp[target]
            
            target_counter = Counter(target)
            res = float("inf")
            for sticker in stickers:
                if sticker[target[0]] == 0: continue
                tmp = 1 + generate("".join([letter*count for letter,count in (target_counter-sticker).items()]))

                res = min(res,tmp)
            dp[target] = res
            return res

        res = generate(target)
        return -1 if res == float("inf") else res
      
----------------------------------------------------------------------------------------------------------------------------
class Solution:
    def minStickers(self, stickers: List[str], target: str) -> int:
        freqs = [Counter(x) for x in stickers]
        
        @cache
        def fn(x):
            """Return min sticks to give x."""
            if not x: return 0 
            ans = inf
            freq = Counter(x)
            for cnt in freqs: 
                if x[0] in cnt: 
                    xx = "".join(k*v for k, v in (freq - cnt).items())
                    ans = min(ans, 1 + fn(xx))
            return ans 
        
        ans = fn(target)
        return ans if ans < inf else -1
