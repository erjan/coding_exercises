'''

We can represent a sentence as an array of words, for example, the sentence "I am happy with leetcode" can be represented as arr = ["I","am",happy","with","leetcode"].

Given two sentences sentence1 and sentence2 each represented as a string array and given an array of string pairs similarPairs where similarPairs[i] = [xi, yi] indicates that the two words xi and yi are similar.

Return true if sentence1 and sentence2 are similar, or false if they are not similar.

Two sentences are similar if:

They have the same length (i.e., the same number of words)
sentence1[i] and sentence2[i] are similar.
Notice that a word is always similar to itself, also notice that the similarity relation is not transitive. For example, if the words a and b are similar, and the words b and c are similar, a and c are not necessarily similar.
'''


class Solution:
    def areSentencesSimilar(self, sentence1: List[str], sentence2: List[str], similarPairs: List[List[str]]) -> bool:
        
        s1 = sentence1
        s2 = sentence2
        
        if len(s1) != len(s2):
            return False

        res = list(zip(s1, s2))
        res = [list(x) for x in res]

        res = list(filter(lambda x: x[0] != x[1], res))


        for i in range(len(res)):

            pair = res[i]
            print(pair)

            if pair not in similarPairs and [pair[1], pair[0]] not in similarPairs:
                return False

        return True
