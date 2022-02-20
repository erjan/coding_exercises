'''
A distinct string is a string that is present only once in an array.

Given an array of strings arr, and an integer k, return the kth distinct string present in arr. 
If there are fewer than k distinct strings, return an empty string "".

Note that the strings are considered in the order in which they appear in the array.
'''


class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        d = dict()

        for i in range(len(arr)):
            if arr[i] not in d:
                d[arr[i]] = 1
            else:
                d[arr[i]] += 1

        res = list()
        for key, v in d.items():

            if v == 1:
                res.append([key, v])

        #print(res)
        k = k - 1

        for i in range(len(res)):
            if k == i:
                #print(res[i])
                return res[i][0]
        #print('not found')
        return ""
