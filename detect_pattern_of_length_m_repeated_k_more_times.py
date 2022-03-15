'''
Given an array of positive integers arr, find a pattern of length m that is repeated k or more times.

A pattern is a subarray (consecutive sub-sequence) that consists of one or more values, repeated multiple times consecutively without overlapping. A pattern is defined by its length and the number of repetitions.

Return true if there exists a pattern of length m that is repeated k or more times, otherwise return false.
'''

def f(arr, m, k):
    counter = 0

    for i in range(len(arr)-m):
        if (arr[i] == arr[i+m]):
            counter+=1
        else:
            counter= 0

            
        if counter == (k-1) *m:
            return True
    return False
