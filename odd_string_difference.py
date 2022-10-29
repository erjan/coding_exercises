'''
You are given an array of equal-length strings words. Assume that the length of each string is n.

Each string words[i] can be converted into a difference integer array difference[i] of length n - 1 where difference[i][j] = words[i][j+1] - words[i][j] where 0 <= j <= n - 2. Note that the difference between two letters is the difference between their positions in the alphabet i.e. the position of 'a' is 0, 'b' is 1, and 'z' is 25.

For example, for the string "acb", the difference integer array is [2 - 0, 1 - 2] = [2, -1].
All the strings in words have the same difference integer array, except one. You should find that string.

Return the string in words that has different difference integer array.
'''

class Solution:
    def oddString(self, words: List[str]) -> str:

        diff = lambda x: [ord(x[j])-ord(x[j-1]) for j in range(1,len(x))]

        words.sort(key = diff)

        return words[0] if diff(words[0]) != diff(words[1]) else words[-1]
      
----------------------------------------------------------------------------------------------------
class Solution:
    def oddString(self, words: List[str]) -> str:
        hashmap = defaultdict(list)
        for w in words:
            difference = []
            for i in range(1,len(w)):
                difference.append(ord(w[i])-ord(w[i-1]))
            hashmap[tuple(difference)].append(w)
        for k,a in hashmap.items():
            if len(a) == 1:
                return a[0]
