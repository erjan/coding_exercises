'''
Given an array of integers arr, return true if we can partition the array into three non-empty parts with equal sums.

Formally, we can partition the array if we can find indexes 
i + 1 < j with (arr[0] + arr[1] + ... + arr[i] == 
arr[i + 1] + arr[i + 2] + ... + arr[j - 1] == arr[j] + arr[j + 1] + ... + arr[arr.length - 1])
'''

def f(arr):

    total = sum(arr)
    if total % 3 != 0:
        return False

    target = total//3

    accum = 0
    counter = 0
    for num in arr:
        if counter == 2:
            return True
        accum += num
        if accum == target:
            counter += 1
            accum = 0
    return False
