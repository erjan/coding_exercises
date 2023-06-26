'''
You are given a 0-indexed array words consisting of distinct strings.

The string words[i] can be paired with the string words[j] if:

The string words[i] is equal to the reversed string of words[j].
0 <= i < j < words.length.
Return the maximum number of pairs that can be formed from the array words.

Note that each string can belong in at most one pair.
'''


class Solution:
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:

        res = 0
        n = len(words)
        for i in range(n):
            temp = list(words[i])
            temp.reverse()
            temp = "".join(temp)
            for j in range(i+1, n):

                if words[j] == temp:
                    res+=1
        return res

-------------------------------------------------------------------------------------------
class Solution:
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:

        d = defaultdict(int)

        for word in words:
            d[min(word, word[::-1])]+= 1
        
        return  sum(map((lambda x: x*(x-1)), d.values()))//2

---------------------------------------------------------------------------------------  
