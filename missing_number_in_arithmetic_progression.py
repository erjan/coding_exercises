'''
In some array arr, the values were in arithmetic progression: the values arr[i + 1] - arr[i] are all equal for every 0 <= i < arr.length - 1.

A value from arr was removed that was not the first or last value in the array.

Given arr, return the removed value.
'''


#my own solution

class Solution:
    def missingNumber(self, arr: List[int]) -> int:
        
        diff = min(abs(arr[-1]-arr[-2]), abs(arr[1]-arr[0]))
        print('diff', diff)
        
        if diff == 0:
            return arr[0]
        
        for i in range(len(arr)-1):
            if abs(arr[i+1] - arr[i]) > diff:
                res = min(arr[i+1], arr[i]) + diff
                print('res', res)
                return res

        print('end')
        
        
#ideal solution from discussions

class Solution:
    def missingNumber(self, arr: List[int]) -> int:
        totalTerms = len(arr) + 1
        expectedSum = totalTerms * (arr[0] + arr[-1]) // 2
        return expectedSum - sum(arr)
