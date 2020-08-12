'''
We are given two sentences A and B.  (A sentence is a string of space 
separated words.  Each word consists only of lowercase letters.)

A word is uncommon if it appears exactly once in one of the sentences, and does not appear in the other sentence.

Return a list of all uncommon words. 

You may return the list in any order.
'''

class Solution:
    def uncommonFromSentences(self, A: str, B: str) -> List[str]:
        a = (A.split(' '))
        b = (B.split(' '))

        ad = dict()
        bd = dict()

        for x in a:
            if x not in ad.keys():
                ad[x] = 1
            else:
                ad[x]+=1

        for x in b:
            if x not in bd.keys():
                bd[x] = 1
            else:
                bd[x]+=1

        res = []
        for x in a:
            if x not in b and ad[x] == 1:
                res.append(x)

        for x in b:
            if x not in a and bd[x] == 1:
                res.append(x)
        print(res)
        return res
