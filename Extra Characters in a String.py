

'''
Companies
You are given a 0-indexed string s and a dictionary of words dictionary. You have to break s into one 
or more non-overlapping substrings such that each substring is present in dictionary. There may be some extra
characters in s which are not present in any of the substrings.

Return the minimum number of extra characters left over if you break up s optimally.
'''


#wrong solution
class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        print(s)
        for word in dictionary:
            print()
            print(s)
            if s.find(word) != -1:
                print()
                first = s.find(word)
                last = s.find(word) + (len(word) - 1)
                print("found: " + word)
                print("first char is at %d" % first)
                print("last char is at %d" % last)

                s = s[:first] + s[last + 1 :]

        #print("len of remaining str s is %d" % len(s))
        return len(s)

--------------------------------------------------------------------------------------------------------
class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        dp, n = [0]*(len(s)+1), len(s)
        for i in range(n):
            dp[i+1] = dp[i] + 1 # in the worst case skip one character  
            for w in dictionary:
                if s[0:i+1].endswith(w): # otherwise if it ends with a dictionary word
                    dp[i+1] = min(dp[i+1], dp[i+1-len(w)]) # check i+1-len(w) to adjust the min
        return dp[-1]
