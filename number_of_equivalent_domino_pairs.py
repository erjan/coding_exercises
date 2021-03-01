'''
Given a list of dominoes, dominoes[i] = [a, b] is equivalent to 
dominoes[j] = [c, d] if and only if either (a==c and b==d), or (a==d and b==c) - that is, one domino can 
be rotated to be equal to another domino.

Return the number of pairs (i, j) for which 0 <= i < j < dominoes.length, and dominoes[i] is equivalent to dominoes[j].
'''

#my solution - using n choose k -math.comb for combinations

from itertools import combinations
import collections, math

class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:       
        dom = dominoes
        for d in dom:
            a,b = d[0], d[1]
            if a > b:
                d[0], d[1] = b,a

        res_dict = dict()
        for i in range(len(dom)):
            domino = dom[i]
            a,b = domino[0], domino[1]
            dom[i] = str(a)+str(b)
        c = collections.Counter(dom)
        total = 0
        for item in c.values():
            if item > 1:
                x =math.comb(item,2)
                total+=x
        return total
