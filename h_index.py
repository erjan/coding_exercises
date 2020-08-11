'''
Given an array of citations (each citation is a non-negative integer) of a researcher, write a function to compute the researcher's h-index.

According to the definition of h-index on Wikipedia: "A scientist has index h if h of his/her N papers have at least h citations each, and the other N − h papers have no more than h citations each."
'''

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        c = citations
        c = sorted(c)
        h_index = 0
        for i in range(len(c)-1,-1,-1):
            cnt = len(c)-i
            if c[i] >=cnt:
                h_index = cnt
            else:
                break
        return h_index
