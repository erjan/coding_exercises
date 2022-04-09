'''
A string can be abbreviated by replacing any number of non-adjacent substrings with their lengths. For example, a string such as "substitution" could be abbreviated as (but not limited to):

"s10n" ("s ubstitutio n")
"sub4u4" ("sub stit u tion")
"12" ("substitution")
"su3i1u2on" ("su bst i t u ti on")
"substitution" (no substrings replaced)
Note that "s55n" ("s ubsti tutio n") is not a valid abbreviation of "substitution" because the replaced substrings are adjacent.

The length of an abbreviation is the number of letters that were not replaced plus the number of substrings that were replaced. For example, the abbreviation "s10n" has a length of 3 (2 letters + 1 substring) and "su3i1u2on" has a length of 9 (6 letters + 3 substrings).

Given a target string target and an array of strings dictionary, return an abbreviation of target with the shortest possible length such that it is not an abbreviation of any string in dictionary. If there are multiple shortest abbreviations, return any of them.
'''

class Solution(object):
    def minAbbreviation(self, target, dictionary):
        """
        :type target: str
        :type dictionary: List[str]
        :rtype: str
        """
        self.size = len(target)
        self.wlist = [self.toNumber(target, d) \
                      for d in dictionary \
                      if len(d) == self.size]
        self.ans = (1 << self.size) - 1
        self.length = self.size
        self.dfs(0, 0, 0)
        return self.toWord(self.ans)
    def dfs(self, number, depth, length):
        if length >= self.length: return
        if depth == self.size:
            if not any(number & w == number for w in self.wlist):
                self.ans = number
                self.length = length
            return
        self.dfs((number << 1) + 1, depth + 1, length + 1)
        if length == 0 or number & 1:
            for x in range(2, self.size - depth + 1):
                self.dfs(number << x, depth + x, length + 1)
    def toNumber(self, target, word):
        ans = 0
        for x in range(self.size):
            ans <<= 1
            ans += target[x] == word[x]
        return ans
    def toWord(self, number):
        ans = ''
        cnt = 0
        for x in range(self.size):
            if number & (1 << self.size - x - 1):
                if cnt:
                    ans += str(cnt)
                    cnt = 0
                ans += target[x]
            else:
                cnt += 1
        return ans + str(cnt or '')
