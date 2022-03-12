'''
In an alien language, surprisingly, they also use English lowercase letters, but possibly in a different order. The order of the alphabet is some permutation of lowercase letters.

Given a sequence of words written in the alien language, and the order of the alphabet, return true if and only if the given words are sorted lexicographically in this alien language.
'''

class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        mapping = dict(zip(order, [i for i in range(1, 27)]))
    
        for i in range(len(words)-1):

            w1 = words[i]
            w2 = words[i+1]
            min_len = min(len(w1), len(w2))

            if min_len != len(w1) and min_len == len(w2) and w1.startswith(w2):
                return False

            for j in range(min_len):
                if mapping[w1[j]] > mapping[w2[j]]:
                    return False

                if mapping[w1[j]] < mapping[w2[j]]:
                    break

        return True

