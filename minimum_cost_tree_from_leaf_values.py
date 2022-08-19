'''Given an array arr of positive integers, consider all binary trees such that:

Each node has either 0 or 2 children;
The values of arr correspond to the values of each leaf in an in-order traversal of the tree.
The value of each non-leaf node is equal to the product of the largest leaf value in its left and right subtree, respectively.
Among all possible binary trees considered, return the smallest possible sum of the values of each non-leaf node. It is guaranteed this sum fits into a 32-bit integer.

A node is a leaf if and only if it has zero children.
'''


class Solution:
def mctFromLeafValues(self, arr: List[int]) -> int:
    
    arr = [float('inf')] + arr + [float('inf')]
    n, res = len(arr), 0
    
    while n>3:
        mi = min(arr)
        ind = arr.index(mi)
        
        if arr[ind-1]<arr[ind+1]:
            res+=arr[ind-1]*arr[ind]
        else:
            res+=arr[ind+1]*arr[ind]
        
        arr.remove(mi)
        n = len(arr)
    
    return res
