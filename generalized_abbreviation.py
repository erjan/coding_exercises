'''
A word's generalized abbreviation can be constructed by taking any number of non-overlapping and non-adjacent substrings and replacing them with their respective lengths.

For example, "abcde" can be abbreviated into:
"a3e" ("bcd" turned into "3")
"1bcd1" ("a" and "e" both turned into "1")
"5" ("abcde" turned into "5")
"abcde" (no substrings replaced)
However, these abbreviations are invalid:
"23" ("ab" turned into "2" and "cde" turned into "3") is invalid as the substrings chosen are adjacent.
"22de" ("ab" turned into "2" and "bc" turned into "2") is invalid as the substring chosen overlap.
Given a string word, return a list of all the possible generalized abbreviations of word. Return the answer in any order.
'''

class Solution:
    def generateAbbreviations(self, word: str) -> List[str]:
        results = []
        
        def traverse(accum, idx):
            if idx >= len(word):
                results.append(accum)
            else:
                traverse(accum + word[idx], idx + 1) # keep this letter as is
                if idx == 0 or (len(accum) > 0 and accum[-1].isalpha()): # if the last processed symbol is not a number
                    for shiftSize in range(1, len(word) - idx + 1): # consume `shiftSize` next letters up to the end of the original word, turn them into a single number
                        traverse(accum + str(shiftSize), idx + shiftSize)
                        
        traverse("", 0)
                        
        return results
      
-------------------------------------

For each index, you have two choices - abbreviate, or not to abbreviate.
Basically, you try both possibilities for each step.
However, you also need to consider if the last element from the previous step is number or alphabet because it changes the next step. (i.e., The numbers cannot be put continuously.)

class Solution:
    def generateAbbreviations(self, word: str) -> List[str]:
        def rec(idx, curr_list):
            if idx == L:
                res.append(''.join(curr_list))
                return
            
            #Abbreviate
            if curr_list and curr_list[-1].isdigit():
                curr_list[-1] = str(int(curr_list[-1]) + 1)
                rec(idx + 1, curr_list)
                curr_list[-1] = str(int(curr_list[-1]) - 1)
            else:
                rec(idx + 1, curr_list + ['1'])
            
            #Not to abbreviate
            rec(idx + 1, curr_list + [word[idx]])
                
        L = len(word)
        res = []
        rec(0, [])
        return res
--------------------------------------------------

Consider the example where the input string is "abc"

Let's look at the first character "a".
Now let's assume we have the answer to the subproblem "bc" which is ["bc", "1c", "b1", "2"]
Now how do we add "a" to this subproblem?

For every string in our subproblem's answer, we add an "a" to the beginning of the substring. This case is trivial
For every string in our subproblem's answer, we add a "1" to the beginning of the substring. This case requires additional care to make sure we update the number at the beginning of the string
"a" + ["bc", "1c", "b1", "2"] = ["abc", "a1c", "ab1", "a2"]
"1" + ["bc", "1c", "b1", "2"] = ["1bc", "2c", "1b1", "3"]

The answer is the union of these 2 arrays.

class Solution:
    def generateAbbreviations(self, s: str) -> List[str]:
        result = []

        if len(s) == 1:
            return [s, '1']
        substrings = self.generateAbbreviations(s[1:])

        # Add s[0] to the beginning of every substring
        for sub in substrings:
            result.append(s[0] + sub)

        # Add 1 to the beginning of every substring, combine nums if necessary
        for sub in substrings:
            if sub[0].isnumeric():
                i = 0
                while i < len(sub) and sub[i].isnumeric():
                    i += 1
                num = 1 + int(sub[0:i])
                result.append(str(num) + sub[i:])
            else:
                result.append('1' + sub)
        return sorted(result)
---------------------------------------------------------------

class Solution:
    def generateAbbreviations(self, word: str) -> List[str]:
        
        @lru_cache(maxsize=None)
        def doAbbreviations(start: int, replace: bool) -> List[str]:
            out: List[str] = []
            
            if start + 1 == len(word) + 1:
                return [""]
            
            for i in range(start + 1, len(word) + 1):
                if replace:
                    part = str(i - start)
                else:
                    part = word[start:i]
                for p in doAbbreviations(i, not replace):
                    out.append(part + p)
                    
            return out
                            
        return doAbbreviations(0, True) + doAbbreviations(0, False)
--------------------------------------------------

Algo
Define fn(i) to return abbreviation of word[i:].

Implementation (bottom-up)

class Solution:
    def generateAbbreviations(self, word: str) -> List[str]:
        
        def fn(i):
            """Return abbreviation of word[i:]."""
            if i == len(word): return [(0, "")]
            ans = []
            for c in ("1", word[i]):
                for x, y in fn(i+1):
                    if c.isdigit(): ans.append((x+1, y))
                    else: ans.append((0, c + (str(x) if x else "") + y))
            return ans 
        
        return [(str(x) if x else "") + y for x, y in fn(0)]
Implementation (top-down)

class Solution:
    def generateAbbreviations(self, word: str) -> List[str]:
        
        def fn(i, s="", n=0):
            """Populate ans via backtracking."""
            if i == len(word): return ans.append(s + (str(n) if n else ""))
            fn(i+1, s, n+1)
            fn(i+1, s + (str(n) if n else "") + word[i], 0)
        
        ans = []
        fn(0)
        return ans 
Analysis
Time complexity O(2^N)
Space complexity O(2^N)

      
      
      
