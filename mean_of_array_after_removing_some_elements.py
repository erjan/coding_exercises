'''
Given an integer array arr, return the mean of the remaining integers 
after removing the smallest 5% and the largest 5% of the elements.

Answers within 10-5 of the actual answer will be considered accepted.
'''


class Solution:
    def trimMean(self, arr: List[int]) -> float:
        n = arr
        n = sorted(n)
        first_n = int(len(n)*5/100)
        largest_5_percent = n[first_n:]
        smallest_5_percent = n[:-first_n]
        temp = n[first_n: -first_n]

        res2 =  sum(temp)/ len(temp)
        res2 = round(res2,5)
        #print(res2)
        return res2
