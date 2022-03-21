'''
Given a string s, return the length of the longest substring between two 
equal characters, excluding the two characters. If there is no such substring return -1.

A substring is a contiguous sequence of characters within a string.
'''


class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        
        if len(s) == 1:
            return -1
        d = defaultdict(list)

        for i in range(len(s)):
            if s[i] not in d:
                d[s[i]] = [i]
            else:
                d[s[i]].append(i)

        d = list(d.values())
        maxi = 0
        for i in range(len(d)):
            temp = d[i]

            if len(d[i]) != 1:

                s = max(temp) - temp[0]
                if s > maxi:
                    maxi = s

        maxi = maxi-1
        print(maxi)
        return maxi
