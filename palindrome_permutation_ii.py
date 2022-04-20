'''
Given a string s, return all the palindromic permutations (without duplicates) of it.

You may return the answer in any order. If s has no palindromic permutation, return an empty list.

 

Example 1:

Input: s = "aabb"
Output: ["abba","baab"]
Example 2:

Input: s = "abc"
Output: []
'''

If you have some familiarity with palindromes, you should know that a palindrome can only be constructed from a set of letters if and only if at most one character has an odd count. If so, this odd-count character will be in the middle of the string.

We can construct palindromes by considering two scenarios, either there is one character that has an odd count, or all characters have even counts.

If all characters have even counts, the process of backtracking is simple. For each remaining character, we simply add it to each side of the current solution. One branch of the backtracking solution would grow like this:

initial counter: {'a' : 2, 'b' : 2, 'c' : 2}

cur: '', remaining: {'a' : 2, 'b' : 2, 'c' : 2}
cur: 'aa', remaining: {'b' : 2, 'c' : 2}
cur: 'baab', remaining: {'c' : 2}
cur: 'cbaabc', remaining: {} # no more characters, add cur to result and backtrack

If one character has an odd count, we start with the odd-count character as cur and repeat the same process. It would look something like this:

initial counter: {'a' : 2, 'b' : 2, 'c' : 2, 'i' : 1}

cur: 'i', remaining: {'a' : 2, 'b' : 2, 'c' : 2}
cur: 'aia', remaining: {'b' : 2, 'c' : 2}
cur: 'baiab', remaining: {'c' : 2}
cur: 'cbaiabc', remaining: {} # no more characters, add cur to result and backtrack

Once you've made this observation this should be a standard backtracking problem.

def generatePalindromes(self, s: str) -> List[str]:
        counter = Counter(s)
        res = []
        
        def backtrack(cur=""):
            if not counter:
                res.append(cur)
                return
            for c in list(counter.keys()):
				counter[c] -= 2
                if not counter[c]:
					del counter[c]
                backtrack(c+cur+c)
                counter[c] += 2

        oddCounts = [c for c in counter if counter[c]%2] # The characters in counter with odd count
        
        if not len(oddCounts): # if no odd chars, we can simply backtrack
            backtrack()
            
        if len(oddCounts) == 1: # if exactly one odd char, backtrack with oddChar in the middle of string
            oddChar = oddCounts[0]
            counter[oddChar] -= 1
            if not counter[oddChar]:
                del counter[oddChar]
            backtrack(oddChar)
            
        return res
---------------------------------------------------

Take aabbbcc as an example

counter would be {"a":2, "b":3, "c":2}

After preprocess: baseStr = "abc", mid = "b" (if there is no char happens odd times, mid = "")

Then use backtracking to find all the permutation of baseStr,

the valid palindrome would be "permuStr + mid + reverseOfPermuStr"

def generatePalindromes(self, s):
    counter = collections.Counter(s)
    odds = filter(lambda x: x % 2, counter.values())
    if len(odds) > 1:
        return []
    baseStr, mid = self.preProcess(counter)
    return self.backTracking(baseStr, 0, mid, [baseStr + mid + baseStr[::-1]])
    
def preProcess(self, counter):
    baseStr = mid = ""
    for char in counter:    
        if counter[char] % 2:
            mid = char
        baseStr += char*(counter[char]/2)
    return baseStr, mid
    
def backTracking(self, s, idx, mid, ans):
    if idx == len(s) - 1:
        return ans
    for i in range(idx, len(s)):
        if i >= 1 and s[i] == s[i-1] == s[idx]:
            continue #no need to go deeper if swap would be the same
        #Swap s[idx] with s[i]
        if i != idx:
            permu = s[:idx] + s[i] + s[idx+1:i] + s[idx] + s[i+1:] 
            ans.append(permu + mid + permu[::-1])
        else:
            permu = s
        self.backTracking(permu, idx+1, mid, ans)
    return ans
-------------------------------------------------

Use collections.Counter and itertools.permutations

class Solution(object):
    def generatePalindromes(self, s):
        d = collections.Counter(s)
        m = tuple(k for k, v in d.iteritems() if v % 2)
        p = ''.join(k*(v/2) for k, v in d.iteritems())
        return [''.join(i + m + i[::-1]) for i in set(itertools.permutations(p))] if len(m) < 2 else []
----------------------------------------------------

Idea:

Generate only those permutations which are already palindromes.
If a str is palindrome eligible: See [Comment 1]
Only use half the str and generate permutations for it.
The way half a str is built using frequencies guarantees they will be palndromic. See [Commnet 2]
This eliminates the need to check later if the permtation at the leaf is a palindrome which amplifies the big-o complexity by O(N) like we saw in Approach 1.
Then append the other half (which should be the the same first half but reversed) See [Comment 3]
When it comes to odd-freq-chars. There are two possible scnearios:
odd-freq-char has a freq of 1 -- [Comment 4]

Only consider Half of even-freq chars
Ignore odd-freq char for now
Use a flag to indicate you've found an odd-freq-char
Store the odd-freq-char (remember this char has freq = 1)
odd-freq-char has a freq > 1 (for ex: 3, 5, 7 . . . )

Only consider Half of even-freq chars
Decrement odd-freq for oddFreqChar by 1 -> turning it into even-freq char -> now that's even -> then take half of it frq as well
Visual Illustrations
image

image

Big-O:

Time: O(N*N!)
Code:

def generatePalindromes(s):

		# is Panlindrome eligible
        def isPalindromicEligibile(s):
            d = {}
            for ch in s:
                if ch in d:
                    d[ch] += 1
                else:
                    d[ch] = 1
            # if more one oddFreqChar -> invalid - ineligible
            odds = 0
            hasOddFreqChar = False
            for k in d:
                if d[k] % 2 != 0: # odd
                    odds += 1
                    hasOddFreqChar = True
                    if odds > 1:
                        return (False, d, hasOddFreqChar)
            return (True, d, hasOddFreqChar)
            
        # recursive helper
        def recursive(s, path="", res=[]):
            if not s:
                # time to add the next half back -- [Comment 3]
                # check the 2 scnearios -> zero odd-freq-chars or non-zero
                if hasOddFreqChar:
                    res.append(path + oddFreqChar + path[::-1])
                else:
                    res.append(path + path[::-1])
            for i in range(len(s)):
                if i > 0 and s[i] == s[i-1]:
                    continue
                newS = s[:i] + s[i+1:]
                path = path + s[i]
                recursive(newS, path, res)
                path = path[:-1]
            return res
        
        # main
        isPalindromEligible, d, hasOddFreqChar = isPalindromicEligibile(s) # -- [Comment 1]
        if not isPalindromicEligibile(s):
            return []
        if isPalindromEligible:
            # edge case - str has one distinct char
            if len(d) == 1:
                return [s]
            # only take half of the d:
            halfStr = ""
            for k in d:
                if d[k] % 2 == 0:
                    halfStr += k*(d[k]//2)  # -- [Comment 2]
                else:
                    if d[k] > 1: # -- [Comment 4]
                        halfStr += k*((d[k]-1)//2) 
                    oddFreqChar = k 
            return recursive(halfStr, "", [])
          ---------------------------------------------------------------
def generatePalindromes(self, s):
        kv = collections.Counter(s)
        mid = [k for k, v in kv.iteritems() if v%2]
        if len(mid) > 1:
            return []
        mid = '' if mid == [] else mid[0]
        half = ''.join([k * (v/2) for k, v in kv.iteritems()])
        half = [c for c in half]
        
        def backtrack(end, tmp):
            if len(tmp) == end:
                cur = ''.join(tmp)
                ans.append(cur + mid + cur[::-1])
            else:
                for i in range(end):
                    if visited[i] or (i>0 and half[i] == half[i-1] and not visited[i-1]):
                        continue
                    visited[i] = True
                    tmp.append(half[i])
                    backtrack(end, tmp)
                    visited[i] = False
                    tmp.pop()
                    
        ans = []
        visited = [False] * len(half)
        backtrack(len(half), [])
        return ans
      
      ------------------------------------------------------------------------------------
      class Solution:
    def __init__(self):
        self.ans = []
        
    def generate(self, counter, mid, n):
        if not n:
            self.ans.append(mid)
            return
        for i in counter:
            if counter[i] > 0:
                counter[i] -= 2
                self.generate(counter, i + mid + i, n-2)
                counter[i] += 2
        
    def generatePalindromes(self, s: str) -> List[str]:
        counter = collections.Counter(s)
        cnt = 0
        c = None
        n = len(s)
        for i in counter:
            if counter[i] % 2:
                cnt += 1
                c = i
        if cnt > 1:
            return []
        else:
            if cnt:
                counter[c] -= 1
                self.generate(counter, c, n-1)
            else:
                self.generate(counter, '', n)
            return self.ans
      
  
      
