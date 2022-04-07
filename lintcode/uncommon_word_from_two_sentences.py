'''

We are given two sentences A and B. (A sentence is a string of space separated words. Each word consists only of lowercase letters.)

A word is uncommon if it appears exactly once in one of the sentences, and does not appear in the other sentence.

Return a list of all uncommon words.

'''



from typing import (
    List,
)
from collections import Counter
class Solution:
    """
    @param a: Sentence A
    @param b: Sentence B
    @return: Uncommon Words from Two Sentences
    """
    def uncommon_from_sentences(self, a: str, b: str) -> List[str]:
        # Write your code here.

        res = []
        alist = a.split(' ')
        blist = b.split(' ')
        dic = {}
        for i in alist:
            if i not in dic:
                dic[i] = 1
            else:
                dic[i] += 1
        for i in blist:
            if i not in dic:
                dic[i] = 1
            else:
                dic[i] += 1
        for key in dic.keys():
            if dic[key] == 1:
                res.append(key)
        return res
