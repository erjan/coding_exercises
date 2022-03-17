'''
You are given a string s. Reorder the string using the following algorithm:

Pick the smallest character from s and append it to the result.
Pick the smallest character from s which is greater than the last appended character to the result and append it.
Repeat step 2 until you cannot pick more characters.
Pick the largest character from s and append it to the result.
Pick the largest character from s which is smaller than the last appended character to the result and append it.
Repeat step 5 until you cannot pick more characters.
Repeat the steps from 1 to 6 until you pick all characters from s.
In each step, If the smallest or the largest character appears more than once you can choose any occurrence and append it to the result.

Return the result string after sorting s with this algorithm.
'''

class Solution:
    def sortString(self, s: str) -> str:
        res = []
        freq = dict(collections.Counter(s)).items()
        freq = sorted([c, n] for c, n in freq)
        print(freq)
        while len(res) < len(s):

            for i in range(len(freq)):

                if freq[i][1] != 0:
                    res.append(freq[i][0])
                    freq[i][1] -= 1

            for i in range(len(freq)):

                if freq[~i][1] != 0:
                    res.append(freq[~i][0])
                    freq[~i][1] -= 1

        res = ''.join(res)
        print(res)
        return res
