You are given a string s consisting of lowercase English letters.

Your task is to find the maximum difference diff = a1 - a2 between the frequency of characters a1 and a2 in the string such that:

a1 has an odd frequency in the string.
a2 has an even frequency in the string.
Return this maximum difference.
-----------------------------------------------------

  class Solution:
    def maxDifference(self, s: str) -> int:
        freq = dict(Counter(s))

        freq = [[k,v] for k,v in freq.items()]
        freq.sort(key = lambda x: x[1])

        freq = [v for k,v in freq]
        max_odd = max(list(filter(lambda x: x%2 == 1,freq)))

        min_ev = min(list(filter(lambda x: x%2 == 0, freq)))
        return max_odd-min_ev
